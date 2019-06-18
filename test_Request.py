import requests
baseUrl='https://reqres.in'
uri='/api/users'
params={'page':2}
data=requests.get(baseUrl+uri,params)
data_dict=data.json()
print(data_dict)
