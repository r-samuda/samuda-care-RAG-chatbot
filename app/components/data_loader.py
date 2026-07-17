import os
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import load_faiss_vector_store, create_vector_store
from app.config.config import DB_FAISS_PATH
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdf():
    try:
        logger.info("Making the vector store")
        documents = load_pdf_files()
        logger.info("Creating Text Chunks")
        text_chunks = create_text_chunks(documents)
        create_vector_store(text_chunks)
        logger.info("Created Vector Store")
    except Exception as e:
        message = CustomException("Failed to create vector store", e)
        logger.error(str(message))

if __name__ == "__main__":
    process_and_store_pdf()