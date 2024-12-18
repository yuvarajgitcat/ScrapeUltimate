import requests

api_key = "YAIzaSyAJuypOFjlM9SFu7vz4Mf0tH2wgcOjU_oA"
url = "https://generativelanguage.googleapis.com/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers)
print(response.json())
