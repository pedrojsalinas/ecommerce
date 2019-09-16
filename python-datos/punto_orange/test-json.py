import json


with open('categorias.json', 'r') as myfile:
    data = myfile.read()
# parse file
obj = json.loads(data)
urls =[]
for i in obj:
    urls.append(i["p_href"])
print(urls)
    
