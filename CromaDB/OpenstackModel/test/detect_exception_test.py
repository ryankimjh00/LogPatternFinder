import os
import glob

import chromadb
from chromadb.utils import embedding_functions

COLLECTION = "cosine"
MODEL = "all-MiniLM-L6-v2"
OUTPUT_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/OpenstackModel/test/output.txt"
LOG_DIRECTORY = "/mnt/c/LogPatternFinder/gensim/test/embed"
THRESHOLD = 0.5

client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)
collection = client.get_collection(name=COLLECTION, embedding_function=embedding_func)

with open(OUTPUT_LOG_PATH, "w") as detect_file:
    for log_file in glob.glob(os.path.join(LOG_DIRECTORY, "*.txt")):
        with open(log_file, "r") as file:
            document = " ".join(file.readlines())  # 파일 내용을 하나의 문자열로 읽어들임
            results = collection.query(query_texts=[document], n_results=1)
            distance = results['distances'][0][0]
            # if distance >= THRESHOLD:
            detect_file.write(f"File: {os.path.basename(log_file)}, 거리: {distance}\n")

print("output.txt 파일에 결과가 저장되었습니다.")
