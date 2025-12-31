import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

# Set page config
st.set_page_config(page_title="Chatbot", page_icon="chatbot", layout="wide")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for status
with st.sidebar:
    st.title("Status")
    status_placeholder = st.empty()
    
    # Initialize components
    with st.spinner("Loading components..."):
        # 1. Load environment
        load_dotenv()
        status_placeholder.text("Environment loaded")
        
        # 2. Load embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        status_placeholder.text("Embeddings loaded")
        
        # 3. Load FAISS
        vectorstore = FAISS.load_local(
            "faiss_db",
            embeddings,
            allow_dangerous_deserialization=True
        )
        retriever = vectorstore.as_retriever()
        status_placeholder.text("FAISS loaded")
        
        # 4. Load LLM
        pipe = pipeline(
            task="text2text-generation",
            model="google/flan-t5-base",
            max_new_tokens=256
        )
        llm = HuggingFacePipeline(pipeline=pipe)
        status_placeholder.text("LLM ready")
        
        # 5. Set up RAG chain
        prompt = ChatPromptTemplate.from_template(
            """Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know". 

Context:
{context}

Question:
{question}
"""
        )
        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
        )
        status_placeholder.text("RAG chain ready")

# Main chat interface
st.title(" Chatbot")
st.write("Ask me anything about your documents!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = rag_chain.invoke(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})