import requests


key = '9ae447ce6968419590f9b930d6b38efc'

url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={key}"
result = requests.get(url)
print(result.json())
print(type(result.json()))