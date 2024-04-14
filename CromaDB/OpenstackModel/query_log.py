import chromadb
from chromadb.utils import embedding_functions
import math
import time


CHROMA_DATA_PATH = "chroma_data/"
COLLECTION = "cosine"
MODEL = "all-MiniLM-L6-v2"


client = chromadb.HttpClient(host='localhost', port=8001)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=MODEL
)
collection = client.get_collection(name=COLLECTION, embedding_function=embedding_func)

start = time.time()
results = collection.query(
    
    query_texts = ['[.. ::] [ERROR]  [quartzScheduler_Worker- org.quartz.core.JobRunShell: ] - Job crawler.kr_tunnel_info threw an unhandled Exception: '],
    n_results=1
)
end = time.time()
print(f"거리가 가장 가까운 애들 10개의 거리: {results}")
print(f"소요시간: {end - start:.5f} sec")

"""
{
   "ids":[
      [
         "561"
      ]
   ],
   "distances":[
      [
         0.6558767557144165
      ]
   ],
   "embeddings":"None",
   "metadatas":[
      [
         {
            "source":"log"
         }
      ]
   ],
   "documents":[
      [
         "[.. ::] [INFO ]  [New I/O  worker # com.indigo.fileserver.IndigoFileServerHandler: ] - server closed : [id: xfa, /...: :> /...:] DISCONNECTED\n"
      ]
   ],
   "uris":"None",
   "data":"None"
}
"""