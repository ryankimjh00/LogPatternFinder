import os
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess

def read_documents(directory):
    documents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    text = f.read()
                    processed_text = simple_preprocess(text)
                    tagged_doc = TaggedDocument(processed_text, [file])
                    documents.append(tagged_doc)
    return documents

def train_doc2vec_model(documents, vector_size=100, window=5, min_count=1, epochs=20):
    model = Doc2Vec(vector_size=vector_size, window=window, min_count=min_count, workers=4)
    model.build_vocab(documents)
    model.train(documents, total_examples=model.corpus_count, epochs=epochs)
    model.save("doc2vec")
    return model

def main():
    directory_path = "/mnt/c/LogPatternFinder/gensim/test/out"
    documents = read_documents(directory_path)
    model = train_doc2vec_model(documents)

    # 예시: 특정 문서에 대한 벡터 확인
    example_document_path = os.path.join(directory_path, "log_2011.12.19 19:26:02.txt")
    example_document_text = open(example_document_path, "r").read()
    example_document_vector = model.infer_vector(simple_preprocess(example_document_text))
    print("Example document vector:", example_document_vector)

if __name__ == "__main__":
    main()
