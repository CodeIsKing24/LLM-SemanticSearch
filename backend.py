import numpy as np
import torch
import os
import pandas as pd

from sentence_transformers import SentenceTransformer, util

class SSearch:
    #load the vector embeddings from file
    def __init__(self): 
        self.embeddings = []
        self.chunks = []
        self.MODEL = 'msmarco-distilbert-base-v4'
        self.embedder = SentenceTransformer(self.MODEL)
        csv_file_name = os.path.join(os.path.relpath("output/"), "output_data.csv")
        df = pd.read_csv(csv_file_name)
        embedding_strings = df['vector_embedding'].tolist()
        nd_array = [np.fromstring(embedding_string[1:-1], sep=' ') for embedding_string in embedding_strings]
        self.embeddings = [torch.from_numpy(nd_string).float() for nd_string in nd_array]
        #self.embeddings = [np.fromstring(embedding_string[1:-1], sep=' ') for embedding_string in embedding_strings]
        self.chunks = df['chunk_text'].tolist()

    # builds JSON response object with search results
    def build_json_response(self, search_results):
        json_response = []
        for index, result in enumerate(search_results[0]):
            data = {
                'Search Rank': index, 
                'Relevance Score': result["score"], 
                'Document Chunk': self.chunks[result['corpus_id']] 
                }
            json_response.append(data)
        return json_response
    
    # prints search results
    def print_results(self, search_results):
        for index, result in enumerate(search_results[0]):
            print('-'*80)
            print(f'Search Rank: {index}, Relevance score: {result["score"]} ')
            print(self.chunks[result['corpus_id']])

    # Search function which will search against vector embeddigns
    def search(self, query):
        print("Query:" + query)
        # Replace with your backend API URL
        #url = "https://your-backend-api/search"
        # Send a GET request with the query as a parameter
        # response = requests.get(url, params={"query": query})
        # build vector embeddings for query string
        query_embedding = self.embedder.encode(query, convert_to_tensor=True)
        search_results = util.semantic_search(query_embedding, self.embeddings, top_k=10)
        json_response = self.build_json_response(search_results)
        print(json_response)
        return json_response 

my_obj = SSearch()
results = my_obj.search("Arjun")
#my_obj.print_results(results)