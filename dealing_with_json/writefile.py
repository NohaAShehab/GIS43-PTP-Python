# import json
# try:
#     with open('data.json','r') as jfile:
#         old_content = json.loads(jfile.read())  # list ?
#         d = {"name":"Added", "intake": 443 }
#         ## convert dictionary to string
#         # jfile.write(str(d))
#         # d=json.dumps(d)
#         # print(d)
#         with open('data.json', 'w') as myfile:
#             old_content.append(d)
#             myfile.write(json.dumps(old_content, indent=5))
#
# except Exception as e:
#     print(e)


class Engineer:
    def speak(self):
        print("--HHooo ")


e = Engineer()
e.speak()

Engineer.speak(e)