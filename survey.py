import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")

headers = {
    "Authorization": access_token,
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

res = requests.get("https://api.neosia.unhas.ac.id/api/mahasiswa/belanja_krs", headers=headers)
data = res.json()

kelas_kuliahs = data.get("kartu_rencana_studi", {}).get("kelas_kuliahs", [])

print("Mengisi survey:")
session = requests.Session()
session.headers.update(headers)

for kelas in kelas_kuliahs:
    kelas_kuliah_id = kelas["id"]
    nama_mk = kelas["mata_kuliah"]["nama_resmi"]

    try:
        form_url = f"https://api.neosia.unhas.ac.id/survey/mahasiswa/kepuasan_peserta_kuliah?access_token={access_token}&kelas_kuliah_id={kelas_kuliah_id}"
        res_form = session.get(form_url)

        soup = BeautifulSoup(res_form.text, "html.parser")
        form = soup.find("form")
        if not form:
            print(f"⚠️ Form survei tidak ditemukan untuk {nama_mk}")
            continue

        action = form.get("action")
        csrf_token = form.find("input", {"name": "_token"}).get("value")

        form_data = {
            "_token": csrf_token,
            "access_token": access_token,
            "kelas_kuliah_id": kelas_kuliah_id
        }

        for input_tag in form.find_all("input", {"type": "radio"}):
            name = input_tag.get("name")
            value = input_tag.get("value")
            if name not in form_data:
                form_data[name] = value

        form_data["text_answer_for_question_73"] = "Materi disampaikan dengan sangat baik."
        form_data["text_answer_for_question_74"] = "Perlu ditingkatkan interaksi saat kuliah."

        submit = session.post(action, data=form_data)
        if submit.status_code == 200:
            print(f"✅ Survey untuk {nama_mk} berhasil dikirim.")
        else:
            print(f"❌ Gagal kirim survey {nama_mk}: {submit.status_code}")
            print(submit.text)

    except Exception as e:
        print(f"❌ Error saat isi survey {nama_mk}: {e}")