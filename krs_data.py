import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")

url = "https://api.neosia.unhas.ac.id/api/mahasiswa/belanja_krs"

headers = {
    "Authorization": access_token,
    "Accept": "application/json"
}

res = requests.get(url, headers=headers)

if res.status_code == 200:
    data = res.json()

    with open("krs_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Data KRS berhasil diambil dan disimpan ke krs_data.json")
else:
    print(f"Gagal mengambil data. Status: {res.status_code}")
    print(res.text)