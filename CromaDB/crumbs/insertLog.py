from datetime import datetime, timedelta
import os
import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import json
from concurrent.futures import ProcessPoolExecutor
import chardet # 패키지 설치 필요(encode 변환)

CHROMA_DATA_PATH = "chroma_data/"
MODEL = "all-MiniLM-L6-v2"
COLLECTION = "cosine"
DATA = "log"

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

# file_path -> Encoding Type
def is_encoded(file_path):
    rawdata = open(file_path, mode='rb').read()
    data = chardet.detect(rawdata)
    result = data['encoding']
    return result

# File_path, Encoding_Type -> Change Files encoding type
def to_utf8(file_path, encoding_in):
    try:
        with open(file_path, 'r', encoding=encoding_in) as f:
            datas = f.read()

        with open(file_path, 'w', encoding='utf-8') as k:
            k.write(datas)
    except:
        print('변환 실패')


result = ''
current_time = None
current_min = None
index = 1

def read_log_file(DATA):
    global result
    global current_time
    global current_min


    for file_name in os.listdir(DATA):
        to_utf8(os.path.join(DATA, file_name), is_encoded(os.path.join(DATA, file_name)))
        print(file_name)
        with open(os.path.join(DATA, file_name), 'r', encoding='UTF-8') as file:
            
            for line in file:
                sliding_window_30_sec(line)
            collection.add(
            documents=result,
            metadatas={'source': 'log'},
            ids=[str(index)]
            )
            result = ''
            current_time = None
            current_min = None

        print('done 2')
        
        #TODO : 파일이 바뀔때 현재시간을 어떻게 할지 (0)
        #TODO : 시간이 59초인 경우 지나가는 경우가 있음(이 경우 처리 필요) (0)
        #TODO : error 분리 안함
    return

def sliding_window_30_sec(log_events):
    global result
    global current_time
    global current_min
    global index
    
    print(log_events[20:27])
    if 'INFO' not in log_events[20:27] and 'DEBUG' not in log_events[20:27]:
        return
    event_time = log_events[16:18]
    if len(log_events) >= 15:
        event_min = log_events[14]
    else:
        result += log_events
        return
    #event_min = log_events[14]
    if event_min:
        if not (47 < ord(event_min) and ord(event_min) < 58):
                result += log_events
                return
    print('event_time', event_time)
    print('event_min', event_min)
    if event_time: 
        for i in event_time:
            if not (47 < ord(i) and ord(i) < 58):
                result += log_events
                return
    else:
        return
    
    
    if current_time is None and current_min is None:
        
        current_time = int(event_time) + 30
        current_min = int(event_min)
        print(current_min)
        if int(current_time) >= 60:
            current_time -= 60
            current_min += 1

    print(f'{current_min} : {current_time}')
    if int(current_min) == 10 and int(event_min) != 9:
        print("ssss")
        current_min = 0
    if (int(current_min) == int(event_min) and int(current_time) <= int(event_time)) or (int(current_min) < int(event_min) and int(current_time) <= int(event_time)):
        print(result)
        print('#########################')
        print('event_time', event_time)
        print('current_time', current_time)
        print('#########################')
        collection.add(
            documents=result,
            metadatas={'source': 'log'},
            ids=[str(index)]
        )
        
        result = ''
        index = index + 1
        current_time = int(event_time) + 30
        current_min = int(event_min)
        if current_time >= 60:
            current_time -= 60
            current_min += 1

    result += log_events[27:]
    return


if __name__ == "__main__":
    
    read_log_file(DATA)
    print("SUCCESS")
    print(collection.count())
    