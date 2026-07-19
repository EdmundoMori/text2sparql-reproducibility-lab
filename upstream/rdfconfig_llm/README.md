
# SPARQL Query Generation Benchmark

## Overview

This project is a benchmark tool for generating SPARQL queries based on questions, with configurable database options and difficulty levels. It evaluates the accuracy of query results against expected answers.


## Usage

For detailed setup instructions, please see [SETUP.md](SETUP.md).

### How to Execute

Below is an example workflow for generating and evaluating SPARQL queries using this project. This example is based on the steps in `demo_propose.ipynb`:

1. **Set Environment Variables**
   - Make sure to set `OPENAI_API_KEY` and `PATH_DIR` in your `.env` file.
   - Also set the database endpoint, e.g., `ENDPOINT_RHEA` for the Rhea database.

2. **Select Database and Parameters**
   - Choose the target database (e.g., `rhea`, `bgee`, `uniprot`, etc.).
   - Set prompt and variable IDs according to the database.
   - Set difficulty level (`EASY`, `MEDIUM`, `HARD`).

3. **Load Questions**
   - Load questions from the JSON dataset:
     ```python
     with open(f"questions/json_format/{db}.json", 'r') as f:
         questions = json.load(f)
     ```

4. **Generate Prompts**
   - Use the prompt maker to fill in prompts for each question:
     ```python
     questions = make_prompt(db, prompt_id, prompt_variable_id, questions)
     ```

5. **Generate SPARQL Queries**
   - Use the language model and RDF config to generate SPARQL queries:
     ```python
     questions = sparql_gen(db, questions, verbose)
     ```

6. **Execute SPARQL Queries**
   - Send generated queries to the database endpoint and collect results:
     ```python
     for question in questions:
         result = execute_query(question, endpoint, "llm_rdf_result", 10000, "")
         question["results"] = result
     ```

7. **Save Results**
   - Save the questions and results to a file:
     ```python
     with open(save_path, "w") as f:
         json.dump(questions, f, indent=2)
     ```

8. **Evaluate Results**
   - Compare generated results with correct answers using Jaccard evaluation:
     ```python
     score = evaluate_jaccard(questions, answers)
     print(score)
     ```

This workflow can be run interactively in a Jupyter notebook or adapted to a Python script. For more details, see the code in `demo_propose.ipynb`.

## Current Development Status

Currently under development:

- Functionality to generate SPARQL queries related to questions for known databases and evaluate the accuracy of the results.

## Dataset Explanation

The `questions` directory contains datasets in two formats:

- **JSON format** (`questions/json_format/`):
  - Each file contains a list of question objects, typically including fields such as `question`, `database`, `difficulty`, and expected SPARQL query or answer.
  - Example structure:
    ```json
    [
      {
        "question": "What is the gene expression of X?",
        "database": "bgee",
        "difficulty": "easy",
        "expected_sparql": "SELECT ..."
      },
      ...
    ]
    ```

- **TTL format** (`questions/ttl_format/`):
  - Files are in Turtle (RDF) format, representing questions and metadata as RDF triples.
  - Example structure:
    ```ttl
    @prefix ex: <http://example.org/> .
    ex:question1 a ex:Question ;
      ex:text "What is the gene expression of X?" ;
      ex:database "bgee" ;
      ex:difficulty "easy" ;
      ex:expected_sparql "SELECT ..." .
    ```

These datasets are used to benchmark SPARQL query generation and result evaluation for different databases and question types.



## License


All files in this repository are distributed under the [MIT License](https://opensource.org/license/mit "The MIT License").

## Licenses of External Libraries

- **rdf-config**: Distributed under the [MIT License](https://opensource.org/license/mit/)

## Contact
- Hikaru Nagazumi (max.hikaru@fuji.waseda.jp)

## History

2025/Aug/01; initial version
