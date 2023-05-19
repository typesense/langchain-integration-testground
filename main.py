from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Typesense
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI

def main():
    with open("state_of_the_union.txt") as f:
        state_of_the_union = f.read()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(state_of_the_union)

    embeddings = OpenAIEmbeddings()
    docsearch = Typesense.from_texts(texts,
                                     embeddings,
                                     metadatas=[{"source": f"{i}-pl"} for i in range(len(texts))],
                                     typesense_client_params={
                                         'host': 'localhost',   # Use xxx.a1.typesense.net for Typesense Cloud
                                         'port': '8108',        # Use 443 for Typesense Cloud
                                         'protocol': 'http',   # Use https for Typesense Cloud
                                         'typesense_collection_name': 'lang'
                                     })
    chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="stuff", retriever=docsearch.as_retriever())
    response = chain({"question": "What did the president say about Justice Breyer"}, return_only_outputs=True)

    print(response)


if __name__ == '__main__':
    main()

