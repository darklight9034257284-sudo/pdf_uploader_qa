# PDF to Chroma DB Vector Store

A Streamlit-based web application that allows users to upload a PDF file, processes its content into text chunks, generates vector embeddings using a Hugging Face model, and stores them in an in-memory Chroma DB for quick similarity-based semantic search.

---

## 🚀 Features

*   **PDF Uploading:** Seamlessly drag and drop or upload any `.pdf` document.
*   **Smart Text Chunking:** Extracts text and breaks it down using a `RecursiveCharacterTextSplitter` (1000 chunk size, 200 chunk overlap) to preserve context.
*   **Local Embeddings:** Generates vector representations using the open-source `sentence-transformers/all-MiniLM-L6-v2` model via Hugging Face.
*   **Vector Storage:** Initializes an in-memory `Chroma` database on the fly to store document vectors.
*   **Semantic Search:** Includes an interactive chat input field to query the PDF and instantly retrieve the top 2 most relevant context chunks.

---

## 🛠️ Tech Stack

*   **Frontend & UI:** [Streamlit](https://streamlit.io/)
*   **LLM Orchestration:** [LangChain](https://www.langchain.com/) (`langchain-huggingface`, `langchain-core`, `langchain-community`)
*   **Vector Database:** [Chroma DB](https://www.trychroma.com/)
*   **Text Extraction:** [PyPDF](https://pypdf.readthedocs.io/)

---

## ⚙️ Getting Started

### Prerequisites

Ensure you have Python 3.9+ installed on your machine.

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd pdf_uploader_qa
