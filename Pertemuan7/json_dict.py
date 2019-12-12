import json

mahasiswa = []

fauzi = {"nama": "Fauzi", "alamat": "Losari"}
ilham = {"nama": "Ilham", "alamat": "Wanasari"}
hadi = {"nama": "Hadi", "alamat": "Brebes"}

mahasiswa.append(fauzi)
mahasiswa.append(ilham)
mahasiswa.append(hadi)

json_str = json.dumps(mahasiswa)
print(json_str)
