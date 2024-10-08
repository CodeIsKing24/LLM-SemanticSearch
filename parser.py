## We perform the following actions:
## - Read the chunked filed under chunks folder
## - Generate embeddings for the chunks
## - Store data in a CSV file (chunk_id, document_id, document_file_name, chunk_text, vector_embedding)
from sentence_transformers import SentenceTransformer
import os
import numpy as np
import pandas as pd

# model used to generate embeddings
MODEL = 'msmarco-distilbert-base-v4'
embedder = SentenceTransformer(MODEL)

output_filename = "output_data.csv"

# reads all files under listed directory
def read_files(directory):
    """Reads all text files in a given directory and returns their contents as a list."""
    search_corpus = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as f:
                search_corpus.append(f.read())
    return search_corpus

# writes embeddings into files
def generate_write_embeddings(file_name, chunks):
    json_data = []
    page_num = 1
    for chunk in chunks:
      #  print(vectors)
       # vector = embedder.encode(chunk, convert_to_tensor=True)
        vector = embedder.encode(chunk)
        data = {
                'chunk_id': page_num, 
                'document_id': page_num, 
                'document_file_name': 'mahabharat.txt', 
                'chunk_text': chunk, 
                'vector_embedding': vector
                }
        json_data.append(data)
        # output_filename = f"vector_{page_num + 1}.txt"
       # output_path = os.path.join(directory, output_filename)
        page_num = page_num + 1
       # np.savetxt(output_path, vectors, delimiter=",", fmt="%.8f")
    #df = pd.DataFrame(json_data, dtype={'vector_embedding': object})
    df = pd.DataFrame(json_data)
    # print(json_data)
    df.to_csv(file_name, index=False)


# Reads chunked files, converts into embeddings and writes to embeddings folder.
def main():
    folder_path_chunks = os.path.relpath("chunks/")
    folder_path_embeddings = os.path.relpath("embedding/")
    output_folder_path = os.path.join(os.path.relpath("output/"), output_filename)
    print("embedding path:" + folder_path_embeddings)
    sentences = read_files(folder_path_chunks)
    
   # embeddings = embedder.encode(sentences, convert_to_numpy=True)
    generate_write_embeddings(output_folder_path, sentences)


if __name__ == "__main__":
    main()