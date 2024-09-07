Project leverages streamlit for basic UI creation for project setup.

Run the following commands:
- `conda create -n llm-project-phase1 python=3.12` (create a new python environment for the project)
- `conda activate llm-project-phase1` (activate the project environment)
- `pip install streamlit pandas requests` (install required libraries)
- `pip install -q sentence-transformers` (installs transformer libraries)
- `pip install PyPDF2` (installs PDF reader)
- `pip install torch` (installs pyTorch)
- `pip install spacy` (installs spaCy semantic chunker library)
- `python -m spacy download en_core_web_sm` (download 'en_core_web_sm' model used by spaCy model for semantic chunking)
- `conda deactivate` (deactivate the environment)
- Create folders `chunks`, `embedding`, `inputs`, `output` under root directory
- run command `python semantic_chunker.py` to generate 