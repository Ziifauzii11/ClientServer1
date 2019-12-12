import json

data = '[{ "nama" : "Fauzi", "alamat" : "Losari" },' \
       '{ "nama" : "Ilham", "alamat" : "Wanasari" }]'

result = json.loads(data)

for x in result:
    print(x['nama'])
