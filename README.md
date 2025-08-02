# HomeMatch-AI

An AI-powered real estate tool that generates a database of fictional property listings and uses vector search to find the best matches for a user's preferences.

## Project Description

"HomeMatch-AI" is an innovative application designed to demonstrate the power of combining Large Language Models (LLMs) with vector databases for personalized search experiences. The application simulates a real estate agent by first using a generative AI model to create a diverse set of real estate listings. These listings are then converted into vector embeddings and stored in a database. When a user provides their preferences in natural language, the application performs a semantic search to find the most relevant properties and then uses the LLM again to rewrite the descriptions, highlighting the features most appealing to the user.

## Features

* **Generative Listing Creation:** Automatically generates realistic real estate listings and neighborhood descriptions using OpenAI's `gpt-3.5-turbo`.
* **Vector Database Integration:** Stores property listings as vector embeddings in a ChromaDB instance for efficient semantic search.
* **Natural Language Preference Parsing:** Collects and interprets user preferences in natural language to form a query.
* **Semantic Search:** Finds properties that are semantically similar to the user's preferences, going beyond simple keyword matching.
* **Personalized Description Augmentation:** Rewrites and personalizes the retrieved listing descriptions to emphasize features of interest to the specific buyer.

## Technologies Used

* **Python:** The core programming language for the application.
* **OpenAI:** Used for generating listings and personalizing descriptions.
* **ChromaDB:** The vector database used for storing and searching embeddings.
* **Pandas:** For handling and displaying search results in a readable format.
* **Conda/venv:** For creating a dedicated virtual environment.

## Installation

### Prerequisites

* Python 3.10 or higher
* A Conda installation
* An OpenAI API Key
* Rust Compiler and Microsoft C++ Build Tools (required for building `tiktoken` and `chroma-hnswlib` from source on Windows)

### Setup Steps

1.  **Clone the repository:**
    ```bash
    git clone [Your GitHub Repository URL]
    cd [Your Repository Name]
    ```

2.  **Create and activate a Conda environment:**
    ```bash
    conda create --name homematch-env python=3.10
    conda activate homematch-env
    ```

3.  **Install dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your OpenAI API key:**
    Open each of the Python files (`generate_listings.py`, `vector_db_setup.py`, `homematch.py`) and replace the placeholder API key with your actual key.

    ```python
    # Example snippet to modify in each file
    openai.api_base = "[https://openai.vocareum.com/v1](https://openai.vocareum.com/v1)"
    openai.api_key = "YOUR_API_KEY_HERE"
    ```

## Usage

Follow these steps to run the "HomeMatch-AI" application in your terminal.

1.  **Generate a database of real estate listings:**
    This script will create a `listings.json` file containing 10+ synthetically generated property listings.
    ```bash
    python generate_listings.py
    ```

2.  **Populate the vector database:**
    This script will read the `listings.json` file, create embeddings for each listing, and store them in a ChromaDB collection.
    ```bash
    python vector_db_setup.py
    ```

3.  **Run the "HomeMatch-AI" agent:**
    This script will start the interactive session. The application will ask you a series of questions to understand your preferences, perform a semantic search, and provide personalized property descriptions.
    ```bash
    python homematch.py
    ```

## File Structure

* `generate_listings.py`: Script to generate synthetic real estate listings.
* `vector_db_setup.py`: Script to create the vector database and populate it with embeddings.
* `homematch.py`: The main application logic for user interaction, search, and personalization.
* `requirements.txt`: Lists all Python dependencies and their versions.
* `listings.json`: The file containing the generated listings (created by `generate_listings.py`).
* `README.md`: This project documentation file.
