import os
import chardet
from tqdm import tqdm
import chromadb
from chromadb.utils import embedding_functions

# 경로 설정
# CHROMA_DATA_PATH = "chroma_data/"
MODEL = "all-MiniLM-L6-v2"
COLLECTION = "cosine"
DATA = "/mnt/c/LogPatternFinder/CromaDB/log"

# 임베딩 모델 정의
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)

# ChromaDB 클라이언트 초기화
client = chromadb.HttpClient(host='localhost', port=8001)

# 컬렉션 가져오거나 생성
collection = client.get_or_create_collection(
    name=COLLECTION,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"},
)

# 파일 인코딩 감지 함수
def detect_encoding(file_path):
    rawdata = open(file_path, mode='rb').read()
    encoding = chardet.detect(rawdata)['encoding']
    return encoding

# 파일 인코딩을 UTF-8로 변환하는 함수
def convert_to_utf8(file_path, encoding):
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            data = f.read()
            print(f"Read {file_path} to UTF-8")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)
            print(f"Write {file_path} to UTF-8")
    except:
        print('Failed to convert encoding')

# 로그 파일을 읽어와 처리하는 함수
def read_log_files(DATA):
    for file_name in tqdm(os.listdir(DATA), desc="Processing Files"):
        file_path = os.path.join(DATA, file_name)
        encoding = detect_encoding(file_path)
        convert_to_utf8(file_path, encoding)

        with open(file_path, 'r', encoding='utf-8') as file:
            process_log_events(file)
            print(f"Processed {file_name}")

# 로그 이벤트를 처리하여 컬렉션에 추가하는 함수
def process_log_events(file):
    index = 1
    for line in file:
        collection.add(
            documents=line,
            metadatas={'source': 'log'},
            ids=[str(index)]
        )
        index += 1

# 메인 함수
if __name__ == "__main__":
    read_log_files(DATA)
    print("SUCCESS")
    print("Total documents in collection:", collection.count())