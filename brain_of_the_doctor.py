import os
import base64
from groq import Groq

# Set your API key
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not set in environment variables!")

client = Groq(api_key=GROQ_API_KEY)

# Convert image file to base64
def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Analyze image and query with Pixtral-12B
def analyze_image_with_query(query: str, encoded_image: str, model: str = "mixtral-8x7b"):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    },
                },
            ],
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    result = response.choices[0].message.content
    print("🧠 Model Response:\n", result)
    return result
