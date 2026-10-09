# llama-eurlex

Early prototype (September 2023) exploring retrieval-augmented generation (RAG) over EU legislation.

## What is here

- `test.py`: queries the [EUR-Lex SOAP web service](https://eur-lex.europa.eu/content/help/data-reuse/webservice.html) with an expert query, then builds a LlamaIndex vector index over local documents in `data/` and runs a sample question. It needs EUR-Lex web-service credentials in a local `config.py`, which is not included.
- `test2.py`: runs LlamaIndex with a local Hugging Face model (`facebook/opt-iml-1.3b`) instead of a hosted API. It is based on a public LlamaIndex tutorial example.

## Status

Experimental scripts, not maintained. They target the 2023 `llama_index` API (before v0.10), which has since changed, so they will not run unmodified against current releases.
