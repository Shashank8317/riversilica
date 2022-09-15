import requests
session = requests.Session()
print(session.cookies.get_dict())
data={"user_name":"admin", "password":"pixfix@123"}
response = session.post('http://skycode5.riversilica.com/users',data=data)
print(session.cookies.get_dict()["PHPSESSID"])
phpSessionId=session.cookies.get_dict()["PHPSESSID"]
response = session.get("http://skycode5.riversilica.com/jobs/job_list",headers={"PHPSESSID":phpSessionId})
print(response.text)
