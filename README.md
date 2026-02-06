# Debate

Multi-agent AI debate system powered by CrewAI. Agents collaborate to research and present arguments on topics.

## Tech Stack

- **Framework**: CrewAI 1.8.0
- **LLM**: OpenAI
- **Language**: Python 3.10+

## Key Concepts

- **Agents**: AI workers configured in `agents.yaml` with specific roles and expertise
- **Tasks**: Debate tasks defined in `tasks.yaml` executed by agents
- **Tools**: Custom tools in `tools/` for agents to research and analyze topics
- **Knowledge Base**: Static knowledge in `knowledge/` for context

## Project Structure

```
debate/
├── src/debate/
│   ├── main.py           # Entry point
│   ├── crew.py           # Crew orchestration
│   ├── config/
│   │   ├── agents.yaml   # Agent definitions
│   │   └── tasks.yaml    # Task definitions
│   └── tools/
│       └── custom_tool.py # Custom tools
├── knowledge/
│   └── user_preference.txt
└── pyproject.toml        # Dependencies
```

## Quick Start

1. **Install dependencies**:
   ```bash
   cd debate
   pip install -e .
   ```

2. **Run debate**:
   ```bash
   debate
   ```

3. **Available commands**:
   - `run_crew` - Execute crew
   - `train` - Training mode
   - `replay` - Replay previous runs
   - `test` - Run tests
