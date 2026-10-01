import os
from google import genai
from dotenv import load_dotenv

def get_text(search):
    relevent_data = ""
    search=search.lower()

    with open(f"../Complete_knowlade_base/data.txt","r") as file:
        all_data=file.readlines()
        for line in all_data:
            if search in line.lower():
                relevent_data = relevent_data + line + '\n'
    return relevent_data

question = input("Ask your question: ")

load_dotenv()
API_KEY= os.getenv('GEMINI_API_KEY')

def Ask_Ai(question):

    relevant_data = get_text(question)

    prompt = f"""
You are an Apple Company AI bot that provides information
about Apple products.

Use the following knowledge base to answer the user's question.

--- KNOWLEDGE BASE ---
{relevant_data}
--- END KNOWLEDGE BASE ---

User Question:
{question}

Rules:
1. Answer only using the information provided in the knowledge base.
2. Do not make assumptions or invent information.
3. If the answer cannot be found in the knowledge base, politely say
   that the information is not available in the provided knowledge base.
4. If the user asks something unrelated to Apple products, politely
   explain that you can only answer questions related to Apple products.
5. Give a clear and detailed answer.
"""

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print(response.text)