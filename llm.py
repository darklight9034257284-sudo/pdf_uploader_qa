from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os
import streamlit as st
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

st.title("PDF to Chroma DB Vector Store")

# 2. Render File Uploader 
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing PDF and generating embeddings..."):
        
        # 3. Read and Extract Text from PDF Bytes
        pdf_reader = PdfReader(uploaded_file)
        raw_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"
        
        # 4. Wrap text into a LangChain Document format
        initial_doc = Document(page_content=raw_text, metadata={"source": uploaded_file.name})
        
        # 5. Split Text into manageable chunks (prevents losing context)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        final_chunks = text_splitter.split_documents([initial_doc])
        
        # 6. Initialize Embeddings and Connect to Chroma
        embeddings= HuggingFaceEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2")

        
        # In-memory database initialization
        vector_store = Chroma.from_documents(
            documents=final_chunks,
            embedding=embeddings
        )
        
        st.success(f"Successfully processed {len(final_chunks)} text chunks from '{uploaded_file.name}' into Chroma DB!")
        
        # 7. Quick testing input interface
        query = st.chat_input("Ask a question about your PDF:")
        if query:
            results = vector_store.similarity_search(query, k=2)
            st.write("### Top Relevant Match:")
            st.write(results[0].page_content)
#./.venv/bin/streamlit run chat_app/llm.py