import requests

url = "https://www.w3schools.com/xml/books.xml"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)