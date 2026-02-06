# Agentic AI Projects - Monorepo

## 🔍 Overview

A hands-on monorepo of Agentic AI projects, each on a separate branch. Showcases the evolution of modern AI systems — from basic LLM tool usage to advanced multi-agent, graph-based, production-grade workflows.

**Explores:**
- LLM agents and reasoning patterns (ReAct, Reflection, Reflexion)
- Retrieval-Augmented Generation (RAG)
- Graph-based agent orchestration
- Multi-agent collaboration
- Real-world integrations (web search, email, browsers, UIs)

## 🧠 Tech Stack & Concepts

**Languages & Runtime**
- Python 3.10–3.12+

**LLMs & Providers**
- Azure OpenAI, OpenAI, Google Generative AI (Gemini)

**Frameworks**
- LangChain, LangGraph, OpenAI Agents SDK, CrewAI

**Agent Patterns**
- ReAct (Reason → Act → Observe)
- Tool/Function Calling
- Reflection & Self-Critique Loops
- Reflexion (Research-grade iteration)
- Agentic RAG
- Multi-Agent Workflows

**Retrieval & Search**
- RAG (Retrieval-Augmented Generation)
- Chroma / Pinecone (Vector Databases)
- Tavily Search (Web Search & Crawling)

**UIs & Interfaces**
- Gradio, Streamlit, Rich (Terminal UI)

**Integrations**
- Web Browsing (Playwright)
- Email Automation (SendGrid)
- Notifications (Pushover)
- Async Workflows (asyncio)

**Observability & Quality**
- LangSmith (Tracing & Monitoring)
- Structured Outputs (Pydantic)
- Guardrails & Validation

## Projects

All projects live on their own branches under `projects/`. Ordered from beginner to advanced.

### 🟢 Beginner Level

| Project | Description | Branch |
|---------|-------------|--------|
| Hello World | Basic LLM calls, prompts, and simple chains | `projects/hello-world` |
| Sequential Chain | Simple sequential LLM operations | `projects/seq-chain-using-openaiClient` |
| AI-Powered Todo Planner | Task planner using LLM function calling loops | `projects/plan-act-loop-usingOpenaiClient` |
| Search Agent | Lightweight web search agent with source URLs | `projects/search-agent` |
| RAG Gist | Basic RAG pipeline with embeddings and vector search | `projects/rag-gist` |
| ReAct Agent with Tool Calling | Foundational ReAct agent with step-by-step reasoning | `projects/ReAct-agent-with_tool_calling` |

### 🟡 Intermediate Level

| Project | Description | Branch |
|---------|-------------|--------|
| ReAct Search Agent | ReAct agent with real-time web search | `projects/ReAct-search-agent` |
| Portfolio Chatbot | Personal AI chatbot with Gradio UI | `projects/alter-ego-gradio-chatbot` |
| Documentation Helper | Streamlit RAG app for documentation Q&A | `projects/documentation-helper` |
| Reflection Agent | Self-critique and refinement loops | `projects/reflection-agent` |
| Debate System | Multi-agent debate using CrewAI | `projects/crewai-debate-system` |

### 🔵 Advanced Level

| Project | Description | Branch |
|---------|-------------|--------|
| ReAct Function Calling | Deterministic ReAct with LangGraph state graphs | `projects/react-function-calling` |
| Agentic RAG | Agent-driven document retrieval and web search | `projects/agentic-rag` |
| Deep Research Agent | Multi-agent research with parallel data gathering | `projects/deep-research-OpenaiSDK` |
| Reflexion Agent | Self-critique with web search and citations | `projects/reflexion-agent` |

### 🔴 Expert / Production-Grade

| Project | Description | Branch |
|---------|-------------|--------|
| Sidekick | Full-fledged co-worker with Playwright, tools, notifications | `projects/agent-withCheckpoint-usingLangGraph` |
| Autonomous SDR | Production multi-agent sales system with guardrails | `projects/autonomous-SDR-usingOpenaiSDK` |

## Learning Resources

This monorepo was created while learning from:
- [Edin Marco's LangChain Course on Udemy](https://www.udemy.com/course/langchain/learn)
- [Ed Donner's Agentic AI track](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/learn)

## Getting Started

To explore a specific project, switch to its branch:

```bash
git checkout projects/project-name
```

Each project contains its own README with specific setup and usage instructions.

---

**Note:** This is a learning monorepo where each branch represents a different experiment or project implementation.