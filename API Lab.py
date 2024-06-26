import requests

url = "https://safeut.test.med.utah.edu/apidemo/RestService/Quote"

req = requests.get(url)

print("Status Code:", req.status_code)
ret_val = req.json()
print(ret_val)

