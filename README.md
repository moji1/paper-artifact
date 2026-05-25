# Software Requirements Ambiguity Resolution Using Large Language Models

This repository accompanies the paper:

> **Software Requirements Ambiguity Resolution Using Large Language Models**

It provides a unified **Chain-of-Thought (CoT)** framework for resolving four
types of ambiguity in natural-language software requirements — **anaphoric**,
**structural**, **vagueness**, and **scope** — using **Llama 3.1-8B-Instruct**,
with optional **Retrieval-Augmented Generation (RAG)**.

---

##  Highlights

- Unified prompt-engineering framework with type-specific CoT reasoning.
- Three prompting strategies: **zero-shot**, **one-shot**, **few-shot**.
- Optional **RAG** using `all-MiniLM-L6-v2` embeddings + ChromaDB.
- Evaluation with Exact Match, BLEU-1/2/3/4, Semantic Similarity, and
  manual judgements.
- 411 expert-annotated ambiguity instances spanning four ambiguity types.

---


##  Installation

### 1. Clone and create a Python environment

```bash
git clone <repo-url> requirements-ambiguity-llm
cd requirements-ambiguity-llm
python3 -m venv .venv
source .venv/bin/activate
pip install -r code/requirements.txt
```

### 2. Authenticate with Hugging Face (for Llama 3.1)

Llama 3.1 is a gated model. Request access on the
[model page](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct), then:

```bash
huggingface-cli login
```

### 3. (One-time) download NLTK data used by BLEU smoothing

```bash
python -c "import nltk; nltk.download('punkt')"
```

---

##  Hardware requirements

- NVIDIA GPU with **≥ 40 GB VRAM** (e.g. A100-40GB) for Llama 3.1-8B in
  `bfloat16`.
- Runs on CPU too, but will be very slow.
- ~5 GB disk space for model weights.

---


##  Model configuration

These defaults match §Experimental Setup of the paper:

| Hyperparameter         | Value                                |
|------------------------|--------------------------------------|
| Model                  | `meta-llama/Llama-3.1-8B-Instruct`   |
| Precision              | `bfloat16`                           |
| Temperature            | 0.1                                  |
| Top-p                  | 0.9                                  |
| Max new tokens         | 512                                  |
| Repetition penalty     | 1.1                                  |
| Max input (zero-shot)  | 2048 tokens                          |
| Max input (one-shot)   | 2560 tokens                          |
| Max input (few-shot)   | 3584 tokens                          |
| Embedding model        | `all-MiniLM-L6-v2`                   |
| RAG index              | ChromaDB (cosine, HNSW)              |
| Retrieved chunks       | 3 (≤ 200 tokens each)                |
| Random seed            | 42                                   |

---

##  Evaluation metrics

Automatic metrics computed per instance:

- **Exact Match** (case-insensitive, whitespace-normalised)
- **BLEU-1 / BLEU-2 / BLEU-3 / BLEU-4** (NLTK, `method1` smoothing)
- **Semantic Similarity** (cosine of `all-MiniLM-L6-v2` embeddings)

---

##  License

- **Code** — [MIT](LICENSE)
- **Data** — [CC BY 4.0](LICENSE-DATA) (with attribution to the PURE corpus
  and the multi-label ambiguity-detection dataset cited in the paper)

---

