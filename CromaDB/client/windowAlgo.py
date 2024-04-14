from datetime import datetime, timedelta
import os
import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import json
from concurrent.futures import ProcessPoolExecutor

CHROMA_DATA_PATH = "chroma_data/"
MODEL = "all-MiniLM-L6-v2"
COLLECTION = "log_collection"
DATA = "log"

date_format = '%y.%m.%d %H:%M:%S'

#embedding 모델 정의
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)

#client가 사용할 데이터 파일 선택
#client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)
client = chromadb.HttpClient(host='localhost', port=8001)

# Get a collection object from an existing collection, by name. If it doesn't exist, create it.
collection = client.get_or_create_collection(
    name=COLLECTION,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"}, #사용 알고리즘 정의 가능
)

result = ''
current_time = None
index = 1

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            sliding_window_1_minute(line)
    print('success to read log file')
    return

def sliding_window_1_minute(log_events):
    global result
    global current_time
    global index
    
    try:
        event_time = log_events[1:15]
    except (SyntaxError, NameError, IndexError, AttributeError) as e:
        print(f'Failed due to {type(e).__name__}')

    if current_time is None:
        current_time = event_time
        
    if current_time != event_time:
        current_time = event_time
        collection.add(
            documents=result,
            metadatas={'source': 'log'},
            ids=[str(index)]
        )
        result = ''
        index = index + 1
    result += log_events[28:]
    return

collections = client.list_collections()

if __name__ == "__main__":
    try:
        log_file_path = '/mnt/c/LogPatternFinder/CromaDB/client/chroma_data/tester.log'
        read_log_file(log_file_path)
        print("Collections:")
        for collection in collections:
            print(collection)
    except (SyntaxError, NameError, IndexError, AttributeError) as e:
        client.delete_collection(COLLECTION)
        print(f'Failed due to {type(e).__name__}')