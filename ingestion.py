import asyncio
import os
import ssl
from typing import List

import certifi
from dotenv import load_dotenv
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import AzureOpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_tavily import TavilyCrawl
from langchain_chroma import Chroma

from logger import (
    Colors,
    log_error,
    log_header,
    log_info,
    log_success,
    log_warning,
)

# -------------------------------------------------
# Environment & SSL Hardening
# -------------------------------------------------
load_dotenv()

ssl_context = ssl.create_default_context(cafile=certifi.where())
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

# -------------------------------------------------
# Embeddings & VectorStore
# -------------------------------------------------
embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBED_DEPLOYMENT"),
    show_progress_bar=False,
    chunk_size=50,
    retry_min_seconds=10,
)

vectorstore = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
# vectorstore = PineconeVectorStore(
#     index_name=os.getenv("INDEX_NAME"),
#     embedding=embeddings,
# )

tavily_crawl = TavilyCrawl()

# -------------------------------------------------
# Async Indexing Logic
# -------------------------------------------------
async def index_documents_async(docs: List[Document], batch_size: int = 200):
    log_header("VECTOR STORAGE PHASE")
    log_info(f"📚 Preparing to index {len(docs)} chunks", Colors.DARKCYAN)

    batches = [docs[i:i + batch_size] for i in range(0, len(docs), batch_size)]
    log_info(f"📦 Split into {len(batches)} batches")

    async def add_batch(batch: List[Document], batch_num: int):
        try:
            await vectorstore.aadd_documents(batch)
            log_success(f"Batch {batch_num}/{len(batches)} indexed ({len(batch)} docs)")
            return True
        except Exception as e:
            log_error(f"Batch {batch_num} failed — {e}")
            return False

    results = await asyncio.gather(
        *(add_batch(batch, i + 1) for i, batch in enumerate(batches))
    )

    ok = sum(1 for r in results if r)
    if ok == len(batches):
        log_success("All batches indexed successfully")
    else:
        log_warning(f"{ok}/{len(batches)} batches indexed")


# -------------------------------------------------
# Main Pipeline
# -------------------------------------------------
async def main():
    log_header("DOCUMENTATION INGESTION PIPELINE")

    log_info("🗺️ Crawling LangChain docs", Colors.PURPLE)

    crawl_result = tavily_crawl.invoke({
        "url": "https://python.langchain.com/",
        "max_depth": 5,
        "extract_depth": "advanced"
    })

    docs = [
        Document(
            page_content=r["raw_content"],
            metadata={"source": r["url"]},
        )
        for r in crawl_result["results"]
    ]

    log_success(f"Crawled {len(docs)} pages")

    # -------- Chunking --------
    log_header("DOCUMENT CHUNKING PHASE")
    splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    log_success(f"Created {len(chunks)} chunks")

    # -------- Indexing --------
    await index_documents_async(chunks, batch_size=200)

    log_header("PIPELINE COMPLETE")
    log_success("🎉 Documentation ingestion pipeline finished")
    log_info(f"• Documents: {len(docs)}")
    log_info(f"• Chunks: {len(chunks)}")


# -------------------------------------------------
if __name__ == "__main__":
    asyncio.run(main())
