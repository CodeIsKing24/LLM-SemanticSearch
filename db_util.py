import sqlite3
import json

class SqliteUtil:
    def create_database(self):
        conn = sqlite3.connect('semantic_search.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS embeddings (
                id INTEGER PRIMARY KEY,
                vector TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metadata (
                id INTEGER PRIMARY KEY,
                embedding_id INTEGER,
                chunk_id INTEGER,
                document_id INTEGER,       
                chunk_text TEXT,
                file_name TEXT,       
                FOREIGN KEY (embedding_id) REFERENCES embeddings(id)
            )
        ''')

        conn.commit()
        conn.close()

    # Function receives list of data objects and writes them to Sqlite database
    def write_data(self, data_list):
        conn = sqlite3.connect('semantic_search.db')
        cursor = conn.cursor()
        # Iterate thru data list
        for data in data_list:
            print(data)
            embedding_data = json.dumps(data['vector_embedding'].tolist())
            cursor.execute("INSERT INTO embeddings (vector) VALUES (?)", (embedding_data,))
            embedding_id = cursor.lastrowid
            # Example: Store an embedding and its metadata
            cursor.execute("INSERT INTO metadata (embedding_id, chunk_id, document_id, chunk_text, file_name) VALUES (?, ?, ?, ?, ?)", (embedding_id, data['chunk_id'], data['document_id'], data['chunk_text'], data['document_file_name']))
        conn.commit()
        conn.close()

    # Function queries Sqlite database and retrieves the 
    def read_data(self):
        conn = sqlite3.connect('semantic_search.db')
        cursor = conn.cursor()
        # Execute the JOIN query
        query = """
        SELECT E.id, E.vector, M.chunk_text, M.file_name, M.document_id, M.chunk_id
        FROM embeddings E
        INNER JOIN metadata M ON E.id = M.embedding_id
        """
        cursor.execute(query)
        # Fetch all rows from the result set
        result = cursor.fetchall()

        column_names = ['vector_id', 'vector_embedding', 'chunk_text', 'document_file_name', 'document_id', 'chunk_id'] 
        results = []
        for row in result:
            json_data = {
                column_names[i]: row[i]
                for i in range(len(column_names))
            }
            results.append(json_data)
        conn.close()
        return results

# Runs the code locally
def main():
    create_database()


if __name__ == "__main__":
    main()