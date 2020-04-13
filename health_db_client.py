import requests

# server_name = "http://127.0.0.1:5000"
server_name = "http://vcm-14501.vm.duke.edu:5000"


def add_some_patient():
    new_patient = {"name": "Tifa Lockhart",
                   "id": 111,
                   "age": 18}
    r = requests.post(server_name+"/new_patient", json=new_patient)
    if r.status_code != 200:
        print("Error: {} - {}".format(r.status_code, r.text))
    else:
        print("Success {}".format(r.text))


def add_test():
    new_test = {"id": 111,
                "test_name": "hdl",
                "test_result": 101}
    r = requests.post(server_name+"/add_test", json=new_test)
    print(r.status_code)
    print(r.text)


def get_results():
    r = requests.get(server_name+"/get_results/111")
    if r.status_code != 200:
        print("Error {} - {}".format(r.status_code, r.text))
    else:
        print("Success {}".format(r.text))


if __name__ == '__main__':
    add_some_patient()
    add_test()
    get_results()
