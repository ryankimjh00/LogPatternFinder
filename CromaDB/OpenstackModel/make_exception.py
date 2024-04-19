import chromadb

# ChromaDB 클라이언트 초기화
client = chromadb.HttpClient(host='localhost', port=8001)

# 모든 컬렉션 목록 가져오기
collections = client.list_collections()

# 출력
print("All collections:")
for collection in collections:
    print(collection)
