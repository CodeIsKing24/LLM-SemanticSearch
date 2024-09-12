Project leverages streamlit for basic UI creation for project setup.

Run the following commands:

Package deployment using conda package manager - 
- `conda create -n llm-project-phase1 python=3.12` (create a new python environment for the project)
- `conda activate llm-project-phase1` (activate the project environment)
- `conda install -n llm-project-phase1 conda` (install conda package)
- `conda update --all` (update all conda packages)
- `conda install PyTorch` (install PyTorch package)
- `conda install pandas` (install pandas package)
- `conda install numpy` (install numpy package)
- `conda install streamlit` (install streamlit package)
- `conda install spacy` (install spacy package)
- `conda install -c conda-forge sentence-transformers` (install sentence-transformers from conda-forge channel)
- `python -m spacy download en_core_web_sm`  (download spacy model used for semantic chunking)
- `conda install sqlalchemy`
- `conda install tensorflow`
- `conda install tf-keras`

Package deployment using pip package manager - 
- `pip install streamlit pandas requests` (install required libraries)
- `pip install -q sentence-transformers` (installs transformer libraries)
- `pip install PyPDF2` (installs PDF reader)
- `pip install torch` (installs pyTorch)
- `pip install numpy` (installs numpy)
- `pip install spacy` (installs spaCy semantic chunker library)
- `python -m spacy download en_core_web_sm` (download 'en_core_web_sm' model used by spaCy model for semantic chunking)
Note: You can also run command `pip install -r requirements.txt` to install all above packages

Required steps prior to streamlit app run:
- Create folders `chunks`, `embedding`, `inputs`, `output` under root directory
- run command `python semantic_chunker.py` to generate chunks under `chunks` folder
- run command `python parser.py` to generate vector embeddings and save it into a CSV file
- Finally start the streamlit app using command `streamlit run app.py`

Other useful commands:
- `conda deactivate` (deactivate the environment)
- `conda info --envs` (list all conda packages)
- `conda remove -n <environment_name> --all` (remove conda environment)
- `conda clean --all` (cleanup cache and temporary files)
- `pip uninstall -y -r requirements.txt` (uninstall all required files)
- `pip cache purge` (purge cache and temporary files)

Note:
- For pytorch installation, we can go to `https://pytorch.org/` website and scroll down to `INSTALL PYTORCH` section which will show the command to run on your machine for installation based on your existing config.
- For windows, conda environment should be created using python 3.11 to install pytorch and other packages.

Docker commands:
- Open terminal and navigate to root folder of the project
- `docker build -t sqlite-container .` (to build docker container)
- `docker run -it --rm sqlite-container` (run the container)