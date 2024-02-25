# ITPath

ITPath adalah platform forum IT yang dikembangkan menggunakan Django, Vue.js, dan MongoDB. Platform ini dirancang untuk memfasilitasi diskusi, berbagi pengetahuan, dan kolaborasi di antara para profesional dan penggemar IT.

## Fitur Utama

- Diskusi Forum: Pengguna dapat membuat, membalas, dan menjelajahi berbagai topik terkait IT.
- Learning: Pengguna dapat mengunggah dan berbagi materi belajar sesuai dengan tema yang relevan.
- Profil Pengguna: Setiap pengguna memiliki profil pribadi yang mencakup informasi tentang diri mereka dan aktivitas di platform.
- Kategori Pengguna: Terdapat beberapa kategori pengguna seperti admin, pengguna biasa, dan lainnya.
- Pencarian Topik: Pengguna dapat mencari topik berdasarkan kata kunci atau kategori tertentu.
- Notifikasi: Sistem notifikasi untuk memberi tahu pengguna tentang aktivitas terbaru di forum.

## Instalasi

### Persyaratan

- Python 3.x
- Node.js
- MongoDB

### Langkah-langkah

1. **Klon Proyek:**
    ```bash
    git clone https://github.com/your-username/ITPath.git
    cd ITPath
    ```

2. **Setup Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3. **Setup Frontend:**
    ```bash
    cd frontend
    npm install
    npm run serve
    ```

4. **Akses Aplikasi:**
    Buka browser dan akses `http://localhost:8080`.

## Kontribusi

Kami senang menerima kontribusi dari komunitas. Jika Anda ingin berkontribusi pada proyek ini, silakan ikuti langkah-langkah berikut:

1. Fork repositori ini.
2. Buat cabang fitur baru (`git checkout -b fitur/fitur-baru`).
3. Lakukan perubahan yang diperlukan dan commit (`git commit -am 'Tambahkan fitur baru'`).
4. Push ke cabang (`git push origin fitur/fitur-baru`).
5. Buat pull request.

## Lisensi

Proyek ini dilisensikan di bawah lisensi [MIT License](LICENSE).
