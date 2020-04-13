import requests

repo = requests.get("http://vcm-7631.vm.duke.edu:5000/regions")
answer = repo.json()
print(answer)
# for branch in answer:
#     print("Name of branch is:{}".format(branch["name"]))

# request_json = {"one": "Spain", "two": "China"}
# r = requests.post("http://vcm-7631.vm.duke.edu:5000/compare", json=request_json)
# if r.status_code == 200:
#     print(r.json())
# else:
#     print("Error with status code")
