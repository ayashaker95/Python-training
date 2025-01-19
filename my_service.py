import requests

url ="https://jsonplaceholder.typicode.com/posts/1/comments"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for entry in data:
     print(f"Name: {entry['name']}, Email: {entry['email']}")
else:
    print("the get is failed")
    
    
data ={
    "postId": 1,
    "id": 10,
    "name": "Aya",
    "email": "aya@gmail.com",
    "body": "hello from aya"
}

    
response = requests.post(url, data)
if response.status_code==201:
    print("created Successfully")
else:
    print("the post is faild")