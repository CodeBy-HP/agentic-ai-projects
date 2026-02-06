# AI-Powered Todo Planner

<img width="1407" height="462" alt="Screenshot 2026-01-08 113430" src="https://github.com/user-attachments/assets/2a88574c-6791-4224-90bd-1dadb6504be0" />

## Description

An AI-powered problem solver that uses large language models to break down complex problems into actionable steps. The AI creates a todo list, executes each step, and provides the final solution using intelligent planning and execution.

## Tech Stack

- **Python 3.12+**
- **Azure OpenAI** (GPT-4o-mini)
- **Rich** - Terminal output formatting
- **python-dotenv** - Environment variable management

## Key Concepts

- **Function Calling**: AI uses defined tools (`create_todos`, `mark_complete`) to manage tasks
- **Agentic Loop**: The AI iteratively creates plans and marks items complete
- **Rich Console Markup**: Formatted terminal output with styling and colors

## Project Structure

```
├── main.py           # Entry point and agent loop
├── todo.py           # Todo management and tool definitions
├── pyproject.toml    # Project dependencies
└── README.md         # This file
```

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -e .
   ```

2. **Set up environment** - Create a `.env` file with:
   ```
   AZURE_OPENAI_DEPLOYMENT=<your-deployment-name>
   AZURE_OPENAI_ENDPOINT=<your-endpoint>
   AZURE_OPENAI_API_KEY=<your-api-key>
   ```

3. **Run the project**:
   ```bash
   python main.py
   ```
