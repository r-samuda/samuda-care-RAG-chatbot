import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path '{DATA_PATH}' does not exist.")
        
        logger.info(f"Loading PDF files from directory: {DATA_PATH}")

        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            logger.warning("No PDF documents found in the specified directory.")
        else:
            logger.info(f"Loaded {len(documents)} PDF documents.")

        return documents
    except Exception as e:
        logger.error(f"Error occurred while loading PDF files: {str(e)}")
        raise CustomException(f"Error occurred while loading PDF files: {str(e)}")
    
def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents provided for text chunking.")

        logger.info("Creating text chunks from loaded documents.")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        chunks = text_splitter.split_documents(documents)

        if not chunks:
            logger.warning("No text chunks were created from the documents.")
        else:
            logger.info(f"Created {len(chunks)} text chunks from the documents.")

        return chunks
    except Exception as e:
        logger.error(f"Error occurred while creating text chunks: {str(e)}")
        raise CustomException(f"Error occurred while creating text chunks: {str(e)}")