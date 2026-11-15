import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
response.raise_for_status()
posts = response.json()
for post in posts[:5]:
    print("Заголовок:", post["title"])
    print("Текст:", post["body"])
    print("-" * 50)
