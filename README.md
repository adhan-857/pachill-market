# Tugas 6: JavaScript dan Asynchronous JavaScript
### Ramadhan Andika Putra (2206081976) - PBP A <br>
#### Link: http://ramadhan-andika-tugas.pbp.cs.ui.ac.id/

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
<br>
<br>
