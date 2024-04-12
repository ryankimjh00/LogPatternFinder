import chromadb
from chromadb.utils import embedding_functions
import re

CHROMA_DATA_PATH = "chroma_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "test3"
FILE_NAME = "/mnt/c/LogPatternFinder/CromaDB/log/tester.log"

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)
client = chromadb.HttpClient(host='localhost', port=8001)
collection = client.get_or_create_collection(
    name=COLLECTION_NAME, embedding_function=embedding_func
)

def preprocess_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = re.sub(r'\d+', '', text)
    return text

def embed_log_documents(file_path, collection):
    count = collection.count()
    documents = []
    metadatas = []
    ids = [str(i) for i in range(count, count + len(documents))]
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        for i in range(0, num_lines, 10):
            batch_lines = lines[i:i+10]
            processed_text = preprocess_log_lines(batch_lines)
            document = {"text": processed_text}
            embedding = collection.add(
                ids=ids[i : i + 100],
                documents=documents[i : i + 100],
                metadatas=metadatas[i : i + 100],  # type: ignore
            )
            collection.insert_one(embedding)

def preprocess_log_lines(lines):
    processed_text = ''.join([re.sub(r'\d+', '', line) for line in lines])
    return processed_text.strip() 

log_file_path = FILE_NAME

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"}
)

if __name__ == "__main__":
    embed_log_documents(log_file_path, collection) 