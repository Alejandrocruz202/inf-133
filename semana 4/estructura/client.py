import requests
url = "http://localhost:8000"

#response = requests.get(f"{url}/posts")

#response2 = requests.get(f"{url}/post/2")

create =requests.post(f"{url}/posts/2",headers={"content-type ":"application/json"},data={"title":"title","content":"content"} )

#print(response.text)
#print(response2.text)
print(create.text)

