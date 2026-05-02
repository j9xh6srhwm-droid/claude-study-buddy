import anthropic
from dotenv import load_dotenv
from prompts import DEFAULT_MODE
from mode_parser import parse_mode, available_modes

load_dotenv()
client = anthropic.Anthropic()


def chat():
    conversation_history = []
    current_mode = DEFAULT_MODE

    print("=" * 54)
    print("  Claude Study Buddy — Claude Code 101 Tutor")
    print("=" * 54)
    print(f"\nAvailable modes:\n{available_modes()}")
    print("\nCommands: 'history', 'tokens', 'quit'")
    print("Usage: /quiz context window  or  just type freely\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        # ── Built-in commands ──────────────────────────────────────
        if user_input.lower() == "quit":
            print("\nSession ended. Good studying, Rohan!")
            break

        if user_input.lower() == "history":
            if not conversation_history:
                print("  No history yet.\n")
            else:
                print("\n── Conversation history ──")
                for i, msg in enumerate(conversation_history):
                    role = "You  " if msg["role"] == "user" else "Claude"
                    preview = msg["content"][:72].replace("\n", " ")
                    print(f"  [{i+1}] {role}: {preview}…")
                print()
            continue

        if user_input.lower() == "tokens":
            total_chars = sum(len(m["content"]) for m in conversation_history)
            estimated = total_chars // 4
            print(f"\n  Estimated tokens in history: ~{estimated:,}\n")
            continue

        # ── Mode parsing ───────────────────────────────────────────
        mode, system_prompt, content = parse_mode(user_input)

        # Summary mode operates on history, not on fresh content
        if mode == "summary":
            if not conversation_history:
                print("  Nothing to summarise yet — have a conversation first.\n")
                continue
            system_message = system_prompt
            messages_to_send = [
                *conversation_history,
                {"role": "user",    "content": "Please summarise our session."}
            ]
        else:
            # Use the stripped content as the actual message
            actual_content = content if content else user_input
            conversation_history.append({
                "role": "user",
                "content": actual_content
            })
            system_message = system_prompt
            messages_to_send = [ *conversation_history]

        if mode != current_mode:
            print(f"\n  ── Switched to {mode} mode ──\n")
            current_mode = mode

        # ── API call ───────────────────────────────────────────────
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            system = system_message,
            messages=messages_to_send
        )

        assistant_reply = response.content[0].text

        # Only append to history for non-summary modes
        if mode != "summary":
            conversation_history.append({
                "role": "assistant",
                "content": assistant_reply
            })

        print(f"\nClaude [{mode}]: {assistant_reply}")
        print(f"\n  [tokens — in: {response.usage.input_tokens}, "
              f"out: {response.usage.output_tokens}]\n")


if __name__ == "__main__":
    chat()