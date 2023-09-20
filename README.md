# Tugas 3: Implementasi *Form* dan *Data Delivery* pada Django
### Ramadhan Andika Putra (2206081976) - PBP A <br>

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Membuat input *form* untuk menambahkan objek model pada app sebelumnya. ]
>> Blablabla
>>
>> Kalo spasi blala
<br>

>> #### [ Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by* ID, dan JSON *by* ID. ]
>> Blablabla
<br>

>> #### [ Membuat *routing* URL untuk masing-masing views yang telah ditambahkan pada poin 2 ]
>> Blablabla
<br>
<br>

#### Apa perbedaan antara form POST dan form GET dalam Django?
*Jawab:* <br>
Perbedaan utama antara form POST dan form GET dalam Django adalah cara data ditransfer dari *client* ke server. Form POST mengirimkan data secara langsung dalam badan pesan tanpa menampilkan pada URL, sedangkan form GET mengirimkan data dalam URL *string*.

***-Form POST-*** <br>
Form POST digunakan untuk mengirimkan data ke server untuk diproses. Data yang dikirimkan dengan form POST tidak terlihat di URL *string*, sehingga lebih aman daripada form GET. Form POST juga dapat digunakan untuk mengirimkan data yang besar, seperti gambar atau file.

***-Form GET-*** <br>
Form GET digunakan untuk mengambil data dari server. Data yang dikirimkan dengan form GET terlihat di URL *string*, sehingga kurang aman daripada form POST. Form GET juga dapat digunakan untuk mengirimkan data yang kecil, seperti parameter pencarian.
<br>
<br>

Intinya, secara garis besar perbedaan antara form POST dan form GET dalam Django  adalah sebagai berikut:
| Fitur |     Form POST     |      Form GET      |
| ---------------- | ---------------- | ---------------- |
| Cara Pengiriman data | Badan pesan                               | URL *string*                 |
| Kemananan            | Lebih aman                                | Kurang aman                  |
| Ukuran data          | Dapat mengirimkan data besar              | Dapat mengirimkan data kecil |
| Penggunaan           | Mengirimkan data ke server untuk diproses | Mengambil data dari server   |

Dengan perbedaan tersebut, tentunya ada saat dimana kita sebaiknya menggunakan Form POST atau Form GET. Untuk Form POST, biasanya digunakan jika kita ingin melakukan aktivitas berikut:
*	Mengirimkan data sensitif, seperti kata sandi atau nomor kartu kredit
*	Mengirimkan data yang besar, seperti gambar atau file
*	Mengirimkan data yang tidak ingin terlihat di URL *string*

Sedangkan, untuk Form GET biasanya digunakan jika kita ingin melakukan aktivitas berikut:
*	Mengambil data dari server
*	Mengirimkan data yang kecil
*	Mengirimkan data yang tidak sensitif
<br>

Berikut adalah beberapa contoh penggunaan form POST dan form GET dalam Django:
*	***Form POST untuk login:*** Form login biasanya menggunakan form POST untuk mengirimkan data kata sandi dan nama pengguna ke server.
*	***Form POST untuk mengunggah file:*** Form unggahan file biasanya menggunakan form POST untuk mengirimkan data file ke server.
*	***Form GET untuk pencarian:*** Form pencarian biasanya menggunakan form GET untuk mengirimkan parameter pencarian ke server.
<br>
<br>

#### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
*Jawab:* <br>
XML, JSON, dan HTML adalah format data yang umum digunakan untuk pengiriman data. Namun, ada beberapa perbedaan utama antara ketiga format tersebut, yaitu:

***-XML-***
*	XML adalah format data yang terstruktur. Data XML diformat dalam bentuk tag yang dapat diidentifikasi.
*	XML bersifat deklaratif, artinya format datanya didefinisikan dalam dokumen XML itu sendiri.
*	XML dapat digunakan untuk menggambarkan berbagai jenis data, termasuk data struktural, data hierarkis, dan data aritmatika.

***-JSON-***
*	JSON adalah format data yang tidak terstruktur. Data JSON diformat dalam bentuk objek, array, dan nilai primitif.
*	JSON bersifat deskriptif, artinya format datanya didefinisikan di luar dokumen JSON tersebut.
*	JSON sering digunakan untuk mengirimkan data sederhana, seperti data daftar atau data formulir.

***-HTML-***
*	HTML adalah format data yang digunakan untuk membuat halaman web.
*	HTML bersifat deklaratif, artinya format datanya didefinisikan dalam dokumen HTML itu sendiri.
*	HTML dapat digunakan untuk menggambarkan berbagai elemen halaman web, seperti teks, gambar, tabel, dan tautan.
<br>

Secara keseluruhan, berikut adalah tabel rangkuman mengenai perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data:
| Fitur |     XML     |      JSON     |      HTML     |
| -------------- | -------------- | -------------- | -------------- |
| Struktur       | Terstruktur                    | Tidak terstruktur         | Tidak terstruktur                |
| Deklaratif     | Ya                             | Ya                        | Ya                               |
| Kompatibilitas | Luas                           | Luas                      | Luas                             |
| Penggunaan     | Umum untuk berbagai jenis data | Umum untuk data sederhana | Umum untuk pembuatan halaman web |
<br>

Kesimpulannya, XML, JSON, dan HTML adalah format data yang memiliki kelebihan dan kekurangan masing-masing. Pemilihan format data yang tepat tergantung pada kebutuhan spesifik aplikasi, yaitu:
*	XML cocok untuk aplikasi yang membutuhkan pengiriman data yang terstruktur dan dapat digambarkan dengan jelas.
*	JSON cocok untuk aplikasi yang membutuhkan pengiriman data yang sederhana dan mudah dibaca oleh manusia.
*	HTML cocok untuk aplikasi yang membutuhkan pengiriman data untuk pembuatan halaman web
<br>
<br>

#### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
*Jawab:* <br>
Secara umum, JSON *(JavaScript Object Notation)* adalah format data yang ringan, mudah dibaca dan ditulis oleh manusia, dan mudah 'diurai' oleh komputer. JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan, yaitu:
*	***Sederhana dan mudah dibaca oleh manusia:*** JSON menggunakan format teks yang sederhana dan mudah dibaca oleh manusia. Hal ini memudahkan *developer* untuk memahami data yang dikirimkan. JSON dapat dibaca seperti kode JavaScript, sehingga developer JavaScript dapat dengan mudah memahaminya.
*	***Kompatibilitas yang luas:*** JSON didukung oleh berbagai bahasa pemrograman dan platform. Ini memudahkan pengembang untuk menggunakan JSON dalam aplikasi mereka. JSON didukung oleh semua bahasa pemrograman utama, termasuk JavaScript, Python, Java, C++, dan PHP. JSON juga didukung oleh berbagai platform, termasuk *web*, *mobile*, dan desktop.
*	***Efisiensi:*** JSON adalah format data yang efisien. Ini memudahkan data untuk dikirimkan dan diproses. JSON menggunakan format teks, sehingga data dapat dikirimkan dengan cepat dan mudah. JSON juga dapat 'diurai' dengan cepat oleh komputer.
<br>

Berikut adalah beberapa contoh penggunaan JSON dalam pertukaran data antara aplikasi web modern:
*	***Mengirimkan data dari aplikasi klien ke server:*** JSON sering digunakan untuk mengirimkan data dari aplikasi klien ke server, seperti data formulir atau data pencarian. Misalnya, saat pengguna mengirim formulir pendaftaran, data formulir tersebut dapat dikirimkan ke server dalam format JSON.
*	***Mengirimkan data dari server ke aplikasi klien:*** JSON sering digunakan untuk mengirimkan data dari server ke aplikasi klien, seperti data produk atau data berita. Misalnya, saat pengguna mengakses halaman produk, data produk tersebut dapat dikirimkan dari server ke aplikasi klien dalam format JSON.
*	***Menggunakan API RESTful:*** JSON sering digunakan dalam API RESTful untuk mewakili data yang dikirimkan dan diterima. API RESTful adalah jenis API yang menggunakan HTTP untuk berkomunikasi. JSON adalah format data yang ideal untuk API RESTful karena mudah dibaca dan ditulis oleh komputer.
<br>
<br>

#### *Screenshot* dari hasil akses URL pada Postman
HTML
-Gambar

XML
-Gambar

JSON
-Gambar

XML *by ID*
-Gambar

JSON *by ID*
-Gambar
