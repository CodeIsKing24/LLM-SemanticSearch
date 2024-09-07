import spacy
import os

def chunk_text(text, chunk_size=1000):
    """Chunks text into smaller segments for processing."""
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def process_chunk(chunk, nlp):
    """Processes a chunk of text using spaCy's syntactic parser."""
    doc = nlp(chunk)
    sents = list(doc.sents)
    return sents

def perform_semantic_chunking(file_path, chunk_size=1000):
    """Performs semantic chunking on a large text file."""
    nlp = spacy.load("en_core_web_sm")  # Load a spaCy model (adjust as needed)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text, chunk_size)

    semantic_chunks = []
    for chunk in chunks:
        semantic_chunks.extend(process_chunk(chunk, nlp))

    return semantic_chunks


# Reads file and performs semantic chunking and writed to chunks folder.
def main():
    file_path = os.path.relpath("inputs/mahabharat.txt")
    semantic_chunks = perform_semantic_chunking(file_path)
    page_num = 1
    for chunk in semantic_chunks:
        # print(chunk.text)
        output_filename = f"page_{page_num}.txt"
        output_path = os.path.join(os.path.relpath("chunks/"), output_filename)
        page_num = page_num + 1
        with open(output_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(chunk.text)
    print("total number of chunks")
    print(page_num)

if __name__ == "__main__":
    main()