import chromadb
from chromadb.utils import embedding_functions
import math
import time

start = time.time()
CHROMA_DATA_PATH = "chroma_data/"
COLLECTION = "test3"
MODEL = "all-MiniLM-L6-v2"

client = chromadb.HttpClient(host='localhost', port=8001)
#client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)

#print(client.list_collections())

#이곳에서 넣은 embedding funtion을 사용하여 쿼리를 embedding
collection = client.get_collection(name=COLLECTION, embedding_function=embedding_func)


results = collection.query(
    #위에서 설정한 embedding function을 활용하여 기본적으로 embedding
    #2.35525 sec
    #query_embeddings=embedding_func(['iPhone']),
    
    #2.30656 sec 
    #결과 값 같음 
    query_texts = ['iPhone']
    
)


print(results)

end = time.time()

print(f"{end - start:.5f} sec")