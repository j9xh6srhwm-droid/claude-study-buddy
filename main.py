import anthropic
from dotenv import load_dotenv
from prompts import STUDY_BUDDY_SYSTEM_PROMPT

load_dotenv()
client = anthropic.Anthropic()


def chat():
    conversation_history = []

    print("=" * 50)
    print("Claude Study Buddy — Claude Code 101 Tutor")
    print("Type 'quit' to exit, 'history' to see the log")
    print("Type 'summary' to summarise the session")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("\nSession ended. See you next study session!")
            break

        if user_input.lower() == "history":
            print("\n--- Conversation history ---")
            for i, msg in enumerate(conversation_history):
                role = "You" if msg["role"] == "user" else "Claude"
                print(f"\n[{i + 1}] {role}:")
                print(msg["content"])
            print("\n---")
            continue

        if user_input.lower() == "summary":
            if not conversation_history:
                print("Nothing to summarise yet.")
                continue

            try:
                summary_response = client.messages.create(
                    model="claude-opus-4-5",
                    max_tokens=512,
                    system=(
                        "Summarise the following study session in 3 bullet points. "
                        "Focus on the concepts covered and any misconceptions corrected."
                    ),
                    messages=[
                        *conversation_history,
                        {
                            "role": "user",
                            "content": "Please summarise our session so far."
                        }
                    ]
                )

                print(f"\nSession summary:\n{summary_response.content[0].text}")

            except Exception as e:
                print("\nSomething went wrong while generating the summary:")
                print(e)

            continue

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=1024,
                system=STUDY_BUDDY_SYSTEM_PROMPT,
                messages=conversation_history
            )

            assistant_reply = response.content[0].text

            conversation_history.append({
                "role": "assistant",
                "content": assistant_reply
            })

            print(f"\nClaude: {assistant_reply}")

            print(
                f"\n[Tokens used — input: {response.usage.input_tokens}, "
                f"output: {response.usage.output_tokens}]"
            )

        except Exception as e:
            print("\nSomething went wrong while calling Claude:")
            print(e)

            # Remove the last user message because Claude did not answer it
            if conversation_history:
                conversation_history.pop()


if __name__ == "__main__":
    chat()