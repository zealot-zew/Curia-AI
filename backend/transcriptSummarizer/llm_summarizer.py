"""
Module: llm_summarizer
Description: Wraps the call to the local Ollama LLaMA 3.1 model to extract
structured meeting data (decisions and action items) from a transcript.
"""

import subprocess
import sys
import textwrap

def summarize_with_llama(transcript):
    """Call Ollama's LLaMA 3.1 model to extract structured JSON from a transcript.

    Args:
        transcript (str): Cleaned transcript text.

    Returns:
        str: Raw model output (expected to contain a JSON object).

    Exits:
        Exits the process with code 1 if the model cannot be run.
    """
    prompt = textwrap.dedent(f"""
    You are an expert meeting assistant. Your task is to extract key decisions and action items from a meeting transcript.
    The output MUST be a valid JSON object.

    ### Instructions ###
    1. **Decisions**: Identify all key decisions made.
    2. **Action Items**: Identify all tasks that need to be completed. For each task, extract:
        - `Summary`: A concise description of the task.
        - `Assignee`: The person responsible for the task.
        - `Priority`: Assign a priority (Highest,High ,Medium ,Low or Lowest).
        - `Due date`: The due date for the task, if mentioned. If not, use "N/A".The duedate must be of the format "yyyy-MM-dd".

    ### Example JSON Output ###
    {{
      "decisions": [
        "Decision 1: The team will switch to a new project management tool.",
        "Decision 2: The budget for Q3 marketing campaigns will be increased by 15%."
      ],
      "action_items": [
        {{
          "Summary": "Research and evaluate new project management tools.",
          "Assignee": "Sarah",
          "Priority": "Highest",
          "Due date": "2025-09-01"
        }},
        {{
          "Summary": "Update the Q3 marketing budget proposal.",
          "Assignee": "Alex",
          "Priority": "Medium",
          "Due date": "N/A"
        }}
      ]
    }}

    ### Transcript ###
    {transcript}
    """)

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.1", prompt],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Error running Ollama: {result.stderr}")
            sys.exit(1)
        return result.stdout.strip()
    except FileNotFoundError:
        print("Error: Ollama is not installed or not in PATH.")
        sys.exit(1)


