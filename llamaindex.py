from pathlib import Path

from llama_index.core import VectorStoreIndex
from llama_index.readers.file import PDFReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Load PDF (path relative to this script so cwd does not matter)
_pdf = Path(__file__).resolve().parent / "data" / "sample_report.pdf"
if not _pdf.is_file():
    raise FileNotFoundError(f"PDF not found: {_pdf}")

loader = PDFReader()
documents = loader.load_data(file=str(_pdf))

# Local LLM + embeddings
llm = Ollama(model="llama3")
embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Create index
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)

# Query engine
query_engine = index.as_query_engine(llm=llm)

# Ask questions
response = query_engine.query("Summarize this document")
print(response)