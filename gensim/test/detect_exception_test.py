import os
import glob

import chromadb
from chromadb.utils import embedding_functions

COLLECTION = "tester"
MODEL = "all-MiniLM-L6-v2"
OUTPUT_LOG_PATH = "/mnt/c/LogPatternFinder/CromaDB/OpenstackModel/test/output.txt"
LOG_DIRECTORY = "/mnt/c/LogPatternFinder/CromaDB/OpenstackModel/test/out"
THRESHOLD = 0.5

client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)
collection = client.get_collection(name=COLLECTION, embedding_function=embedding_func)

with open(OUTPUT_LOG_PATH, "w") as detect_file:
    for log_file in glob.glob(os.path.join(LOG_DIRECTORY, "*.log")):
        with open(log_file, "r") as file:
            for line in file:
                results = collection.query(query_texts=[line.strip()], n_results=1)
                distance = results['distances'][0][0]
                # if distance >= THRESHOLD:
                detect_file.write(f"File: {os.path.basename(log_file)}, 거리: {distance}, 원본로그: {line.strip()}\n")

print("output.txt 파일에 결과가 저장되었습니다.")
