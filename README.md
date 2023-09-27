# Tugas 4: Implementasi Autentikasi, *Session*, dan *Cookies* pada Django
### Ramadhan Andika Putra (2206081976) - PBP A <br>

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. ]
>> Pertama, saya membuat fungsi dengan nama *register* yang menerima parameter request pada *views.py* yang berada pada subdirektori *main*. Lalu, saya memanfaatkan UserCreationForm sebagai impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web yang saya buat. Setelah itu, saya mengimpor fungsi *register* yang telah dibuat pada *urls.py* yang terdapat pada subdirektori *main*. Tak lupa. saya menambahkan *path url* ke dalam *urlpatterns* untuk mengakses fungsi yang sudah diimpor tadi.
>>
>> Langkah selanjutnya, saya membuat fungsi dengan nama *login_user* yang menerima parameter request pada *views.py* yang berada pada subdirektori *main*. Lalu, saya mengimpor *function authenticate, login* untuk melakukan autentikasi dan *login* jika autentikasi berhasil. Setelah itu, saya mengimpor fungsi *login_user* yang telah dibuat pada *urls.py* yang terdapat pada subdirektori *main*. Tak lupa. saya menambahkan *path url* ke dalam *urlpatterns* untuk mengakses fungsi yang sudah diimpor tadi.
>>
>> Yang terakhir, saya membuat fungsi dengan nama *logout_user* yang menerima parameter request pada *views.py* yang berada pada subdirektori *main*. Lalu, saya mengimpor *logout* pada bagian paling atas. Setelah itu, saya mengimpor fungsi *logout_user* yang telah dibuat pada *urls.py* yang terdapat pada subdirektori *main*. Tak lupa. saya menambahkan *path url* ke dalam *urlpatterns* untuk mengakses fungsi yang sudah diimpor tadi
<br>

>> #### [ Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. ]
>> #### [ Menghubungkan model Item dengan User. ]
>> Untuk saat ini semua akun akan terhubung ke data yang sama entah siapapun yang membuatnya. Sekarang kita akan membuat user menjadi bagian dari models agar setiap account memiliki datanya masing-masing. Langkah pertama, kita akan menambahkan user pada class Item pada models.py di subdirektori main. Lalu, kita akan mengubah function show_main dan create_product pada views.py di direktor main agar kita dapat menampilkan objek Product yang terasosiasikan dengan pengguna yang sedang login. Hal tersebut dilakukan dengan menyaring seluruh objek dengan hanya mengambil Product yang dimana field user terisi dengan objek User yang sama dengan pengguna yang sedang login.
>>
>> Selanjutnya, karena kita mengubah models.py maka kita perlu melakukan migrasi dengan menjalankan *python manage.py makemigrations* dan *python manage.py migrate* untuk mengaplikasikan migrasi yang dilakukan. Kita bisa mencobanya dengan membuat akun baru dan login dengan akun yang baru dibuat. Jika kita mengamati halaman utama, produk yang tadi telah dibuat dengan akun sebelumnya tidak akan ditampilkan di halaman pengguna akun yang baru saja kita buat.
<br>

>> #### [ Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi. ]
>> Untuk mengimplementasikan checklist ini, saya memanfaatkan cookies yang ada pada Django. Pada views.py di direktori main, saya menambahkan import datetime. Setelah itu, saya mengubah fungsi login_user agar men-set cookies dengan key last_login dengan waktu saat ini. Lalu, saya juga menambahkan variable last_login yang datanya berasal dari COOKIES di dalam context pada fungsi show_main. Setelah itu, saya juga mengubah function logout_user agar dapat menghapus cookie last_login saat pengguna melakukan logout.
>>
>> Langkah terakhir, saya menambahkan potongan kode tambahkan berikut di antara tabel dan tombol logout untuk menampilkan data last login pada halaman utama aplikasi. <br>
>> *...*
>> *<h5>Sesi terakhir login: {{ last_login }}</h5>*
>> *...*
>>
>> Sekarang, jika kita mnelakukan login maka akan terlihat tampilan data last login kita pada halaman utama aplikasi.
<br>
<br>

#### Apa itu Django *UserCreationForm*, dan jelaskan apa kelebihan dan kekurangannya?
*Jawab:* <br>
Django UserCreationForm adalah sebuah form yang disediakan oleh kerangka kerja Django yang dapat digunakan untuk membuat pengguna baru di Django. Form ini sudah terintegrasi dengan sistem autentikasi Django, sehingga pengguna baru yang dibuat dengan form ini akan langsung dapat login ke aplikasi Django.

Kelebihan Django UserCreationForm:
* **Mudah digunakan**. Django UserCreationForm sudah memiliki semua field yang dibutuhkan untuk membuat pengguna baru, sehingga pengguna tidak perlu membuat form sendiri.
* **Terintegrasi dengan sistem autentikasi Django**. Pengguna baru yang dibuat dengan Django UserCreationForm akan langsung dapat login ke aplikasi Django.
* **Dapat disesuaikan**. Django UserCreationForm dapat disesuaikan dengan kebutuhan aplikasi. Misalnya, pengguna dapat menambahkan field tambahan, seperti alamat email atau nomor telepon.

Kekurangan Django UserCreationForm:
* **Tidak dapat digunakan untuk membuat pengguna dengan peran khusus**. Django UserCreationForm hanya dapat digunakan untuk membuat pengguna dengan peran default, yaitu "user".
* **Tidak dapat digunakan untuk membuat pengguna dengan data yang sudah ada**. Django UserCreationForm hanya dapat digunakan untuk membuat pengguna baru.

Secara keseluruhan, UserCreationForm sangat berguna untuk skenario umum pembuatan pengguna dalam aplikasi Django, tetapi perlu dipertimbangkan dengan hati-hati jika kita memiliki kebutuhan yang sangat khusus atau kompleks dalam proses pendaftaran pengguna kita.
<br>
<br>

#### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
*Jawab:* <br>
Authentication dan authorization adalah dua konsep yang berbeda dalam keamanan komputer. Authentication adalah proses untuk memverifikasi identitas pengguna, sedangkan authorization adalah proses untuk menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu. *(Ibarat sebuah rumah, authentication adalah proses yang memverifikasi bahwa kita adalah pemilik rumah. Authorization adalah proses yang menentukan apakah kita memiliki izin untuk memasuki rumah tersebut.)*
 
Untuk lebih detailnya, authentication adalah proses untuk memverifikasi identitas pengguna. Hal ini dilakukan untuk memastikan bahwa pengguna yang mencoba mengakses sistem adalah pengguna yang sah. Authentication dapat dilakukan dengan berbagai metode, seperti menggunakan nama pengguna dan kata sandi, menggunakan token keamanan, atau menggunakan biometrik.
 
Sedangkan, authorization adalah proses untuk menentukan apakah pengguna memiliki izin untuk mengakses sumber daya tertentu. Hal ini dilakukan untuk memastikan bahwa pengguna hanya dapat mengakses sumber daya yang mereka berhak akses. Authorization dapat dilakukan dengan berbagai metode, seperti menggunakan peran pengguna, menggunakan kebijakan akses, atau menggunakan kontrol akses berbasis objek.
 
Keduanya memiliki beberapa perbedaan, yaitu: <br>
***Authentication***
* Memverfikasi siapa pengguna sebenarnya
* Bekerja menggunakan kata sandi, OTP, informasi biometrik, dan informasi lain yang diberikan atau dimasukkan oleh pengguna
* Tahap pertama dalam proses pemeriksaan keamanan
* Terlihat dan sebagian dapat diubah oleh pengguna
 
***Authorization***
* Menentukan sumber daya apa yang dapat diakses pengguna
* Bekerja berdasarkan peraturan yang telah ditetapkan oleh developer atau organisasi pemilik aplikasi
* Selalu dijalankan setelah proses authentication selesai
* Tidak terlihat dan tidak dapat diubah oleh pengguna

Autentikasi dan otorisasi sangat penting dalam keamanan aplikasi web karena autentikasi membantu memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sedangkan otorisasi membantu memastikan bahwa pengguna hanya dapat mengakses sumber daya yang mereka miliki izin untuk mengakses.

Tanpa autentikasi, siapa pun dapat mengakses aplikasi kita, bahkan jika mereka tidak memiliki izin untuk melakukannya. Hal ini dapat menyebabkan pencurian data, penyalahgunaan sistem, dan kerusakan lainnya. Tanpa otorisasi, pengguna dapat mengakses semua sumber daya dalam aplikasi Anda, bahkan jika mereka tidak memiliki izin untuk melakukannya. Hal ini dapat menyebabkan kebocoran data, penyalahgunaan sistem, dan kerusakan lainnya.

Oleh karena itu, penting untuk menerapkan autentikasi dan otorisasi yang tepat dalam aplikasi web kita.
<br>
<br>

#### Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
*Jawab:* <br>
*Cookies* adalah sejumlah kecil data yang disimpan di dalam browser web pengguna saat mereka mengunjungi sebuah situs web. *Cookies* digunakan dalam konteks aplikasi web untuk berbagai tujuan, termasuk mengidentifikasi pengguna, melacak preferensi pengguna, menyimpan data sesi, dan lainnya. Dalam konteks Django, *cookies* dapat digunakan untuk mengelola data sesi pengguna.

Dalam konteks aplikasi web, *cookie* sering digunakan untuk mengelola data sesi pengguna. Sesi pengguna adalah jangka waktu di mana pengguna berinteraksi dengan aplikasi web. Selama sesi, aplikasi web dapat menyimpan informasi tentang pengguna, seperti:
* Identitas pengguna
* Informasi tentang halaman yang telah dikunjungi pengguna
* Informasi tentang tindakan yang telah dilakukan pengguna

Django menggunakan cookie untuk mengelola data sesi pengguna dengan cara berikut:
* Django membuat *cookie* sesi saat pengguna masuk ke aplikasi web.
* *Cookie* sesi berisi informasi tentang identitas pengguna, seperti ID pengguna dan nama pengguna.
* Django menggunakan *cookie* sesi untuk memverifikasi identitas pengguna saat mereka melakukan permintaan ke aplikasi web.

Django juga menggunakan *cookie* untuk menyimpan preferensi pengguna. Misalnya, Django dapat menggunakan *cookie* untuk menyimpan preferensi bahasa pengguna atau preferensi tampilan.
<br>
<br>

#### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
*Jawab:* <br>
Penggunaan cookies tidak aman secara default dalam pengembangan web. Cookie dapat menjadi kerentanan keamanan jika tidak digunakan dengan benar.

Berikut adalah beberapa risiko potensial yang harus diwaspadai saat menggunakan cookies:
* **Risiko Keamanan Cookie**: Jika cookies digunakan untuk menyimpan data sensitif seperti token otentikasi atau informasi keuangan, mereka dapat menjadi target serangan peretas. Oleh karena itu, penting untuk mengenkripsi atau melindungi cookies yang berisi data sensitif, seperti dengan menggunakan HTTPS.
* **Cross-Site Scripting (XSS)**: Jika aplikasi Anda rentan terhadap serangan XSS, peretas dapat mencoba mencuri cookies pengguna. Mereka dapat menginjeksi kode berbahaya yang mencuri cookies atau mengirimkan cookies ke situs jahat. Penggunaan tipe cookie yang aman (secure cookie flag) dan penghindaran dari XSS adalah penting.
* **Cross-Site Request Forgery (CSRF)**: Serangan CSRF dapat memanfaatkan cookies untuk mengirim permintaan palsu dari browser pengguna yang terotentikasi. Ini dapat menyebabkan perubahan tidak diinginkan dalam status pengguna. Perlindungan CSRF seperti penggunaan token CSRF harus diterapkan.
* **Keamanan Identitas**: Cookies yang digunakan untuk autentikasi atau sesi pengguna harus diatur dengan benar untuk menghindari serangan peretasan otentikasi, seperti serangan brute force pada kata sandi. Kebijakan keamanan, seperti membatasi jumlah percobaan login, harus diterapkan.
* **Kebocoran Informasi**: Cookies bisa saja mengandung informasi yang seharusnya tidak terlihat oleh pengguna atau bahkan oleh aplikasi lain pada domain yang sama. Menerapkan aturan kebijakan SameSite pada cookies adalah penting untuk mengontrol perilaku mereka.
* **Privasi Pengguna**: Pengguna memiliki hak privasi, dan penyimpanan cookies yang berlebihan atau pelacakan yang tidak diinginkan dapat melanggar privasi pengguna. Penting untuk mengikuti praktik-praktik terbaik dalam hal privasi dan peraturan yang berlaku seperti GDPR.

Untuk mengurangi risiko keamanan saat menggunakan cookies, Anda dapat menerapkan langkah-langkah berikut:
* **Enkripsi cookie**: Enkripsi cookie akan membuat data yang disimpan dalam cookie tidak dapat dibaca oleh orang lain.
* **Validasi cookie**: Validasi cookie akan membantu memastikan bahwa cookie yang diterima dari browser pengguna adalah cookie yang valid.
* **Penggunaan cookie sesi**: Cookie sesi hanya akan disimpan di browser pengguna selama sesi aktif. Cookie sesi akan dihapus saat sesi berakhir.
* **Penggunaan cookie dengan hati-hati**: Hanya simpan informasi yang diperlukan dalam cookie.

Berikut adalah beberapa tips tambahan untuk meningkatkan keamanan cookie:
* **Gunakan cookie dengan protokol HTTPS**. HTTPS akan mengenkripsi komunikasi antara browser pengguna dan server web.
* **Setel masa berlaku cookie dengan bijak**. Masa berlaku cookie yang lebih pendek akan mengurangi risiko cookie yang dicuri.
* **Gunakan cookie dengan domain yang tepat**. Hanya izinkan cookie dari domain yang Anda percayai untuk mengakses data dalam cookie.

Dengan mengikuti langkah-langkah tersebut, dapat membantu kita untuk mengurangi risiko keamanan saat menggunakan cookies dalam pengembangan web.
<br>
<br>
