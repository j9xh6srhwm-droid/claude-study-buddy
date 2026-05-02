# Claude Study Buddy

A CLI tutor for studying Anthropic's Claude and generative AI concepts.
Built in Python using the Anthropic SDK with multi-turn conversation memory
and four distinct tutor modes.

## Modes

| Command      | Behaviour                                      |
|-------------|------------------------------------------------|
| `/explain`  | Explanation + analogy + follow-up question     |
| `/quiz`     | Multiple-choice questions with score tracking  |
| `/summary`  | Structured recap of the full session           |
| `/eli5`  | Explains like to a five year old           |


Usage: `/explain context window` or just type freely (defaults to explain).

## Setup

1. Clone this repo
2. `python3 -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. Create a `.env` file with `ANTHROPIC_API_KEY=your_key_here`
5. `python main.py`

## What this project covers

- Anthropic Python SDK and the `messages.create()` API
- System prompts and prompt engineering patterns
- Multi-turn conversation history management
- Mode-based routing with a shared message history
- Git branching workflow: feature branches, merges, tags