import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import json

CHROMA_DATA_PATH = "chroma_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "test3"
FILE_NAME = "/mnt/c/LogPatternFinder/CromaDB/client/chroma_data/testData.json"

#embedding 모델 정의
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)

#client가 사용할 데이터 파일 선택
client = chromadb.HttpClient(host='localhost', port=8001)

#collection 생성
collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"}, #사용 알고리즘 정의 가능
)

collections = client.list_collections()

def add_data_database(sec_col, data):
    text_list = data['text'].tolist()
    genre_list = data['genres'].tolist()
    sec_col.add(
        documents=text_list,
        ids=[f"id{i}" for i in range(len(text_list))], 
        metadatas=[{"genre": g} for g in genre_list]  #군집
    )

def read_json_file():
    filename = FILE_NAME
    df = pd.read_json(filename)
    return df

if __name__ == "__main__":
    try:
        dataframe = read_json_file()
        add_data_database(collection,dataframe)
        print('success')
        # 컬렉션 리스트 출력
        print("Collections:")
        for collection in collections:
            print(collection)
    except SyntaxError :
        client.delete_collection(COLLECTION_NAME)
        print(f's fail')
    except NameError :
        client.delete_collection(COLLECTION_NAME)
        print(f'n fail')
    except IndexError :
        client.delete_collection(COLLECTION_NAME)
        print(f'i fail')
    except AttributeError  :
        client.delete_collection(COLLECTION_NAME)
        print(f'a fail')
