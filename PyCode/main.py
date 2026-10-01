import os

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
