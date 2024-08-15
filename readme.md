# Instagram Story Viewer

Instagram Story Viewer adalah sebuah aplikasi Python yang memungkinkan pengguna untuk melihat stories Instagram dari akun target secara otomatis.

## Fitur

- Login menggunakan kredensial atau cookie tersimpan
- Melihat stories dari satu atau beberapa akun target
- Konfigurasi waktu jeda antara melihat stories

## Persyaratan

- Python 3.9+
- pip (Python package installer)

## Instalasi

1. Clone repositori ini:
```bash
git clone https://github.com/yusuf601/ig-automation-read-story.git
```
2. Buat virtual environment:
 **untuk Windows**  
```bash
python -m venv venv
```
**Untuk Linux**
```bash
python3 -m venv venv
```
3. Aktifkan virtual environment:
- Pada Windows:
  ```
  venv\Scripts\activate
  ```
- Pada macOS dan Linux:
  ```
  source venv/bin/activate
  ```
4. Install dependensi:
```bash
pip install -r requirements.txt
```

## Penggunaan

Jalankan aplikasi dengan perintah:
```bash
python3 main.py
```
## Struktur Proyek
```instagram-story-viewer/
│
├── app/
│   ├── services/
│   │   ├── init.py
│   │   ├── auth_service.py
│   │   └── instagram_service.py
│   │
│   ├── utils/
│   │   ├── init.py
│   │   └── config.py
│   │
│   └── exceptions/
│       ├── init.py
│       ├── login_exception.py
│       └── story_view_exception.py
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```
## Peringatan

Penggunaan alat otomatis pada Instagram dapat melanggar Ketentuan Layanan mereka. Gunakan dengan bijak dan atas risiko Anda sendiri.

## Lisensi

[MIT License](https://opensource.org/licenses/MIT)

## Kontribusi

Kontribusi, isu, dan permintaan fitur dipersilakan. Jangan ragu untuk memeriksa halaman isu jika Anda ingin berkontribusi.

