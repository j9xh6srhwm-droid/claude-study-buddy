import anthropic
from dotenv import load_dotenv

# Loads ANTHROPIC_API_KEY from your .env file into the environment
load_dotenv()

# Creates a client — it auto-reads the key from the environment
client = anthropic.Anthropic()

#The actual API call
response = client.messages.create(
    model = "claude-opus-4-5",
    max_tokens = 1024,
    # Anthropic prefers system prompting as a seperate line item and not in the messages array
    system = "You are a pirate who explains concepts using only nautical metaphors.",
    messages = [
        {
            "role" : "user",
            "content" : "What is the difference between a model and a weight?"
        }
    ]
)

# Pull out the text from the response
print(response.content[0].text)
