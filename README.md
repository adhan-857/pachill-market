# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
### Ramadhan Andika Putra (2206081976) - PBP A <br>

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin. ]
>> Karena saya ingin menambahkan CSS menggunakan framework bootstrap, maka saya menambahkan Bootstrap CSS dan juga JS pada file base.html yang ada pada templates folder yang berada di root project.
>>
>> Lalu, dengan memanfaatkan bootstrap saya menambahkan *navigation bar* pada halaman `main.html`. Navigation bar menampilkan nama app **'Pachill.Market'** serta tombol *'home'* (jika belum login, akan mengarahkan ke halaman login. jika sudah login, akan mengarahkan ke halaman main). Jika pengguna sudah login, maka pada navbar akan muncul username pengguna, waktu last login-nya, serta tombol untuk logout.
>>
>> Navbar jika belum login:<br>
>> <img width="959" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/52ac3695-ce75-4bb9-af5a-718953069e1e"><br>
>> <img width="812" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/30f6dc94-7590-445e-aead-555c88a90540">
>>
>> Navbar jika sudah login:<br>
>> <img width="949" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/24f64711-992b-4410-996b-f372d2de80df"><br>
>> <img width="816" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/57a98fcc-29e9-429f-8b4c-ad05fb2ad0ff">
>>
>> <br>
>> Lalu, saya membuat agar tampilan applikasi saya rata tengah dengan memanfaatkan `justify-content-center` dan `align-items-center`. Tak lupa, saya menambahkan class `card` dan menggunakan `bg-light` untuk mengatur warna latar belakang dari *card* tempat saya menaruh isi konten dari app saya.<br>
>> <img width="769" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/6056f380-b940-4cf2-a16b-9fd3039aa97d"><br>
>> <img width="960" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/271ee028-5939-46de-845d-bd48c587e99e">

<br>

>> #### [ Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card. ]
>> Untuk melakukan kustomisasi halaman daftar inventori, saya menggunakan `card`. Jadi, untuk sebuah produk akan dibuatkan sebuah card yang menampilkan detail informasi dari produk tersebut. Banyaknya card akan mengikuti jumlah jenis produk yang dimasukkan.
>> 
>> <br>
>> Tampilan kode:<br>
>> <img width="273" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/2619e986-43f3-4288-a0db-447375682d16"><br>
>> <br>
>> Tampilan halaman daftar inventori:<br>
>> <img width="960" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/1e33c84d-081e-4a26-a0a4-ce311cda4c4b"><br>

<br>
<br>

#### Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.
*Jawab:* <br>
Ada berbagai jenis selector, dan masing-masing memiliki kegunaan serta manfaat tertentu. Berikut ini adalah beberapa jenis selector dasar dan manfaat serta waktu yang tepat untuk menggunakannya:

<br>**Universal Selector ('*'):**
* Manfaat: Memilih semua elemen di halaman.
* Kapan menggunakannya: Saat kitaa ingin menerapkan gaya ke semua elemen di halaman. Misalnya, untuk mengatur margin dan padding menjadi 0 di semua elemen.

<br>**Type Selector (atau Element Selector):**
* Manfaat: Memilih elemen berdasarkan nama elemen (mis., `div`, `h1`, `p`).
* Kapan menggunakannya: Saat kita ingin menerapkan gaya ke semua elemen dengan jenis tertentu. Misalnya, untuk mengatur semua paragraf `(p)` memiliki warna teks biru.

<br>**Class Selector (`.classname`):**
* Manfaat: Memilih elemen berdasarkan atribut kelas mereka.
* Kapan menggunakannya: Saat kita ingin menerapkan gaya khusus ke sekelompok elemen tanpa mengacu pada jenis elemennya. Misalnya, jika kita memiliki beberapa elemen dengan kelas `highlight`, kita dapat menggunakan selector kelas untuk mengatur gaya bagi semua elemen tersebut.

<br>**ID Selector (`#idname`):**
* Manfaat: Memilih elemen berdasarkan atribut id mereka.
* Kapan menggunakannya: Saat kita ingin memberikan gaya satu elemen spesifik yang memiliki ID tertentu. Ingat, ID harus unik dalam halaman, sehingga ID selector biasanya digunakan untuk elemen yang unik dalam desain.

<br>**ID Selector (`#idname`):**
* Manfaat: Memilih elemen berdasarkan atribut id mereka.
 Kapan menggunakannya: Saat kita ingin memberikan gaya satu elemen spesifik yang memiliki ID tertentu. Ingat, ID harus unik dalam halaman, sehingga ID selector biasanya digunakan untuk elemen yang unik dalam desain.

<br>**Descendant Selector (mis., `article p`):**
* Manfaat: Memilih elemen berdasarkan hubungan keturunannya.
* Kapan menggunakannya: Saat kita ingin menargetkan elemen yang berada di dalam elemen lain. Misalnya, untuk memberikan gaya semua paragraf yang berada di dalam elemen 'article'.

<br>**Grouping Selector:**
* Manfaat: Menggabungkan beberapa selector untuk menerapkan gaya yang sama ke beberapa elemen.
* Kapan menggunakannya: Saat kita ingin menerapkan satu set gaya ke beberapa elemen berbeda. Misalnya, `h1, h2, h3 { font-family: Arial; }`.
<br>
<br>

#### Jelaskan HTML5 Tag yang kamu ketahui.
*Jawab:* <br>
HTML5 Tag (atau elemen HTML5) adalah blok bangunan dasar dari halaman web HTML5. Tag digunakan untuk mendefinisikan struktur dan konten halaman web. Misalnya, tag `<p>` digunakan untuk mendefinisikan paragraf, tag `<img>` digunakan untuk mendefinisikan gambar, dan tag `<a>` digunakan untuk mendefinisikan hyperlink.

HTML5 memiliki lebih dari 100 tag yang berbeda, tetapi beberapa tag yang paling umum digunakan termasuk:
* `<head>` dan `<body>`: Tag ini mendefinisikan bagian kepala dan badan dari halaman web.
* `<title>`: Tag ini mendefinisikan judul halaman web.
* `<h1>`, `<h2>`, `<h3>`, dst.: Tag ini mendefinisikan heading (judul) dari berbagai tingkat.
* `<p>`: Tag ini mendefinisikan paragraf.
* `<img>`: Tag ini mendefinisikan gambar.
* `<a>`: Tag ini mendefinisikan hyperlink.
* `<ul>` dan `<ol>`: Tag ini mendefinisikan daftar tidak berurut dan daftar berurut.
* `<table>`: Tag ini mendefinisikan tabel.
* `<div>`: Tag ini mendefinisikan divisi, yang merupakan blok konten generik.

HTML5 juga memiliki sejumlah tag baru yang tidak tersedia di versi HTML sebelumnya. Tag-tag baru ini menambahkan fungsionalitas baru ke halaman web, seperti:
* `<audio>` dan `<video>`: Tag ini digunakan untuk mendefinisikan audio dan video.
* `<canvas>`: Tag ini digunakan untuk menggambar grafik dan animasi.
* `<svg>`: Tag ini digunakan untuk mendefinisikan gambar vektor.
*`<section>`: Tag ini digunakan untuk mendefinisikan bagian dari halaman web.
* `<article>`: Tag ini digunakan untuk mendefinisikan artikel mandiri.

Tag HTML5 ditulis dalam bentuk pasangan tag, dengan tag pembuka (`<tag>`) dan tag penutup (`</tag>`). Misalnya, untuk mendefinisikan paragraf, kita akan menggunakan tag `<p>` sebagai tag pembuka dan tag `</p>` sebagai tag penutup. Semua konten paragraf akan ditulis di antara tag pembuka dan tag penutup.
<br>
<br>

#### Jelaskan perbedaan antara margin dan padding.
*Jawab:* <br>

Margin dan padding adalah dua properti CSS yang digunakan untuk mengatur jarak antara elemen HTML. Margin adalah jarak antara elemen dan elemen lain di sekitarnya, sedangkan padding adalah jarak antara elemen dan kontennya.

Perbedaan antara margin dan padding:
| Fitur    |     Margin       |      Padding     |
| -------- | ---------------- | ---------------- |
| Lokasi                        | Di luar elemen                                | Di dalam elemen                             |
| Pengaruh terhadap elemen lain | Mengatur jarak antara elemen dan elemen lain  | Mengatur jarak antara elemen dan kontennya  |
| Nilai                         | Bisa positif, negatif, atau auto              | Bisa positif atau negatif                   |
| Nilai default                 | 0px                                           | 0px                                         |

Kapan menggunakannya:
* Margin digunakan untuk mengatur jarak antara elemen dan elemen lain. Misalnya, kita dapat menggunakan margin untuk membuat elemen-elemen di halaman web saling berjauhan.
* Padding digunakan untuk mengatur jarak antara elemen dan kontennya. Misalnya, kita dapat menggunakan padding untuk membuat elemen tampak lebih tebal atau untuk menambahkan ruang kosong di sekitar konten.
<br>

Berikut adalah beberapa contoh penggunaan margin dan padding:<br>
***Margin:***
* Untuk membuat elemen-elemen di halaman web saling berjauhan
* Untuk membuat elemen tampak lebih besar atau lebih kecil
* Untuk mengatur tata letak halaman web

***Padding:***
* Untuk membuat elemen tampak lebih tebal atau lebih besar
* Untuk menambahkan ruang kosong di sekitar konten
* Untuk membuat elemen tampak lebih menarik
<br>
<br>

#### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
*Jawab:* <br>
Tailwind dan Bootstrap adalah dua framework CSS yang populer untuk membangun tampilan web. Keduanya memiliki kelebihan dan kekurangannya masing-masing, sehingga penting untuk memilih framework yang tepat untuk kebutuhan kita.

Perbedaan antara Tailwind dan Bootstrap:
| Fitur    |     Tailwind       |      Bootstrap     |
| -------- | ------------------ | ------------------ |
| Pendekatan    |	Utility-first |	Component-based    |
| Ukuran file   |	Lebih kecil   |	Lebih besar        |
| Fleksibilitas |	Lebih tinggi  |	Lebih rendah       |
| Responsivitas |	Built-in      |	Built-in           |
| Dokumentasi	  | Lengkap       |	Lengkap            |
| Komunitas     |	Aktif         |	Aktif              |

***Tailwind***
* Pendekatan: Tailwind menggunakan pendekatan utility-first, yang berarti kita menggunakan kelas CSS yang sudah jadi untuk mengatur tampilan elemen.
* Ukuran file: Tailwind memiliki ukuran file yang lebih kecil daripada Bootstrap, sehingga lebih hemat bandwidth.
* Fleksibilitas: Tailwind menawarkan fleksibilitas yang lebih tinggi daripada Bootstrap, karena kita bisa menyesuaikan tampilan elemen sesuai kebutuhan.
* Responsivitas: Tailwind memiliki responsivitas yang built-in, sehingga kita tidak perlu mengaturnya secara manual.
* Dokumentasi: Tailwind memiliki dokumentasi yang lengkap dan mudah dipahami.
* Komunitas: Tailwind memiliki komunitas yang aktif dan membantu.

***Bootstrap***
* Pendekatan: Bootstrap menggunakan pendekatan component-based, yang berarti kita menggunakan komponen yang sudah jadi untuk membangun tampilan halaman web.
* Ukuran file: Bootstrap memiliki ukuran file yang lebih besar daripada Tailwind.
* Fleksibilitas: Bootstrap menawarkan fleksibilitas yang lebih rendah daripada Tailwind, karena kita harus menyesuaikan komponen yang sudah jadi.
* Responsivitas: Bootstrap memiliki responsivitas yang built-in, sehingga kita tidak perlu mengaturnya secara manual.
* Dokumentasi: Bootstrap memiliki dokumentasi yang lengkap dan mudah dipahami.
* Komunitas: Bootstrap memiliki komunitas yang aktif dan membantu.

<br>
Kapan sebaiknya menggunakan Bootstrap daripada Tailwind, dan sebaliknya? <br>

***Bootstrap:***
* Saat kita membutuhkan framework CSS yang siap pakai dengan banyak komponen yang sudah jadi.
* Saat kita membutuhkan framework CSS yang responsif.
* Saat kita membutuhkan framework CSS dengan komunitas yang aktif.

***Tailwind:***
* Saat kita membutuhkan framework CSS yang fleksibel dan bisa disesuaikan dengan kebutuhan.
* Saat kita membutuhkan framework CSS yang ukuran filenya kecil.
* Saat kita membutuhkan framework CSS yang baru dan up-to-date.

<br>
Secara umum, Bootstrap cocok untuk proyek yang membutuhkan tampilan web yang standar dan siap pakai, sedangkan Tailwind cocok untuk proyek yang membutuhkan tampilan web yang fleksibel dan bisa disesuaikan dengan kebutuhan.
<br>
