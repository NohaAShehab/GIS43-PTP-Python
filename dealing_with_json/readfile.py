import  json

try:
    with open('data.json') as jfile:
        print(jfile)
        # data = jfile.read()  #string
        # print(data)
        # for d in data:
        #     print(d)
        ### load json content into a list ?
        data = json.loads(jfile.read())
        print(data)
except Exception as e:
    print(e)

