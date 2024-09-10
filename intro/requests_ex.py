import requests
print(requests.__version__)

url = "https://jsonplaceholder.typicode.com/posts"
params = {'userId':1}

response = requests.get(url, params=params)
print(f"reponse is {response.json()}")


url = "https://google.com"

response = requests.get(url)
print(f"reponse is {response.text}")