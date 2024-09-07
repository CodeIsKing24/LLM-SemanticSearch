We have multiple phases of the project. 
## Phase-1:
- Identify plan, small texts
- Create vector embeddings
- Add Search function
- Create Streamlit project

Gutenberg (https://www.gutenberg.org/).
Download 100 document, extract text and create embeddings.


## Phase-2:
- Start with a few hundred long texts. 
- CHUNKING - SEMANTIC chunking (ignore the image. Multi-modal learning will come later)
  - If we cannot do semantic chunking, do brute force chunking.
  - Save the chunks to a CSV file. (chunk_id, document_id, document_file_name, chunk_text, vector_embedding)
- When you search, you will get back chunk_id. (search is on embedding. Don’t use Elastic search. Goal is to use semantic search)

## Phase-3:
- Semantic Chunking 
- Put document text, chunks in database (mariadb/mysql/sqllite)
    -   We will use docker for the database. 

## Phase-4:
- Multiple document formats.. (PDF, word docs, markdown, html, text, postscript)
    - We also have OCR tools that can extract data from images.

## Phase-5:
- Put vectors into a ANN (approx. nearest neighbor) index and search there..
    - FAISS → is the most popular vector database.
    - FAISS is enterprise grade ANN. (People index hundreds of billions of vectors in FAISS and still response time is in milli-seconds. Facebook open-sourced project)

## Phase-6: (Optional)
- Put search functionality in a REST application. (Use FastAPI)
    - Some people might use FLASK..
    - For UI, create simple UI in React. 

## Phase-7:
-   Hybrid Search (Keyword search + Semantic Search)
    -   Keyword search → Python library
Interweave results by relevance. Pass the two results into RERANKER. 

## Phase-8: (Optional)
-   Use COLBERTv2 to generate embeddings. It generates better embeddings.

Notes: Late Interaction Theory - To generate multiple 
