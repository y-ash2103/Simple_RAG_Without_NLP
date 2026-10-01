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


print(get_text("iPhone 17"))
API_KEY= os.getenv("OPENAI_API_KEY")

print(API_KEY)
# def Ask_Ai(prompt): 
#     prompt""" """
#     client = genai.Client(api_key=)

#     interaction = client.interactions.create(
#         model="gemini-3.8-flash",
#         input=prompt
#     )

    # print(interaction.output_text)    
        
        