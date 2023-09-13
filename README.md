# Tugas 2: Implementasi *Model-View-Template* (MVT) pada Django
### Ramadhan Andika Putra (2206081976) - PBP A <br>

#### Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step*!
>> #### [ Membuat sebuah proyek Django baru ]
>> Untuk membuat sebuah proyek Django baru, tentunya saya harus menyiapkan sebuah direktori baru terlebih dahulu. Direktori tersebut saya beri nama 'pachill-market' sesuai dengan nama aplikasi yang akan saya buat. Lalu, saya harus menyiapkan dan menginstal beberapa *depedencies* yang ditambahkan ke berkas *requierements.txt* agar aplikasi yang saya buat dapat berfungsi. Tak lupa, saya menggunakan *virtual environment* untuk membantu mengisolasi *package* serta *dependencies* dari aplikasi sehingga tidak bertabrakan dengan versi lain yang mungkin terdapat pada laptop saya.
>>
>> Setelah itu, saya melakukan konfigurasi proyek dengan mengizinkan akses dari semua host, yang akan memungkinkan aplikasi diakses secara luas. Lalu, saya mencoba menjalankan servernya dengan perintah python manage.py runserver dan memeriksa hasilnya di http://localhost:8000/. Yang terakhir, saya membuat repositori baru bernama 'pachill-market' dan menginisiasi direktori shopping_list sebagai repositori Git. Lalu, saya mengunggah direktori lokal saya ke repositori GitHub menggunakan add, commit, push.

>> #### [ Membuat aplikasi dengan nama *main* pada proyek tersebut ]
>> Untuk membuat sebuah aplikasi *main* pada proyek 'pachill-market' yang telah kita buat sebelumnya, kita dapat menjalankan perintah *python manage.py startapp main* untuk membuat sebuah aplikasi baru.
<br>

#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara *urls.py*, *views.py*, *models.py*, dan berkas *html*!
![BaganTugas2](https://github.com/adhan-857/pachill-market/assets/119088782/3c6ddefd-aabb-40fe-9262-4a2d3a7fc3b6)
Alur sebuah *request client* ke web aplikasi berbasis Django beserta responnya menurut bagan tersebut adalah sebagai berikut:
* Pertama, *request* yang masuk ke dalam server Django akan diproses melalui *urls.py* untuk diteruskan ke *views.py* yang kita definisikan untuk memproses permintaan tersebut.
* Apabila terdapat proses yang membutuhkan keterlibatan *database*, maka nantinya *views.py* akan memanggil *query* ke *models.py* dan *database* akan mengembalikan hasil dari *query* tersebut ke *views.py*.
* Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan pada *template.py* sebelum akhirnya HTML tersebut dikembalikan ke *client* sebagai respons.
<br>

#### Jelaskan mengapa kita menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?
*Virtual environment* adalah alat yang digunakan untuk membuat lingkungan Python virtual yang terisolasi. *Virtual environment* ini berguna untuk mengisolasi *package* serta *dependencies* dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputermu. Di sini, kita bisa membangun sebuah website Python, menginstall PIP dan berbagai *packages* di dalamnya tanpa bisa diakses oleh website Python lain.

Untuk menjawab apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*? *Jawabannya adalah ya*, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*. Namun, akan ada beberapa resiko yang harus kita waspadai, seperti:
* Aplikasi mungkin tidak kompatibel satu sama lain. Jika kita mengembangkan beberapa aplikasi web dengan Django, dan aplikasi tersebut menggunakan versi Python atau *library* atau *package* yang berbeda, maka aplikasi tersebut mungkin tidak kompatibel satu sama lain.
* Aplikasi mungkin mengalami masalah. Jika pustaka yang kita instal tidak kompatibel dengan *library* atau *package* lain, maka aplikasi kita mungkin akan mengalami masalah.
* Pengelolaan *library* dan *package* menjadi lebih sulit. Kita harus berhati-hati saat menginstal *library* atau *package* baru, karena *library* atau *package* tersebut mungkin akan mengganggu *library* dan *package* lain yang sudah kita instal.

Secara umum, penggunaan virtual environment sangat dianjurkan untuk pengembangan aplikasi web berbasis Django. *Virtual environment* dapat membantu kita untuk menghindari masalah-masalah yang dapat terjadi jika kita tidak menggunakan *virtual environment*.
<br>

#### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
Jawab
