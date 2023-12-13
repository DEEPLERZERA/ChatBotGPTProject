import openai 
import dotenv
import os

def chat(sua_duvida, nome_personalidade):
    prompt_sistema = f"""
            Você se chama {nome_personalidade}, e quero que você incorpore a personalidade sendo ela de alguma forma, responda as perguntas do usuário como se fosse a pessoa
            especificada. Se a pessoa te chamar por outra coisa que não seja um nome de uma personalidade válida, simplesmente diga que não pode responder a pergunta.
    """
    resposta = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": prompt_sistema
            },
            {
                "role": "user",
                "content": sua_duvida
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=5
    )

    print(resposta.choices[0].message.content)

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Digite sua dúvida:")
sua_duvida = input()
while True:
    print("Digite o nome da personalidade:")
    nome_personalidade = input()
    chat(sua_duvida, nome_personalidade)