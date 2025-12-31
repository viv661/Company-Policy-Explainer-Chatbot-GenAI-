# Company-Policy-Explainer-Chatbot-GenAI-

An AI-powered Company Policy Chatbot built using Retrieval-Augmented Generation (RAG).
This project allows users to ask natural language questions and get accurate answers from company policy documents (PDFs).

**Project Overview**

Organizations maintain multiple policy documents (leave policy, HR rules, code of conduct, etc.).
Answering repetitive employee queries manually increases HR workload.

This chatbot:

Reads company policy PDFs

Converts text into vector embeddings

Stores them in a vector database

Retrieves relevant information

Generates accurate answers using an LLM

**Project Structure**
chatbot/
├── data/                # PDF documents (policies)
│   └── .gitkeep
├── faiss_db/            # Vector database (FAISS)
│   └── .gitkeep
├── input.py             # PDF ingestion & vector creation
├── c.py                 # Chatbot logic / main execution file
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

**Technologies Used**

Python

LangChain

FAISS (Vector Database)

Hugging Face / OpenAI Embeddings

PDF Loader

RAG (Retrieval-Augmented Generation)

**How It Works (Simple Flow)**

PDF policy documents are loaded from the data/ folder

Text is split into smaller chunks

Chunks are converted into vector embeddings

Embeddings are stored in FAISS

User query is matched with relevant document chunks

LLM generates a contextual and accurate response

**How to Run the Project**
1) Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate

2) Install Dependencies
pip install -r requirements.txt

3) Add PDF Files

Place your policy PDFs inside the data/ folder.

4) Generate Vector Database
python input.py

5) Run the Chatbot
python c.py

**Important Notes**

venv/ folder is not uploaded to GitHub

.env file should never be uploaded (contains secrets)

Only source code and required folders are shared

**Use Cases**

HR Policy Assistant

Company Internal Chatbot

Employee Self-Service System

Internship / Academic Project

Beginner-friendly RAG implementation

**Learning Outcome**

Understanding of RAG architecture

Hands-on experience with LangChain

Vector database usage (FAISS)

Document-based QA systems
