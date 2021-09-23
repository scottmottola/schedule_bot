import requests

BASE = "http://127.0.0.1:5000/"

data = [{"user_name": "Scott", "user_pass": "pass1"}, 
        {"user_name": "Stephen", "user_pass": "pass2"}, 
        {"user_name": "Andrew", "user_pass": "pass3"}, 
        {"user_name": "Lacie", "user_pass": "pass4"}, 
        {"user_name": "Mom", "user_pass": "pass5"}, 
        {"user_name": "Dad", "user_pass": "pass6"}, 
        {"user_name": "Steve", "user_pass": "pass7"}, 
        {"user_name": "Alex", "user_pass": "pass8"}, 
        {"user_name": "Axle", "user_pass": "pass9"}]


for i in range(len(data)):
    route = BASE + "users"
    response = requests.post(route, data[i])
    print(route)
    print(response)
    print(response.status_code)
    print(response.json())

response = requests.get(BASE + "users", {"user_name": "Steven"})
print(response.json())

response4 = requests.get(BASE + "users", {"search_id": 1})
print(response4.json())

response = requests.patch(BASE + "users", {"search_id": 1, "user_name": "Steven"})
print(response.json())

response = requests.patch(BASE + "users", {"search_id": 9, "user_name": "Steven"})
print(response.json())

response = requests.delete(BASE + "users", data={"search_id": 8})
print(response)

response = requests.delete(BASE + "users", data={"search_id": 8})
print(response)