# Mini Q&A Chatbot Assessment

This project is a simple, intelligent Q&A chatbot built for the Algorithm Aliens technical assessment. The chatbot is designed to answer a predefined set of questions and excels at understanding variations in user phrasing through the use of semantic similarity.

## ✨ Key Features
- Answers a knowledge base of 15 predefined questions.
- **Handles phrasing variations:** Understands that "What is the price?" and "How much does it cost?" have the same meaning.
- **Graceful Fallback:** Responds with a polite "I don't know" message for irrelevant or out-of-scope questions.
- **Interactive UI:** A clean and simple web interface built with Streamlit for easy interaction.

## 🛠️ Tech Stack
- **Python**
- **Hugging Face `sentence-transformers`**: For generating state-of-the-art text embeddings.
- **Scikit-learn**: For calculating cosine similarity.
- **Streamlit**: For building the interactive web UI.

## 📁 Project Structure
The project is organized into logical modules for clarity and maintainability.

project/
│
├── app.py             # Main Streamlit application file for the UI
├── chatbot.py         # Contains the core MiniChatbot class and its logic
├── knowledge_base.py  # Stores the predefined list of questions and answers
└── requirements.txt   # A list of all Python dependencies for the project

## 🚀 Setup and Installation

Follow these steps to get the chatbot running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-link>
    cd <your-project-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
##🧠 My Approach
The core requirement of this task was to handle variations in user questions. To achieve this, I chose a Semantic Search approach over simple keyword matching.

Knowledge Base: I began by defining the 15 required questions and answers in knowledge_base.py.

Text Embeddings: I used the all-MiniLM-L6-v2 model from Hugging Face's sentence-transformers library. This powerful model converts each question in the knowledge base into a 384-dimensional numerical vector (an "embedding"). These embeddings capture the semantic meaning of the text. This is a one-time process performed when the chatbot initializes.

Real-time Query Processing: When a user submits a question, it is also converted into an embedding using the same model.

Cosine Similarity: The chatbot then calculates the cosine similarity between the user's query vector and all the pre-calculated vectors in the knowledge base. This provides a score of how "semantically close" the user's question is to each known question.

Thresholding for Relevance: The question with the highest similarity score is chosen as the best match. However, to handle completely unrelated questions, I implemented a threshold (e.g., 0.5). If the top score is below this threshold, the bot concludes the question is out of scope and returns a default "I don't know" response.

This method is highly effective and robust, ensuring the chatbot provides accurate answers even when users phrase their questions in unexpected ways.

## 🚀 Setup and Installation

Follow these steps to get the chatbot running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-link>
    cd <your-project-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ How to Run
To start the chatbot, run the Streamlit application from your terminal:
```bash
streamlit run app.py
This will open a new tab in your web browser at http://localhost:8501.







