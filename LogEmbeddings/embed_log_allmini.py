import os
import chardet
import chromadb
from chromadb.utils import embedding_functions

MODEL = "all-MiniLM-L6-v2"
COLLECTION = "normal_docs"
DATA = "/mnt/c/LogPatternFinder/LogEmbeddings/normal_docs"
file_index = 1

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)

client = chromadb.HttpClient(host='localhost', port=8001)

collection = client.get_or_create_collection(
    name=COLLECTION,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"},
)

def detect_encoding(file_path):
    rawdata = open(file_path, mode='rb').read()
    encoding = chardet.detect(rawdata)['encoding']
    return encoding

def convert_to_utf8(file_path, encoding):
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            data = f.read()
            # print(f"Read {file_path} to UTF-8")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)
            # print(f"Write {file_path} to UTF-8")
    except:
        print('❌ Failed to convert encoding')
        
def read_log_files(DATA):
    global file_index
    total_files = len(os.listdir(DATA))
    print("Total files:", total_files)
    for file_name in os.listdir(DATA):
        file_path = os.path.join(DATA, file_name)
        encoding = detect_encoding(file_path)
        convert_to_utf8(file_path, encoding)

        with open(file_path, 'r', encoding='utf-8') as file:
            process_log_events(file, file_path)
            print(f"✅ Complete Embedding {file_index}/{total_files}")
            file_index += 1

def process_log_events(file, file_path):
    index = 1
    document = file.read()
    print(f"⌛ Embedding {os.path.basename(file_path)}")
    collection.add(
        documents=document,
        metadatas={'source': 'log'},
        ids=[str(index)]
    )
    

# 메인 함수
if __name__ == "__main__":
    read_log_files(DATA)
    print("SUCCESS")
    print("Total documents in collection:", file_index, collection.count())
