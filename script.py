import json

# Lire le fichier manifesto.json
with open("manifesto.json", "r") as file:
    data = json.load(file)

print("Message:", data["message"])
print("Challenge:", data["challenge"])

