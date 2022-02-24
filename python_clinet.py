import requests


response = requests.delete("http://127.0.0.1:8000/home_cvb/",)
print(response.content)

# response = requests.delete("http://127.0.0.1:8000/home_cvb/", data = {"key":"value"})
# # print(response)
# print(response.content)
# # s = requests.Session()
# # print(s.__dict__)