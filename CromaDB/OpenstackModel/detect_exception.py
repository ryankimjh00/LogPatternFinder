import chromadb
from chromadb.utils import embedding_functions

CHROMA_DATA_PATH = "chroma_data/"
COLLECTION_NAME = "cosine"
EMBED_MODEL = "all-MiniLM-L6-v2"
OUTPUT_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/output.log"
DETECT_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/detect.log"
THRESHOLD_DISTANCE = 0.5  # 여기에 적절한 기준 거리를 설정하세요

client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)
collection = client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

with open(OUTPUT_LOG_PATH, "r") as log_file:
    with open(DETECT_LOG_PATH, "w") as detect_file:
        for line in log_file:
            results = collection.query(query_texts=[line.strip()], n_results=1)
            distance = results['distances'][0][0]
            if distance >= THRESHOLD_DISTANCE:
                detect_file.write(f"거리: {distance}, 원본로그: {line.strip()}\n")

print("detect.log 파일에 결과가 저장되었습니다.")
