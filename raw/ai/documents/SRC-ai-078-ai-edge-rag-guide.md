---
source_id: "SRC-ai-078"
title: "AI Edge RAG guide"
source_type: "product_documentation"
publisher: "Google AI Edge"
source_date: "2026-05-28"
url: "https://developers.google.com/edge/mediapipe/solutions/genai/rag"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-14T02:12:11+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-ai-078
---
# AI Edge RAG guide

The AI Edge RAG SDK provides the fundamental components to construct a Retrieval Augmented Generation (RAG) pipeline with the LLM Inference API. A RAG pipeline provides LLMs with access to user-provided data, which can include updated, sensitive, or domain-specific information. With the added information retrieval capabilities from RAG, LLMs can generate more accurate and context-aware responses for specific use cases.

The AI Edge RAG SDK is available for Android and can be run completely on-device. Start using the SDK by following the [Android guide](https://developers.google.com/edge/mediapipe/solutions/genai/rag/android), which walks you through a basic implementation of a sample application using RAG.

## RAG Pipeline

Setting up a RAG pipeline with the AI Edge RAG SDK contains the following key steps:

1. **Import data**: Provide the textual data that the LLM will use when generating output.
2. **Split and index the data**: Break the data into small chunks for indexing in a database.
3. **Generate embeddings**: Use an embedder to vectorize the chunks to store in a vector database.
4. **Retrieve information**: Define how relevant information is identified and retrieved to address user prompts. For a given prompt, the retrieval component searches through the vector database to identify relevant information.
5. **Generate text with LLM**: Use a large language model to generate output text based on the information retrieved from the vector database.

## Key Modules

The AI Edge RAG SDK provides the following key modules and APIs for the RAG pipeline:

- **Language Models**: The LLM models with open-prompt API, either local (on-device) or server-based. The API is based on the [LanguageModel](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/models/LanguageModel.java) interface.
- **Text Embedding Models**: Convert structured and unstructured text into embedding vectors for semantic search. The API is based on the [Embedder](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/models/Embedder.java) interface.
- **Vector Stores**: The vector store holds the embeddings and metadata derived from data chunks. It can be queried to get similar chunks or exact matches. The API is based on the [VectorStore](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/memory/VectorStore.java) interface.
- **Semantic Memory**: Serve as a semantic retriever for retrieving top-k relevant chunks given a query. The API is based on the [SemanticMemory](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/memory/SemanticMemory.java) interface.
- **Text Chunking**: Splits user data into smaller pieces to facilitate indexing. The API is based on the [TextChunker](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/chunking/TextChunker.java) interface.

The SDK provides chains, which combines several RAG components in a single pipeline. You can use chains to orchestrate retrieval and query models. The API is based on the [Chain](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/chains/Chain.java) interface. To get started, try the [Retrieval and Inference chain](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/chains/RetrievalAndInferenceChain.java) or [Retrieval chain](https://github.com/google-ai-edge/ai-edge-apis/blob/main/local_agents/rag/java/com/google/ai/edge/localagents/rag/chains/RetrievalChain.java).
