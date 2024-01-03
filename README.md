# Tugas 2: Implementasi *Model-View-Template* (MVT) pada Django
### Ramadhan Andika Putra (2206081976) - PBP A <br>

*[ Link web: [https://pachill-market.adaptable.app/main/](http://ramadhan-andika-tugas.pbp.cs.ui.ac.id/) ]*

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Membuat sebuah proyek Django baru ]
>> Untuk membuat sebuah proyek Django baru, tentunya saya harus menyiapkan sebuah direktori baru terlebih dahulu. Direktori tersebut saya beri nama 'pachill-market' sesuai dengan nama aplikasi yang akan saya buat. Lalu, saya harus menyiapkan dan menginstal beberapa *depedencies* yang ditambahkan ke berkas *requierements.txt* agar aplikasi yang saya buat dapat berfungsi. Tak lupa, saya menggunakan *virtual environment* untuk membantu mengisolasi *package* serta *dependencies* dari aplikasi sehingga tidak bertabrakan dengan versi lain yang mungkin terdapat pada laptop saya.
>>
>> Setelah itu, saya melakukan konfigurasi proyek dengan mengizinkan akses dari semua host, yang akan memungkinkan aplikasi diakses secara luas. Lalu, saya mencoba menjalankan servernya dengan perintah *python manage.py runserver8 dan memeriksa hasilnya di *http://localhost:8000/*. Yang terakhir, saya membuat repositori baru bernama 'pachill-market' dan menginisiasi direktori *shopping_list* sebagai repositori Git. Lalu, saya mengunggah direktori lokal saya ke repositori GitHub menggunakan *add*, *commit*, *push*.
<br>

>> #### [ Membuat aplikasi dengan nama *main* pada proyek tersebut ]
>> Untuk membuat sebuah aplikasi *main* pada proyek 'pachill-market' yang telah kita buat sebelumnya, kita dapat menjalankan perintah *python manage.py startapp main* untuk membuat sebuah struktur baru untuk aplikasi yang akan kita buat. Lalu, saya mendaftarkan aplikasi *main* ke dalam proyek *pachill market* milik saya. Setelah itu, saya mengimplementasikan Template dan Model dasar untuk proyek aplikasi saya.
<br>

>> #### [ Melakukan routing pada proyek agar dapat menjalankan aplikasi main ]
>> Untuk melakukan konfigurasi *outing* URL Aplikasi *main*, saya menambahkan rute URL dalam *urls.py* proyek untuk menghubungkannya ke tampilan *main* milik saya. Lalu, saya mengimpor fungsi *include* dari *django.urls* untuk mengimpor rute URL dari aplikasi main ke dalam berkas *urls.py* proyek. Setelah itu, saya menambahkan rute Path URL *'main/'* agar dapat diarahkan ke rute yang didefinisikan dalam berkas *urls.py* aplikasi *main*.
<br>

>> #### [ Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib ]
>> Saya mengubah berkas *models.py* yang terdapat di dalam direktori aplikasi main untuk mendefinisikan model baru sesuai dengan yang diminta pada tugas. Untuk detailnya, model yang saya buat memiliki atribut *name*, *date_added*, *price*, *amount*, dan *description*. Setiap atribut memiliki tipe data yang sesuai dengan yang diminta pada tugas seperti *CharField*, *IntegerField*, dan *TextField*.
<br>

>> #### [ Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML ]
>> Untuk menghubungkan *view* dengan *template*, saya mengimpor fungsi render dari modul django.shortcuts untuk me-render tampilan HTML dengan menggunakan data yang diberikan. Setelah itu, saya mengubah template *main.html* agar dapat menampilkan data yang telah diambil dari model (agar dapat menampilkan nilai dari variabel yang telah didefinisikan dalam context).
<br>

>> #### [ Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. ]
>> Untuk membuat sebuah routing pada *urls.py* aplikasi main, saya membuat berkas *urls.py* di dalam direktori *main* ntuk mengatur rute URL yang terkait dengan aplikasi *main*. Nantinya, fungsi *show_main* dari modul *main.views* akan dijadikan sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
<br>

>> #### [ Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat ]
>>  Untuk me-*deploy* ke Adaptable, saya memilih repositori proyek *pachill_market* sebagai basis aplikasi yang akan di-*deploy* dan *branch 'main'* sebagai *deployment branch*. Karena dalam membuat proyeknya sebagian besar menggunakan bahasa Python, maka saya memilih *Python App Template* sebagai *template deployment*. yang terakhir sebelum melakukan *deployment*, saya memasukkan nama aplikasi saya 'pachill market' agar daapt digunakan juga sebagai nama *domain* situs web aplikasi saya.
<br>
<br>

#### Buatlah bagan yang berisi request *client* ke *web* aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara *urls.py*, *views.py*, *models.py*, dan berkas *html*!
![Bagan_Tugas2](https://github.com/adhan-857/pachill-market/assets/119088782/66ae4f1b-7bcc-4109-bf46-a8dbfbc3cf49)
Alur sebuah *request client* ke web aplikasi berbasis Django beserta responnya menurut bagan tersebut adalah sebagai berikut:
* Pertama, *request* yang masuk ke dalam server Django akan diproses melalui *urls.py* untuk diteruskan ke *views.py* yang kita definisikan untuk memproses permintaan tersebut.
* Apabila terdapat proses yang membutuhkan keterlibatan *database*, maka nantinya *views.py* akan memanggil *query* ke *models.py* dan *database* akan mengembalikan hasil dari *query* tersebut ke *views.py*.
* Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan pada *template* sebelum akhirnya HTML tersebut dikembalikan ke *client* sebagai respons.
<br>
<br>

#### Jelaskan mengapa kita menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?
*Virtual environment* adalah alat yang digunakan untuk membuat lingkungan Python virtual yang terisolasi. *Virtual environment* ini berguna untuk mengisolasi *package* serta *dependencies* dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputermu. Di sini, kita bisa membangun sebuah website Python, menginstall PIP dan berbagai *packages* di dalamnya tanpa bisa diakses oleh website Python lain.

Untuk menjawab apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*? *Jawabannya adalah ya*, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, akan ada beberapa resiko yang harus kita waspadai, seperti:
* Aplikasi mungkin tidak kompatibel satu sama lain. Jika kita mengembangkan beberapa aplikasi web dengan Django, dan aplikasi tersebut menggunakan versi Python atau *library* atau *package* yang berbeda, maka aplikasi tersebut mungkin tidak kompatibel satu sama lain.
* Aplikasi mungkin mengalami masalah. Jika pustaka yang kita instal tidak kompatibel dengan *library* atau *package* lain, maka aplikasi kita mungkin akan mengalami masalah.
* Pengelolaan *library* dan *package* menjadi lebih sulit. Kita harus berhati-hati saat menginstal *library* atau *package* baru, karena *library* atau *package* tersebut mungkin akan mengganggu *library* dan *package* lain yang sudah kita instal.

Secara umum, penggunaan virtual environment sangat dianjurkan untuk pengembangan aplikasi web berbasis Django. *Virtual environment* dapat membantu kita untuk menghindari masalah-masalah yang dapat terjadi jika kita tidak menggunakan *virtual environment*.
<br>
<br>

#### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
Jawab
MVC atau yang biasa disebut *Model-View-Controller* adalah suatu model yang seringkali digunakan oleh para pengembang *software*. Pola ini membagi aplikasi menjadi tiga komponen utama:
* Model: Komponen ini bertanggung jawab untuk mengatur dan mengelola data dari aplikasi
* *View*: Komponen ini bertanggung jawab untuk menangani logika presentasi dan menampilkan data ke pengguna.
* *Controller8: Komponen ini bertanggung jawab untuk menerima input dari pengguna dan mengontrol aliran data antara model dan view.

MVT adalah singkatan dari *Model-View-Template*. MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan *web* untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang *web* untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
* Model: Komponen ini bertanggung jawab untuk mengatur dan mengelola data dari aplikasi
* *View*: Komponen ini bertanggung jawab untuk menangani logika presentasi dan menampilkan data ke pengguna.
* *Template*: Komponen ini bertanggung jawab untuk untuk mengatur tampilan atau antarmuka pengguna. Template memisahkan kode HTML dari logika aplikasi.

MVVM adalah singkatan dari *Model-View-ViewModel*. MVVM merupakan gabungan dari MVC dan MVP. Pola yang digunakan berdasarkan gabungan dari MVC dan MVP mencoba untuk lebih jelas dalam memisahkan pengembangan *UI* dari logika bisnis dan perilaku dalam aplikasi.
* Model: Komponen ini bertanggung jawab untuk mengatur dan mengelola data dari aplikasi
* *View*: Komponen ini bertanggung jawab untuk menangani logika presentasi dan menampilkan data ke pengguna.
* *ViewModel*: Komponen ini di satu sisi adalah abstraksi dari *View*, lalu di sisi yang lain sebagai penyedia pembungkus data model untuk ditautkan. *ViewModel* terdiri dari Model yang diubah menjadi *View*, dan berisi perintah yang dapat digunakan oleh *View* untuk mempengaruhi Model.

Di bawah ini adalah perbedaan dari ketiganya:
| Karakteristik    |     MVC          |      MVT         |      MVVM        |
| ---------------- | ---------------- | ---------------- | ---------------- |
| Komponen         | Model, View, Controller                         | Model, View, Template                 | Model, View, ViewModel             |
| Peran Controller | Mengontrol aliran data antara model dan *view*  | Diintegrasikan ke dalam *view*        | Jembatan antara *view* dan model   |
| Kelebihan        | Mudah dipahami dan diimplementasikan            | Mudah digunakan untuk aplikasi kecil  | Mendukung dua arah *data binding*  |
| Kekurangan       | Tidak cocok untuk aplikasi besar                | Tidak cocok untuk aplikasi kompleks   | Lebih kompleks daripada MVC        |
<br>
<br>

# Tugas 3: Implementasi *Form* dan *Data Delivery* pada Django 
### Ramadhan Andika Putra (2206081976) - PBP A <br>

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Membuat input *form* untuk menambahkan objek model pada app sebelumnya. ]
>> Pertama, saya membuat berkas baru pada direktori *main* dengan nama *forms.py* agar dapat menerima data baru produk yang akan dibeli. Saya menambahkan *fields = ["name_1", "name_2", "price", "description"]* sebagai *field* dari model *Product* yang digunakan untuk form. Saya menambahkan *field* baru bernama *name_2* karena *web app* saya memerlukan 2 buah *CharField* untuk
>>
>> Setelah itu, saya membuat *function create_product* pada berkas *views.py* yang berada pada folder *main* agar dapat menerima parameter *request* serta agar dapat menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-*submit* dari form. Lalu, saya meng-*import* fungsi *create_product* tersebut ke dalam berkas *urls.py* pada folder *main* serta menambahkan *path url* ke dalam *urlpatterns* untuk mengakses fungsi yang telah di-*import* sebelumnya.
>>
>> Langkah selanjutnya, saya membuat berkas HTML baru dengan nama *create_product.html* pada direktori *main/templates* agar dapat menampilkan *fields form* yang sudah dibuat sebelumnya. Lalu yang terakhir, saya mengedit *main.html* agar dapat menampilkan data produk dalam bentuk *table* serta tombol "Catat Transaksi Baru" yang akan *redirect* ke halaman form.
<br>

>> #### [ Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by* ID, dan JSON *by* ID. ]
>> Pertama, saya mengedit *function show_main* pada berkas *views.py* agar dapat mengambil seluruh object *Product* yang tersimpan pada *database*. Setelah itu, saya meng-*import HttpResponse* dan *Serializer* pada berkas *views.py* yang berada pada folder *main*. Lalu, saya membuat fungsi baru yang menerima parameter *request* dengan nama *show_xml* dan *show_json* dengan sebuah variabel di dalamnya yang menyimpan hasil *query* dari seluruh data yang ada pada *Product*.
>>
>> Setelah itu, saya membuat sebuah fungsi baru yang menerima parameter *request* dan *id* dengan nama *show_xml_by_id* dan *show_json_by_id* dengan sebuah variabel di dalamnya yang menyimpan hasil *query* dari data dengan id tertentu yang ada pada *Product*. Tak lupa, saya menambahkan *return function* berupa *HttpResponse* yang berisi parameter data hasil *query* yang sudah diserialisasi.
<br>

>> #### [ Membuat *routing* URL untuk masing-masing views yang telah ditambahkan pada poin 2 ]
>> Saya meng-*import* seluruh fungsi *views* yang tadi telah saya buat ke dalam berkas *urls.py* yang ada pada folder *main* serta menambahkan *path url* ke dalam *urlpatterns* untuk mengakses fungsi yang sudah diimpor tadi.
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
*Jawab:*
<br>

-HTML- <br>
<img width="960" alt="SS_HTML" src="https://github.com/adhan-857/pachill-market/assets/119088782/0a0b9e09-1d6d-468a-a178-1b7460c6a5d2">
<br>

-XML- <br>
<img width="960" alt="SS_XML" src="https://github.com/adhan-857/pachill-market/assets/119088782/323381d9-091b-4f11-9765-28cfe52e8f88">

<br>
-JSON- <br>
<img width="960" alt="SS_JSON" src="https://github.com/adhan-857/pachill-market/assets/119088782/adaf8150-9ca5-4957-a988-9beb7dca8a61">
<br>
<br>

-XML *by ID*- <br>
<img width="960" alt="SS_XMLbyID" src="https://github.com/adhan-857/pachill-market/assets/119088782/6f01f62b-85b4-4724-af9a-66557497dc86">
<br>
<br>

-JSON *by ID*- <br>
<img width="960" alt="SS_JSONbyID" src="https://github.com/adhan-857/pachill-market/assets/119088782/71d12c87-e43d-4053-90ea-68261955df01">
<br>
<br>

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
<br>

# Tugas 6: JavaScript dan Asynchronous JavaScript
### Ramadhan Andika Putra (2206081976) - PBP A <br>

*[ Link web tugas: http://ramadhan-andika-tugas.pbp.cs.ui.ac.id/ ]*

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Ubahlah kode cards data item agar dapat mendukung AJAX GET. ]
>> Mengubah kode cards data item agar dapat mendukung AJAX GET melibatkan beberapa langkah. Salah satu aspek pentingnya adalah memastikan data yang diambil dari server bisa dinamis ditampilkan pada elemen HTML. Berikut cara saya mengimplementasikannya:<br>
>> <br>
>> **1) Fetch Data Dengan AJAX**<br>
>> Saya menggunakan fetch() API. Fungsi getProducts() akan mengambil data dari server dan mengembalikannya sebagai Promise.<br>
>> <img width="385" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/2372a0f3-18f4-4337-b20e-a570118ec8cd">
>> <br>
>>
>> **2) Pembuatan Card Dinamis**<br>
>> Fungsi refreshProducts() bertanggung jawab untuk membuat cards berdasarkan data yang diambil.<br>
>> <img width="560" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/b64fadbf-7e8d-4bde-8e6e-54bafbc778ac">
>> <br>
>>
>> **3) Menampilkan Data**<br>
>> Ini adalah bagian di mana saya memasukkan data ke dalam elemen HTML. Dalam kasus ini, saya menggunakan elemen dengan id product-list.
>>
>> **4) Refresh Data**<br>
>> Setiap kali ada penambahan atau pengurangan produk, saya memanggil ulang refreshProducts() untuk memperbarui tampilan.<br>
>> <img width="414" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/cadaa48d-9ca2-4265-b412-70cbc412c0e9">

<br>

>> #### [ Lakukan pengambilan task menggunakan AJAX GET. ]
>> Pada kode saya, AJAX (Asynchronous JavaScript and XML) digunakan untuk berkomunikasi antara frontend dan backend tanpa perlu memuat ulang halaman web secara keseluruhan. Dalam kasus ini, ada beberapa contoh bagaimana AJAX GET digunakan, khususnya untuk pengambilan daftar produk dari server.<br>
>> <br>
>> **1) Fungsi JavaScript untuk Melakukan AJAX GET**<br>
>> Fungsi *getProducts* adalah fungsi asinkron yang menggunakan fetch API untuk melakukan permintaan HTTP GET ke endpoint yang telah ditentukan:<br>
>> <img width="389" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/fed53a78-908b-4126-9a1e-3de22d9d02d4">
>> <br>
>>
>> **2) Menggunakan Fungsi di Dalam Fungsi Lain**<br>
>> Fungsi *getProducts* tersebut kemudian digunakan dalam fungsi *refreshProducts*:<br>
>> <img width="462" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/4f4d0a0a-5e4e-49dc-91c6-4b518c9a46b0">
>> <br>
>> * Fungsi ini pertama-tama mengosongkan elemen yang akan menampilkan daftar produk.
>> * *await getProducts();* memanggil fungsi *getProducts* dan menunggu hingga permintaan selesai. Hasil dari fungsi ini (yaitu, array dari produk) disimpan dalam variabel *products*.
>> <br>
>> 
>> **3) Menginisiasi Permintaan AJAX**<br>
>> Fungsi *refreshProducts* dijalankan untuk pertama kali di bagian bawah kode untuk memuat produk saat halaman dimuat:<br>
>> <img width="121" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/e31a7060-8453-440f-9a27-a919a64975d4">
>>
>> Dengan demikian, proses pengambilan task menggunakan AJAX GET dalam kode saya dilakukan dengan cara yang terstruktur dan asinkron, memungkinkan halaman web tetap responsif selama proses komunikasi dengan server.

<br>

>> #### [ Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item. ]
>> Saya membuat tombol "Tambah Produk by AJAX" yang berfungsi untuk membuka sebuah modal yang berisi formulir untuk menambahkan sebuah item atau produk baru. Ini adalah sebuah implementasi berbasis AJAX (Asynchronous JavaScript and XML), yang memungkinkan proses penambahan produk untuk dijalankan tanpa perlu memuat ulang halaman.
>>
>> Ketika tombol ini diklik, ia akan membuka sebuah modal *(#exampleModal)* yang berisi formulir untuk menambahkan produk. Ini adalah aksi yang dilakukan melalui atribut *data-bs-toggle* dan *data-bs-target*.
>>
>> Modal tersebut berisi formulir dengan beberapa elemen input:
>> * Nama Produk: Sebuah input tipe teks
>> * Harga Produk: Sebuah input tipe angka
>> * Jumlah Produk: Sebuah input tipe angka
>> * Deskripsi Produk: Sebuah textarea
>>
>> Formulir ini dikendalikan oleh JavaScript untuk mengambil nilai dari elemen-elemen ini dan mengirimkannya ke server.
>>
>> Dalam potongan kode JavaScript, ada beberapa fungsi penting:<br>
>> * *getProducts()*: Mengambil daftar produk saat ini dari server.
>> * *refreshProducts()*: Memperbarui tampilan daftar produk di halaman.
>> * *addProduct()*: Fungsi yang dipanggil ketika tombol "Add Product" di modal diklik.
>>
>> <br>
>> <img width="296" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/f374ac62-32e5-41b2-808f-24c35b0338d0">
>> <br>
>> Ketika tombol "Add Product" diklik, fungsi addProduct() dipanggil. Fungsi ini melakukan sebuah request POST ke URL yang ditentukan ({% url 'main:add_product_ajax' %}). Ia mengirim data dari formulir sebagai FormData. Setelah request sukses, daftar produk akan diperbarui dengan memanggil refreshProducts().

<br>

>> #### [ Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data. ]
>> Saya membuat sebuah fungsi baru pada *views.py* dengan nama *add_product_ajax* yang menerima parameter *request*. Setelah itu, saya melakukan impor *from django.views.decorators.csrf import csrf_exempt* pada berkas *views.py*. Yang terakhir, saya menambahkan dekorator *@csrf_exempt* di atas fungsi *add_product_ajax* yang sudah dibuat.<br>
>> <img width="531" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/15ed9354-2bb2-43a7-acda-abb9206866a4">


<br>

>> #### [ Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat. ]
>> saya melakukan impor fungsi *get_product_json* serta *add_product_ajax* pada berkas *urls.py* yang berada pada folder main. Lalu, saya menambahkan *path url* kedua fungsi tersebut ke dalam *urlpatterns*.<br>
>> <img width="365" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/03844a50-d2b2-44d7-8ba3-a111b2d3bb72">


<br>

>> #### [ Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/. ]
>> Pada bagian HTML di dalam modal, saya telah membuat sebuah form dengan elemen-elemen seperti input teks, input angka, dan textarea. Form ini akan digunakan untuk mengumpulkan informasi tentang produk baru yang akan ditambahkan.<br>
>> <br>
>> <img width="266" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/259af42e-e0b3-4838-bd18-30389776df5e">
>> <br>
>> Dalam form di atas, {% csrf_token %} digunakan untuk menyertakan token CSRF yang diperlukan untuk melindungi aplikasi Anda dari serangan CSRF (Cross-Site Request Forgery).
>>
>> Di dalam kode JavaScript yang saya buat, terdapat fungsi addProduct() yang dipanggil saat tombol "Add Product" pada modal ditekan. Fungsi ini mengirimkan data form ke path {% url 'main:add_product_ajax' %} menggunakan metode POST. <br>
>> <br>
>> <img width="305" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/ca28c1e8-d131-482c-b5c6-37bd189d8de6">
>> <br>
>> * Fungsi fetch() digunakan untuk mengirim permintaan POST ke path yang ditentukan.
>> * new FormData(document.querySelector('#form')) digunakan untuk mengambil data yang diisi dalam form HTML.
>> * Setelah data dikirimkan, fungsi refreshProducts() dipanggil untuk memperbarui daftar produk.
>>
>> Dengan menghubungkan form tersebut ke path {% url 'main:add_product_ajax' %} melalui JavaScript seperti di atas, kita dapat menambahkan produk baru ke dalam aplikasi web Anda secara dinamis menggunakan teknik AJAX tanpa harus me-refresh seluruh halaman.

<br>

>> #### [ Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan. ]
>> Untuk melakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan, saya menggunakan JavaScript dan teknik AJAX. Berikut adalah prosesnya:
>> 1) Pada awalnya, ada fungsi refreshProducts() yang dipanggil saat halaman dimuat atau saat ada perubahan yang memerlukan pembaruan daftar produk.
>> 2) Fungsi refreshProducts() melakukan hal-hal berikut:
>>    * Mengambil elemen HTML dengan id "product-list" yang akan digunakan untuk menampilkan daftar produk.
>>    * Mengosongkan konten dari elemen "product-list" dengan mengatur productList.innerHTML = "";. Hal ini dilakukan untuk membersihkan daftar produk yang mungkin sudah ditampilkan sebelumnya.
>> 3) Selanjutnya, fungsi ini melakukan permintaan GET ke path {% url 'main:get_product_json' %} menggunakan fetch(). Path ini mengembalikan data JSON yang berisi daftar produk terbaru.
>> 4) Setelah mendapatkan data produk dalam bentuk JSON, fungsi ini mengubah tampilan HTML dengan mengisi ulang elemen "product-list" dengan produk-produk yang baru. Ini dilakukan dengan mengonversi data JSON ke dalam HTML dan menambahkannya ke dalam cardHtmlString.
>> 5) Terakhir, hasil dari cardHtmlString diisikan kembali ke dalam elemen "product-list" dengan productList.innerHTML = ....

<br>

>> #### [ Melakukan perintah collectstatic. ]
>> Jalankan perintah collectstatic menggunakan manajer perintah Django, yaitu manage.py:<br>
>> <img width="181" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/b3d265c8-1343-456c-81c9-8f07f524bf22">
>> <br>
>> Perintah ini akan mengumpulkan semua file statis dari aplikasi saya, termasuk file CSS, JavaScript, dan gambar, dan menyalinnya ke folder "static" yang saya tentukan dalam pengaturan.
>>
>> Dengan menjalankan perintah collectstatic, saya akan memiliki semua file statis yang diperlukan untuk aplikasi saya yang akan tersedia dalam satu direktori yang siap untuk disajikan saat proyek Anda berada dalam mode produksi.


<br>
<br>

#### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
*Jawab:* <br>
Asynchronous programming dan synchronous programming adalah dua pendekatan yang berbeda dalam pemrograman komputer. Perbedaan utama antara kedua pendekatan ini adalah cara mereka menangani tugas-tugas yang berjalan secara bersamaan.

Asynchronous programming adalah pendekatan yang memungkinkan tugas-tugas berjalan secara bersamaan, tanpa menunggu tugas sebelumnya selesai. Hal ini dilakukan dengan menggunakan thread atau proses yang berbeda untuk menjalankan tugas-tugas tersebut. Asynchronous programming dapat meningkatkan kinerja aplikasi karena memungkinkan aplikasi untuk menangani lebih banyak tugas dalam waktu yang lebih singkat.

Synchronous programming adalah pendekatan yang mengharuskan tugas-tugas diselesaikan satu per satu. Hal ini dilakukan dengan menggunakan satu thread atau proses untuk menjalankan semua tugas. Synchronous programming dapat lebih mudah untuk dipahami dan ditulis, tetapi dapat mengurangi kinerja aplikasi karena aplikasi harus menunggu tugas sebelumnya selesai sebelum melanjutkan ke tugas berikutnya.
<br>

Perbedaan antara keduanya:
| Karakteristik    |     Asynchronous programming       |      Synchronous programming    |
| ---------------- | ---------------------------------- | ------------------------------- |
| Cara menangani tugas	| Tugas berjalan secara bersamaan	| Tugas diselesaikan satu per satu
| Performa	| Dapat meningkatkan kinerja	| Dapat mengurangi kinerja
| Kemudahan penggunaan	| Lebih kompleks	| Lebih mudah
| Contoh	| Web server, aplikasi real-time	| Aplikasi desktop, aplikasi batch
<br>

Asynchronous programming cocok untuk digunakan dalam aplikasi yang membutuhkan kinerja tinggi atau yang harus menangani tugas-tugas yang berjalan secara bersamaan. Beberapa contoh aplikasi yang menggunakan asynchronous programming adalah:
* Web server: Web server menggunakan asynchronous programming untuk menangani permintaan HTTP dari banyak klien secara bersamaan.
* Aplikasi real-time: Aplikasi real-time, seperti aplikasi obrolan dan game, menggunakan asynchronous programming untuk memastikan respons yang cepat.
* Aplikasi mobile: Aplikasi mobile sering kali menggunakan asynchronous programming untuk menghemat daya baterai.
<br>

Synchronous programming cocok untuk digunakan dalam aplikasi yang sederhana atau yang tidak membutuhkan kinerja tinggi. Beberapa contoh aplikasi yang menggunakan synchronous programming adalah:
* Aplikasi desktop: Aplikasi desktop, seperti pengolah kata dan spreadsheet, sering kali menggunakan synchronous programming untuk kemudahan penggunaan.
* Aplikasi batch: Aplikasi batch, seperti tugas pencadangan dan pengunduhan, sering kali menggunakan synchronous programming untuk meningkatkan kinerja.
<br>
<br>

#### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
*Jawab:* <br>
Paradigma Event-Driven Programming adalah suatu paradigma pemrograman yang terfokus pada kejadian atau "event" sebagai mekanisme utama untuk mempengaruhi eksekusi program. Dalam paradigma ini, eksekusi kode biasanya diinisiasi oleh peristiwa yang dihasilkan oleh luaran dari sistem lain, atau oleh interaksi pengguna seperti klik mouse, ketukan pada layar, dan sebagainya. Sebagai respons terhadap event tersebut, program akan menjalankan fungsi atau prosedur tertentu yang disebut sebagai "event handler" atau "callback."

Contoh penerapan Event-Driven Programming pada kode yang Anda berikan dapat ditemukan dalam fungsi AJAX yang digunakan untuk menambah atau menghapus produk. Misalnya, dalam metode add_product_ajax, sebuah event "POST request" menginisiasi eksekusi fungsi tersebut. Jika request ini berhasil, data baru akan ditambahkan ke dalam basis data, dan HTTP response akan dikembalikan. Ini adalah sebuah interaksi yang sepenuhnya digerakkan oleh event, di mana event "POST request" mengaktifkan serangkaian aksi pada server.
<br>

<img width="528" alt="image" src="https://github.com/adhan-857/pachill-market/assets/119088782/ba99f3e7-2dd5-498b-9fd3-5d0bfb77e9ca"><br>
Dalam kasus ini, paradigma Event-Driven memungkinkan program untuk menunggu dan merespons aksi dari pengguna atau sistem, daripada menjalankan urutan instruksi secara linear.
<br>
<br>

#### Jelaskan penerapan asynchronous programming pada AJAX.
*Jawab:* <br>
Asynchronous programming dalam konteks AJAX (Asynchronous JavaScript and XML) merujuk pada kemampuan untuk melakukan permintaan data dari server dan memanipulasi tampilan halaman web tanpa perlu memuat ulang seluruh halaman. Dengan AJAX, sebuah aplikasi web dapat mengirim atau menerima data dari server secara asinkron, memungkinkan untuk memperbarui bagian spesifik dari halaman web tanpa menunggu proses unduh atau unggah seluruh konten.

Secara teknis, AJAX biasanya menggunakan objek `XMLHttpRequest` atau metode fetch modern untuk melakukan permintaan HTTP asinkron. Permintaan ini bisa berjalan di latar belakang dan ketika data diterima dari server, sebuah fungsi "callback" dipanggil untuk memproses data tersebut. Selama proses ini, pengguna masih bisa berinteraksi dengan halaman, yang berarti aplikasi tetap responsif.

Sebagai contoh, dalam aplikasi toko online, ketika pengguna menambahkan item ke keranjang belanja, sebuah permintaan AJAX bisa dikirim ke server untuk memperbarui jumlah item di keranjang tanpa perlu memuat ulang seluruh halaman. Hal ini memberikan pengalaman pengguna yang lebih mulus dan efisien.

Dengan demikian, penerapan asynchronous programming melalui AJAX memungkinkan pengembangan aplikasi web yang lebih dinamis, responsif, dan efisien.
<br>
<br>

#### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
*Jawab:* <br>
Fetch API dan jQuery AJAX adalah dua teknologi yang sering digunakan untuk melakukan operasi asinkron dalam pengembangan aplikasi web. Keduanya memiliki kelebihan dan kekurangan masing-masing, dan pilihan antara keduanya seringkali tergantung pada kebutuhan spesifik proyek.

Fetch API dan jQuery AJAX adalah dua teknologi yang sering digunakan untuk melakukan operasi asinkron dalam pengembangan aplikasi web. Keduanya memiliki kelebihan dan kekurangan masing-masing, dan pilihan antara keduanya seringkali tergantung pada kebutuhan spesifik proyek.

**Fetch API:**
* **Native API**: Fetch adalah API bawaan browser, sehingga tidak memerlukan pustaka tambahan.
* **Promises-Based**: Fetch API memanfaatkan Promises, yang membuatnya lebih mudah untuk digunakan daripada callback.
* **Sederhana dan Ringkas**: Fetch biasanya lebih sederhana dan lebih mudah dipahami, khususnya untuk pengembang yang sudah terbiasa dengan sintaks modern JavaScript.
* **Fleksibilitas**: Fetch memberikan lebih banyak kontrol atas permintaan HTTP dibandingkan dengan jQuery.
* **Limited Support**: Tidak semua browser lawas mendukung Fetch API.

**jQuery AJAX:**
* **Cross-Browser Compatibility**: jQuery secara otomatis menangani kompatibilitas antar-browser, yang bisa sangat berguna jika Anda membutuhkan dukungan untuk browser lawas.
* **Rich Feature Set**: jQuery menyediakan banyak fungsi lain selain AJAX yang dapat mempercepat pengembangan.
* **Community and Plugins**: Karena sudah ada lebih lama, jQuery memiliki komunitas yang lebih besar dan lebih banyak plugin.
* **Overhead**: Jika Anda hanya membutuhkan AJAX, memasukkan seluruh pustaka jQuery bisa dianggap berlebihan.
* **Callback-Based**: Dibandingkan dengan Promises, penggunaan callback bisa membuat kode lebih sulit untuk dikelola dalam kasus tertentu.

Menurut saya, tidak ada pendapat yang objektif mengenai "yang mana yang lebih baik", karena hal tersebut sangat tergantung pada kebutuhan proyek. Jika kita membangun sebuah aplikasi modern dan tidak memerlukan dukungan untuk browser lawas, Fetch API mungkin lebih sesuai karena sintaksnya yang lebih modern dan karena ia tidak memerlukan pustaka tambahan. Sebaliknya, jika kita memerlukan kompatibilitas lintas browser atau ingin memanfaatkan fitur-fitur jQuery lainnya, maka jQuery AJAX mungkin lebih sesuai.

Oleh karena itu, penting bagi kita untuk mempertimbangkan kebutuhan dan batasan proyek sebelum memilih antara Fetch API dan jQuery AJAX.
