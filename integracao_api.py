import openai 
import dotenv
import os

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
resposta = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "system",
            "content": "Você é o Aryton Senna, maior piloto da história da Formula 1" 
        },
        {
            "role": "user",
            "content": "Olá Senna! Sou seu fan qual sua pista favorita?"
        }
    ]

)

print(resposta)