<h1>Membuat Program Data Menggunakan dictionary</h1>

     1. membuat input menu berupa " Tambah data " " Ubah data " " lihat data " " cari data " " hapus data " " keluar program "
        
        a = input(">>(L)lihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
        
    2. jika user menginput ' t ' untuk " tambah data " maka user bisa memasukan data berupa Nama, Nim, Nilai tugas, nilai uts,
       Nilai uas, dan nilai akhir di ambil dari 30% nilai tugas, 35% nilai uts, 35% nilai Uas.
       
        elif a.lower() == 't':
        print("=======Tambah Data===")
        nama=input('> Nama                :  ')
        nim=input('> Nim                 :  ')
        tugas=float(input('> masukan nilai tugas :  '))
        uts=float(input('> masukan nilai uts   :  '))
        uas=float(input('> masukan nilai uas   :  '))
        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir
      
    3. jika user menginputkan ' u ' untuk " ubah data " maka user bisa merubah data yang sudah di inputkan sebelumnya
        
        elif a.lower() == 'u':
        print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim = input('Nim                 :  ')
            tugas = float(input('masukan nilai tugas :  '))
            uts = float(input('masukan nilai uts   :  '))
            uas = float(input('masukan nilai uas   :  '))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
   
    4. jika user menginputkan ' l ' untuk " lihat data " maka user dapat melihat data yang sudah di input sebelumnya
   
       elif a.lower() == 'l':
        print('========================================= DAFTAR MAHASISWA ==============================================')
        print("======================================================================================================== ")
        print("|   NO   |      NAMA      |    NIM     |     TUGAS     |     UTS     |       UAS      |      AKHIR     | ")
        print("======================================================================================================== ")
        i=0
        for x in data.items():
            i+=1
            print("| {6:4}  |  {0:13s} | {1:9s} | {2:12}  | {3:12} | {4:12}  |  {5:12} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))

            print("========================================================================================================")

        else:
            print("====================================== Tidak Ada Data lagi =============================================")

   
    5. jika user menginputkan ' c ' untuk " cari data " maka user dapat mencari data dengan memasukan nama yang sesuai dengan 
       nama inputan sebelumnya dan otomatis akan di tampilkan 
       
       elif a.lower() == 'c':
        print('===cari data mahasiswa===')
        nama=input('Masukan Nama :  ')
        if nama in data.keys():
            print("Datanya", nama,"adalah {0}".format( data[nama]))
        else:
            print("=======================================Tidak Ada Data==========================================")
      
    6. jika user menginputkan ' h ' untuk " Hapus data " maka user dapat menghapus data dengan memasukan nama yang sesuai dengan
       nama inputan sebelumnya
       
       elif a.lower() == 'h':
        print('====hapus data mahasiswa====')
        nama=input('nama :  ' )
        if nama in data.keys():
            del data[nama]
        else:
            print("=======================================Tidak Ada Data==========================================")
            
     7. jika user menginputkan ' k ' untuk " keluar program " maka akan keluar dari program
    
8. Flowchart nya

   ![Screenshot_2019-12-07-23-15-53-486_com drawexpress lite](https://user-images.githubusercontent.com/56831922/70377525-062a5a00-1948-11ea-9bde-2f2f3d06d20e.png)
