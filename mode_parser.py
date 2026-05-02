from prompts import MODE_REGISTRY, DEFAULT_MODE


def parse_mode(user_input: str) -> tuple[str, str, str]:
    """
    Parse a user input string for a mode prefix.

    Syntax: /mode <message>  e.g. "/quiz context window"
    If no valid prefix is found, defaults to the explain mode.

    Returns:
        mode     — the mode key ("explain", "quiz", "summary", "/eli5")
        prompt   — the system prompt for that mode
        content  — the user's message with the prefix stripped
    """
    user_input = user_input.strip()

    if user_input.startswith("/"):
        parts = user_input[1:].split(" ", 1)   # split on first space only
        command = parts[0].lower()

        if command in MODE_REGISTRY:
            content = parts[1].strip() if len(parts) > 1 else ""
            return command, MODE_REGISTRY[command], content

    # No valid prefix — fall back to default mode
    return DEFAULT_MODE, MODE_REGISTRY[DEFAULT_MODE], user_input


def available_modes() -> str:
    return "  " + "\n  ".join(f"/{k}" for k in MODE_REGISTRY)