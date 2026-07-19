# Setup Instructions

## Prerequisites

Before you can use this project, you need to set up a few things:

1. **Clone the repository**
   ```bash
   git clone https://github.com/scott2121/sparql_query_generater.git
   cd sparql_query_generater
   ```

2. **Install rdf-config dependencies**
   ```bash
      cd rdf-config
      bundle install
      cd ..
      ```
      The `rdf-config` repository (with updated `model.yaml` variable names and added Uniprot & Bgee set models) is included in this project and is required for the SPARQL query generation process.

3. **Create and configure .env file**
   ```bash
   cp .env_sample .env
   ```
   
   Then edit the .env file to set:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `PATH_RDF_CONFIG`: Path to the rdf-config directory you just cloned (e.g., `/home/username/sparql_query_generater/rdf-config/`)
   - `PATH_DIR`: Path to this project directory (e.g., `/home/username/sparql_query_generater/`)
   - Other endpoints and paths as needed

4. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

5. **Running the examples**
   After completing the setup, you can open and run one of the demo notebooks directly in VS Code:
   ```bash
   code demo_propose.ipynb
   ```
   Or use your preferred Jupyter notebook environment to open `demo_propose.ipynb`.
