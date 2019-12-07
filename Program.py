print("=======================  program input data =========================")
data={}
while True:
    print("")
    a = input(">>(L)lihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if a.lower() == 'k':
        break

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

    elif a.lower() == 't':
        print("=======Tambah Data===")
        nama=input('> Nama                :  ')
        nim=input('> Nim                 :  ')
        tugas=float(input('> masukan nilai tugas :  '))
        uts=float(input('> masukan nilai uts   :  '))
        uas=float(input('> masukan nilai uas   :  '))
        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir

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

        else:
            print("=======================================Tidak Ada Data==========================================")

    elif a.lower() == 'h':
        print('====hapus data mahasiswa====')
        nama=input('nama :  ' )
        if nama in data.keys():
            del data[nama]
        else:
            print("=======================================Tidak Ada Data==========================================")
    elif a.lower() == 'c':
        print('===cari data mahasiswa===')
        nama=input('Masukan Nama :  ')
        if nama in data.keys():
            print("Datanya", nama,"adalah {0}".format( data[nama]))
        else:
            print("=======================================Tidak Ada Data==========================================")


    else :
        print('============harap pilih menu yang tersedia===========')
