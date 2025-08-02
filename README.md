# 🏡 HomeMatch-AI: Your Personalized Real Estate Agent 🤖

### An AI-powered tool for a smarter home search experience. ✨

---

## 🚀 Project Overview

Tired of scrolling through generic real estate listings? **HomeMatch-AI** is a groundbreaking application that brings the power of generative AI and vector databases to your fingertips. 

This project simulates a highly personalized real estate agent. It doesn't just match keywords; it understands the *vibe* of your dream home. First, it generates a diverse database of realistic property listings. Then, when you describe your perfect home in plain English, it finds the most semantically relevant properties and, with a touch of AI magic, rewrites each listing to highlight the features that matter most to **you**. 💖

## 🌟 Key Features

* **✍️ Generative Listing Creation:** Automatically crafts diverse and realistic property listings using the power of OpenAI's GPT-3.5.
* **🧠 Intelligent Semantic Search:** Moves beyond simple filters by using a ChromaDB vector database to find properties that truly match the *meaning* of your preferences.
* **🗣️ Natural Language Processing:** Seamlessly takes your natural language preferences and turns them into actionable search queries.
* **✨ Personalized Descriptions:** Rewrites listings on-the-fly to emphasize the unique aspects of each property that align with your specific taste.

---

## 🛠️ Tech Stack

* **Python:** The core engine of the application. 🐍
* **OpenAI:** The brain behind the content generation and personalization. 🧠
* **ChromaDB:** The memory of the agent, providing fast and efficient vector search. 💾
* **Pandas:** For handling and presenting data results with elegance. 📊

---

## ⚙️ Get Started

### 📦 Prerequisites

* A Conda installation (recommended for environment management).
* An OpenAI API Key.
* Make sure you have the Rust compiler and Microsoft C++ Build Tools installed (essential for building some dependencies on Windows).

### 🚀 Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rushiraj070/Personal_Real_Estate_Agent.git](https://github.com/rushiraj070/Personal_Real_Estate_Agent.git)
    cd Personal_Real_Estate_Agent
    ```

2.  **Create and activate your Conda environment:**
    ```bash
    conda create --name homematch-env python=3.10
    conda activate homematch-env
    ```

3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your OpenAI API Key:**
    Open the three Python files (`generate_listings.py`, `vector_db_setup.py`, `homematch.py`) and replace the placeholder API key with your actual key and API base.
    ```python
    # Example snippet to modify
    openai.api_base = "[https://openai.vocareum.com/v1](https://openai.vocareum.com/v1)"
    openai.api_key = "voc-00000000000000000000000000000000abcd.12345678"
    ```

---

## ▶️ How to Run

Follow these steps in your terminal to bring your "HomeMatch-AI" agent to life!

1.  **Generate a database of fictional real estate listings:**
    ```bash
    python generate_listings.py
    ```
    _This will create a `listings.json` file in your project directory._

2.  **Populate the vector database:**
    ```bash
    python vector_db_setup.py
    ```
    _This step will read the `listings.json` and create the `chroma.sqlite3` database file._

3.  **Launch the interactive agent:**
    ```bash
    python homematch.py
    ```
    _The application will now ask you a series of questions to find your dream home!_

---

## 📁 Project Structure
Here is a more attractive and engaging version of your README.md file, complete with relevant emojis and improved formatting. You can copy and paste this directly into your repository.

Markdown

# 🏡 HomeMatch-AI: Your Personalized Real Estate Agent 🤖

### An AI-powered tool for a smarter home search experience. ✨

---

## 🚀 Project Overview

Tired of scrolling through generic real estate listings? **HomeMatch-AI** is a groundbreaking application that brings the power of generative AI and vector databases to your fingertips. 

This project simulates a highly personalized real estate agent. It doesn't just match keywords; it understands the *vibe* of your dream home. First, it generates a diverse database of realistic property listings. Then, when you describe your perfect home in plain English, it finds the most semantically relevant properties and, with a touch of AI magic, rewrites each listing to highlight the features that matter most to **you**. 💖

## 🌟 Key Features

* **✍️ Generative Listing Creation:** Automatically crafts diverse and realistic property listings using the power of OpenAI's GPT-3.5.
* **🧠 Intelligent Semantic Search:** Moves beyond simple filters by using a ChromaDB vector database to find properties that truly match the *meaning* of your preferences.
* **🗣️ Natural Language Processing:** Seamlessly takes your natural language preferences and turns them into actionable search queries.
* **✨ Personalized Descriptions:** Rewrites listings on-the-fly to emphasize the unique aspects of each property that align with your specific taste.

---

## 🛠️ Tech Stack

* **Python:** The core engine of the application. 🐍
* **OpenAI:** The brain behind the content generation and personalization. 🧠
* **ChromaDB:** The memory of the agent, providing fast and efficient vector search. 💾
* **Pandas:** For handling and presenting data results with elegance. 📊

---

## ⚙️ Get Started

### 📦 Prerequisites

* A Conda installation (recommended for environment management).
* An OpenAI API Key.
* Make sure you have the Rust compiler and Microsoft C++ Build Tools installed (essential for building some dependencies on Windows).

### 🚀 Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rushiraj070/Personal_Real_Estate_Agent.git](https://github.com/rushiraj070/Personal_Real_Estate_Agent.git)
    cd Personal_Real_Estate_Agent
    ```

2.  **Create and activate your Conda environment:**
    ```bash
    conda create --name homematch-env python=3.10
    conda activate homematch-env
    ```

3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your OpenAI API Key:**
    Open the three Python files (`generate_listings.py`, `vector_db_setup.py`, `homematch.py`) and replace the placeholder API key with your actual key and API base.
    ```python
    # Example snippet to modify
    openai.api_base = "[https://openai.vocareum.com/v1](https://openai.vocareum.com/v1)"
    openai.api_key = "voc-00000000000000000000000000000000abcd.12345678"
    ```

---

## ▶️ How to Run

Follow these steps in your terminal to bring your "HomeMatch-AI" agent to life!

1.  **Generate a database of fictional real estate listings:**
    ```bash
    python generate_listings.py
    ```
    _This will create a `listings.json` file in your project directory._

2.  **Populate the vector database:**
    ```bash
    python vector_db_setup.py
    ```
    _This step will read the `listings.json` and create the `chroma.sqlite3` database file._

3.  **Launch the interactive agent:**
    ```bash
    python homematch.py
    ```
    _The application will now ask you a series of questions to find your dream home!_

---

## 📁 Project Structure

├── .git/
├── generate_listings.py
├── homematch.py
├── listings.json
├── requirements.txt
├── vector_db_setup.py
└── README.md
---

## 🔮 Future Enhancements

* **Image Integration:** Add a feature to generate images of the houses and neighborhoods.
* **Web Interface:** Build a simple web front-end using Flask or Streamlit for a more user-friendly experience.
* **Advanced Preference Parsing:** Use a more sophisticated LLM chain to extract structured data from user preferences before performing the search.

Happy coding! 🎉
