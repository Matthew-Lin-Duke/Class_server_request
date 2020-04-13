import requests

# r = requests.get("http://127.0.0.1:5000/info")
# print(r.status_code)
# x = r.text
# x = r.json()
# print(type(x))
# print(x)

name_to_send = "Bob"
r = requests.post("http://127.0.0.1:5000/send_name",
                  json=name_to_send)
print(r.status_code)
print(r.text)

rp = requests.get("http://127.0.0.1:5000/get_names")
print(rp.status_code)
print(rp.text)