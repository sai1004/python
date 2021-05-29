

# a = [0, 1, 2, 3, 4]

# for a[-1] in a:
#     print(a)


# dict1 = {1: 2, 3: 4}
# for k, v in dict1.items():
#     print(v)
import requests
from termcolor import colored

passwords = ['admin', 'admin123', 'ami', 'superAdmin',
             'Nowary', 'Admin!23', 'Admin!234', 'samirt', 'user123']
response = requests.post('http://127.0.0.1:5000/api/auth/signin',
                         {'email': 'admin@xyz.com', 'password': 'Admin!234'})
print(response.text)

# for password in passwords:

#     response = requests.post('http://127.0.0.1:5000/api/auth/signin',
#                              {'email': 'admin@xyz.com', 'password': password})
#     print(response.text)

#     if response.status_code == 200:
#         print(
#             colored(" [!] password is {} Cracked ".format(password), "green"))

#     else:
#         print(
#             colored(" [!] password is {} Not Correct ".format(password), "red"))
