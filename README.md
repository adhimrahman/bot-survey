
# 🧠 Bot Survey Neosia UNHAS

Skrip Python untuk **mengambil data KRS** dan **mengisi survei kepuasan mata kuliah** di portal [neosia.unhas.ac.id](https://neosia.unhas.ac.id) secara otomatis.

💡 **Ingin cara lebih mudah?**  
Gunakan versi Web UI tanpa install embel-embel. Cukup input Token Bearer langsung di form:  
👉 [https://bot-survey-web.app/](https://bot-survey-web.vercel.app/)

---

### 📘 Daftar Isi

- [📁 Struktur Proyek](#-struktur-proyek)
- [🔧 Instalasi](#-instalasi)
- [🧪 Cara Penggunaan](#-cara-penggunaan)
- [🔐 Cara Mendapatkan Token Bearer](#-cara-mendapatkan-token-bearer)

---

## 📁 Struktur Proyek

```
bot-survey/
├── .env                # Menyimpan access token (jangan diupload ke repo)
├── .env.example        # Contoh isi .env
├── .gitignore          
├── krs_data.json       # Output data KRS
├── krs_data.py         # Skrip ambil data KRS dan simpan ke file JSON
├── survey.py           # Skrip isi survei otomatis berdasarkan KRS
└── README.md           # Dokumentasi proyek ini
```

---

## 🔧 Instalasi

1. **Clone repositori ini:**

```bash
git clone https://github.com/username/bot-survey.git
cd bot-survey
```

2. **Install dependency:**

```bash
pip install requests beautifulsoup4 python-dotenv
```

3. **Salin `.env.example` ke `.env` dan isi access token milikmu:**

```env
ACCESS_TOKEN=Bearer eyJ0eXAiOiJ...
```

---

## 🧪 Cara Penggunaan

### 1. Ambil Data KRS dan Simpan

```bash
python krs_data.py
```

> Menyimpan ke `krs_data.json`.

---

### 2. Isi Survei Otomatis

```bash
python survey.py
```

> Mengisi semua survei berdasarkan `kelas_kuliahs` yang terdaftar di `kartu_rencana_studi`.

---

### 🔐 Cara Mendapatkan Token Bearer

Untuk menjalankan script ini, kamu membutuhkan token Bearer dari Neosia. Berikut langkah-langkahnya:

#### 1. Login dan Buka Developer Tools
- Login ke [https://neosia.unhas.ac.id](https://neosia.unhas.ac.id)
- Tekan `F12` untuk membuka DevTools
- Pergi ke tab **Network**

#### 2. Akses Halaman API
- Arahkan ke halaman seperti **Kartu Rencana Studi**
- Pilih request ke URL seperti `belanja_krs`
- Lalu klik request tersebut → tab **Headers**

#### 3. Salin Header Authorization
- Cari bagian `Authorization`
- Copy seluruh nilai `Bearer ...`
- ![Contoh](https://res.cloudinary.com/dsqgrzcgb/image/upload/v1751469779/Screenshot_2025-07-02_231238_xbivee.png)

#### 4. Simpan ke `.env`
Contoh isi file `.env`:
```env
ACCESS_TOKEN=Bearer eyJ0eXAiOiJKV1QiLCJhbGci...
```

> ⏳ Token hanya berlaku dalam waktu terbatas. Ganti jika sudah tidak valid.

---

## ⚠️ Peringatan

- **Token akses (`ACCESS_TOKEN`) bersifat pribadi**. Jangan dibagikan atau diupload ke GitHub.
- Hanya gunakan untuk kebutuhan pribadi, jangan menyalahgunakan sistem akademik.