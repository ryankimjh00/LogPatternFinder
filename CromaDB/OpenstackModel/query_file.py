import chromadb
from chromadb.utils import embedding_functions

CHROMA_DATA_PATH = "chroma_data/"
COLLECTION_NAME = "cosine"
EMBED_MODEL = "all-MiniLM-L6-v2"
EXCEPTION_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/output.log"
RESULT_OUTPUT_PATH = "result.log"

client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)
collection = client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

# 결과를 담을 리스트
result_list = []

with open(EXCEPTION_LOG_PATH, "r") as log_file:
    for line in log_file:
        results = collection.query(query_texts=[line.strip()], n_results=1)
        result_list.append((results['distances'][0], line.strip()))

# 거리를 기준으로 내림차순 정렬
result_list.sort(reverse=True, key=lambda x: x[0])

# 결과를 파일에 출력
with open(RESULT_OUTPUT_PATH, "w") as result_file:
    for dist, log in result_list:
        result_file.write(f"거리: {dist}, 원본로그: {log}\n")

print("결과가 result.log 파일에 저장되었습니다.")
