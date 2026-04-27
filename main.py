import anthropic
from dotenv import load_dotenv
import prompts

# Loads ANTHROPIC_API_KEY from your .env file into the environment
load_dotenv()

# Creates a client — it auto-reads the key from the environment
client = anthropic.Anthropic()

def ask_tutor(question: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        # Anthropic prefers system prompting as a seperate line item and not in the messages array
        system = prompts.STUDY_BUDDY_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response.content[0].text

if __name__ == "__main__":
    question = "Can you explain tokenisation to me?"
    print(f"Question: {question}\n")
    print(ask_tutor(question))