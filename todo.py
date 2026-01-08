from rich.console import Console
import json


def show(text):
    try:
        Console().print(text)
    except Exception:
        print(text)


todos = []
completed = []


def get_todo_report() -> str:
    result = ""
    for index, todo in enumerate(todos):
        if completed[index]:
            result += f"Todo #{index + 1}: [green][strike]{todo}[/strike][/green]\n"
        else:
            result += f"Todo #{index + 1}: {todo}\n"
    show(result)
    return result


def create_todos(descriptions: list[str]) -> str:
    todos.extend(descriptions)
    completed.extend([False] * len(descriptions))
    return get_todo_report()


def mark_complete(index: int, completion_notes: str) -> str:
    if 1 <= index <= len(todos):
        completed[index - 1] = True
    else:
        return "No todo at this index."
    Console().print(completion_notes)
    return get_todo_report()


create_todos_json = {
    "name": "create_todos",
    "description": "Add new todos from a list of descriptions and return the full list",
    "parameters": {
        "type": "object",
        "properties": {
            "descriptions": {
                "type": "array",
                "items": {"type": "string"},
                "title": "Descriptions",
            }
        },
        "required": ["descriptions"],
        "additionalProperties": False,
    },
}

mark_complete_json = {
    "name": "mark_complete",
    "description": "Mark complete the todo at the given position (starting from 1) and return the full list",
    "parameters": {
        "properties": {
            "index": {
                "description": "The 1-based index of the todo to mark as complete",
                "title": "Index",
                "type": "integer",
            },
            "completion_notes": {
                "description": "Notes about how you completed the todo in rich console markup",
                "title": "Completion Notes",
                "type": "string",
            },
        },
        "required": ["index", "completion_notes"],
        "type": "object",
        "additionalProperties": False,
    },
}


TOOLS = [
    {"type": "function", "function": create_todos_json},
    {"type": "function", "function": mark_complete_json},
]


def handle_tool_calls(tool_calls):
    tool_mapping = {
        "create_todos": create_todos,
        "mark_complete": mark_complete,
    }
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        tool = tool_mapping.get(tool_name)
        if not tool:
            raise ValueError(f"Unknown tool: {tool_name}")
        result = tool(**arguments) if tool else {}

        results.append(
            {
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id,
            }
        )
    return results
