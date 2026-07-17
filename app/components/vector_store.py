from langchain_community.vectorstores import FAISS
import os

from app.components.embeddings import get_embedding_model

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_faiss_vector_store():
    try:
        logger.info(f"Loading FAISS vector store from path: {DB_FAISS_PATH}")
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info(f"FAISS vector store found at path: {DB_FAISS_PATH}")
            vector_store = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
            logger.info("FAISS vector store loaded successfully.")
        else:
            logger.warning("no vector store found")
        return vector_store
    except Exception as e:
        logger.error(f"Error occurred while loading FAISS vector store: {str(e)}")
        raise CustomException(f"Error occurred while loading FAISS vector store: {str(e)}")
    
def create_vector_store(chunks):
    try:
        if not chunks:
            raise CustomException("No text chunks provided for vector store creation.")
        
        logger.info("Creating FAISS vector store from text chunks.")
        embedding_model = get_embedding_model()
        vector_store = FAISS.from_documents(chunks, embedding_model)
        logger.info("FAISS vector store created successfully.")

        vector_store.save_local(DB_FAISS_PATH)

        logger.info(f"FAISS vector store saved locally at path: {DB_FAISS_PATH}")
        return vector_store
    
    except Exception as e:
        logger.error(f"Error occurred while creating FAISS vector store: {str(e)}")
        raise CustomException(f"Error occurred while creating FAISS vector store: {str(e)}")
