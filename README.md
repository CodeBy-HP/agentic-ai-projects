# Portfolio Chat Bot

An AI-powered personal portfolio chatbot that answers questions about Harsh Patel's career, background, skills, and experience. Built with Azure OpenAI and Gradio.

# User Interface

<img width="1886" height="904" alt="Screenshot 2026-01-08 001034" src="https://github.com/user-attachments/assets/22688a04-0142-4b55-bd61-75713492d61c" />

## Description

This project creates an interactive chatbot that represents a professional on their website. Visitors can ask questions about the profile, and the AI responds in character using context from the person's LinkedIn profile and background summary. The system records user interest and unknown questions for follow-up.

## Tech Stack

- **Python 3.12+** - Core language
- **Gradio** - Web UI framework
- **Azure OpenAI** - AI/LLM backend
- **PyPDF** - PDF parsing for LinkedIn profiles
- **Requests** - HTTP client for notifications
- **python-dotenv** - Environment management

## Key Concepts

- **Conversational AI** - Uses OpenAI function calling to perform actions (record user details, log unanswered questions)
- **Context Injection** - Combines LinkedIn profile and summary for accurate responses
- **Tool Calling** - AI invokes functions to record user interest and track questions
- **Notification System** - Sends alerts via Pushover API

## Project Structure

```
├── main.py              # Core chat logic and AI setup
├── tools.py             # Tool definitions for AI actions
├── pyproject.toml       # Dependencies
├── README.md            # This file
└── static/
    ├── profile.pdf      # LinkedIn profile
    └── summary.txt      # Background summary
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables** (create `.env`):
   ```
   AZURE_OPENAI_DEPLOYMENT=<your-deployment>
   AZURE_OPENAI_API_KEY=<your-api-key>
   PUSHOVER_USER=<user-id>
   PUSHOVER_TOKEN=<token>
   ```

3. **Add profile files:**
   - Place LinkedIn profile PDF at `static/profile.pdf`
   - Add background summary at `static/summary.txt`

4. **Run the app:**
   ```bash
   python main.py
   ```

The chatbot will open in a Gradio interface. Start chatting!

