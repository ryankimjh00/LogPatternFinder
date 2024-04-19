import chromadb
from chromadb.utils import embedding_functions

COLLECTION = "cosine"
MODEL = "all-MiniLM-L6-v2"
DETECT_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/detect.txt"
OUTPUT_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/OpenstackModel/detection_out/log_2011.12.19 19:26:02.txt"
THRESHOLD = 0.5 

client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)
collection = client.get_collection(name=COLLECTION, embedding_function=embedding_func)

with open(OUTPUT_LOG_PATH, "r") as log_file:
    with open(DETECT_LOG_PATH, "w") as detect_file:
        for line in log_file:
            results = collection.query(query_texts=[line.strip()], n_results=1)
            distance = results['distances'][0][0]
            if distance >= THRESHOLD:
                detect_file.write(f"거리: {distance}, 원본로그: {line.strip()}\n")

print("detect.log 파일에 결과가 저장되었습니다.")
