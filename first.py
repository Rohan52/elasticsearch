import requests

headers = {
    'Content-Type': 'application/x-ndjson',
}

params = (
    ('pretty', ''),
)

data = open('hospi_fin_10.json', 'rb').read()
response = requests.post('http://localhost:9200/hospi_fin_10/doc/_bulk', headers=headers, params=params, data=data)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://localhost:9200/shakespeare/doc/_bulk?pretty', headers=headers, data=data)















#import urllib2, urllib, json
#data = @hospital.json

#data = '{"director": "Rohan Parikh", "genre": ["Comedy","Action"], "year": 3017, "actor": ["Kadvo Kathiyavadi ","Mayank Patel","Hanik Patel"], "title": "Defence!"}'
#data = urllib.urlopen("https://api.github.com/users?since=10").read()
#url = 'http://localhost:9200/hospital/doc/_bulk?pretty'
#req = urllib2.Request(url, data, {'Content-Type': 'application/x-ndjson'})
#f = urllib2.urlopen(req)
#for x in f:
#    print(x)
#f.close()




#curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/hospital_project_final/doc/_bulk?pretty' --data-binary @hospital_project_final.json 
