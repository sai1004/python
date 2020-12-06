import requests


# Making a get request
# response = requests.get('https://api.github.com/')

# # print request object
# print(response.url)

# # print status code
# print(response.status_code)

# print(response.json())


dic = ["admin", "api", "qa"]

for i in dic:
    res = requests.get(f"http://{i}.github.com")
    print(res.url, "--->", res.status_code)
    # print(res.status_code)


# r = requests.get('https://api.github.com/user',
#                  auth=('user', 'pass'))

# r.status_code
# # 200
# r.headers['content-type']
# # 'application/json; charset=utf8'
# r.encoding
# # 'utf-8'
# r.text
# # '{"type":"User"...'
# r.json()

# print("r", r.json())
