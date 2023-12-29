# NAMA: YOGA SAPUTRA
# NIM : 411222034
# PROGRAM SISTEM INFORMASI PENERBANGAN

# INISIALISASI LIST
data_penerbangan = [] # list global kosong untuk menyimpan seluruh data penerbangan

# FUNGSI MENAMBAHKAN PENERBANGAN
def tambah_penerbangan(maskapai, no_pen, kota_asal, ban_asal, kota_tujuan, ban_tujuan, waktu): # fungsi tambah_penerbangan dengan  7 parameter maskapai, no_pen, kota_asal, ban_asal, kota_tujuan, ban_tujuan, waktu
    #INISIALISASI TUPLE
    penerbangan_baru = (maskapai, no_pen, kota_asal, ban_asal, kota_tujuan, ban_tujuan, waktu) # membuat tuple penerbangan_baru dengan nilai sama dengan parameter
    data_penerbangan.append(penerbangan_baru) #menambahkan tuple ke dalam list data_penerbangan
    print()
    print("Notifikasi!") #notifikasi
    print("----------")
    print(f"Penerbangan Maskapai {maskapai} Nomor {no_pen} Dari {kota_asal}, {ban_asal} Ke {kota_tujuan} , {ban_tujuan} Pada Pukul {waktu} Berhasil Ditambahkan ") #output hasil penambahan penerbangan dengan format tertentu
    print()

# FUMGSI PENCARIAN PENERBANGAN
def cari_penerbangan(cari, kriteria): #funsi cari_penerbangan dengan 2 parameter cari, kriteria / index kolom
    hasil_pencarian = [penerbangan for penerbangan in data_penerbangan if penerbangan[kriteria].lower() == cari.lower()] #pembuatan list comprehension hasil_pencarian dengan kodisi jika kriteria sama dengan cari dan looping dilakukan pada data_penerbangan
    return hasil_pencarian # nilai kembali dari hasil_pencarian yang memenuhi kriteria

# FUNGSI MENAMPILKAN INFORMASI PENERBANGAN
def tampilkan_semua_penerbangan():
    if len(data_penerbangan) > 0: #kondisi mengecek data_penerbangan mengunakan len panjang/jumlah data dalam data_penerbangan
        print("=====================") # jika benar
        print("INFORMASI PENERBANGAN")
        print("=====================") # mencetak header atau judul untuk informasi penerbangan yang akan ditampilkan sesuai format
        print("-" * 150)
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan"))
        print("-" * 150)
        #LOOPING DATA_PENERBANGAN
        for data in data_penerbangan: # dilakukan iterasi melalui setiap tuple di dalam data_penerbangan.
            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data)) # Untuk setiap tuple, informasinya dicetak sesuai dengan format yang telah ditentukan sebelumnya. Format ini sesuai dengan setiap kolom yang diberikan dalam tuple.
        print("-" * 150)

    else:# jika salah
        print("Notifikasi!") #notifikasi
        print("----------")
        print("Tidak ada informasi penerbangan yang tersimpan.") #mencetak notifikasi tidak ada data informasi penerbangan yang tersimpan
    print()

# LOOPING MENU
while True: # menu akan terus looping
  # MENU UTAMA
  print("==============================") # header menu utama
  print(" SISTEM INFORMASI PENERBANGAN ")
  print("==============================")
  print()
  print(" 1. Menambahkan Informasi Penerbangan")  # pilihan menu 1
  print(" 2. Mencari Informasi Penerbangan")      # pilihan menu 2
  print(" 3. Menampilkan Informasi Penerbangan")  # pilihan menu 3
  print(" 4. Keluar")                             # pilihan menu 4
  print()
  # INPUT MENU UTAMA
  pilih = int(input("Masukan Pilihan [1,2,3,4] : ")) # user input untuk pilihan menu
  # LOGIKA PENCABANGAN
  if pilih == 1 :
    # MENU PENAMBAHAN
    print("---------------------------------")
    print("Menambahkan Informasi Penerbangan")
    print("---------------------------------")
    maskapai = input("Nama Maskapai \t \t : ") # user input maskapai
    no_pen = input("Nomor Penerbangan \t : ")  # user input no penerbangan
    kota_asal = input("Kota Asal \t \t : ")     # user input kota asal
    ban_asal = input("Bandara Asal \t \t : ")   # user input bandara asal
    kota_tujuan = input("Kota Tujuan \t \t : ")   # user input kota tujuan
    ban_tujuan = input("Bandara Tujuan \t \t : ")   # user input bandara tujuan
    waktu = input ("Waktu Keberangkatan \t : ")   # user input waktu
    # Memanggil Fungsi tambah_penerbangan dan parameter sesuai variable
    tambah_penerbangan(maskapai, no_pen, kota_asal, ban_asal, kota_tujuan, ban_tujuan, waktu)
  elif pilih == 2:
     # MENU PENCARIAN
        print("------------------------------") #header menu pencarian
        print("Mencari Informasi Penerbangan")
        print("------------------------------")
        print(" 1. Cari dengan Maskapai")           # pilihan cari 1
        print(" 2. Cari dengan Nomor penerbangan")  # pilihan cari 2
        print(" 3. Cari dengan Kota Asal")          # pilihan cari 3
        print(" 4. Cari dengan Bandara Asal")       # pilihan cari 4
        print(" 5. Cari dengan Kota Tujuan")        # pilihan cari 5
        print(" 6. Cari dengan Bandara Tujuan")     # pilihan cari 6
        print()
        #INPUT MENU PENCARIAN
        cari_menu = int(input("Masukan Pilihan [1,2,3,4,5,6] : "))  # user input untuk pilihan pencarian

        if cari_menu == 1:
            maskapai_cari = input("Masukkan Nama Maskapai: ")  # user input nama maskapai
            hasil_cari = cari_penerbangan(maskapai_cari, 0) # pemanggilan fungsi cari_penerbangan dengan parameter maskapai, kriteria idx kolom 0 dan hasil akan di tampung di variable hasil_cari
            if len(hasil_cari) > 0: # cek kondisi jika hasil pencarian di temukan
                print("===============================") # jika benar  cetak header pencarian
                print("HASIL PENCARIAN DENGAN MASKAPAI")
                print("===============================")
                print("-" * 150)
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan")) #cetak header format
                print("-" * 150)
                # LOOPING HASIL_CARI
                for data in hasil_cari: #dilakukan iterasi di dalam  hasil_cari
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data)) # mencetak data yang terdapat dalam hasil_cari dengan mengunakan format
                print("-" * 150)
            else:# jikasalah
              print()
              print("Notifikasi!") #cektak notifikasi
              print("----------")
              print("Penerbangan tidak ditemukan.")
              print()

        elif cari_menu == 2:
            nopenerbangan_cari = input("Masukkan Nomor Penerbangan: ")  # user input no penerbangan
            hasil_cari = cari_penerbangan(nopenerbangan_cari, 1) # pemanggilan fungsi cari_penerbangan dengan parameter nopenerbangani, kriteria idx kolom 1 dan hasil akan di tampung di variable hasil_cari
            if len(hasil_cari) > 0:  # cek kondisi jika hasil pencarian di temukan
                print("========================================") # jika benar  cetak header pencarian
                print("HASIL PENCARIAN DENGAN NOMOR PENERBANGAN")
                print("========================================")
                print("-" * 150)
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan")) #cetak header format
                print("-" * 150)

                for data in hasil_cari:  #dilakukan iterasi di dalam  hasil_cari
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data)) # mencetak data yang terdapat dalam hasil_cari dengan mengunakan format
                print("-" * 150)
            else: #jikasalah
              print()
              print("Notifikasi!")  #cektak notifikasi
              print("----------")
              print("Penerbangan tidak ditemukan.")
              print()

        elif cari_menu == 3:
            kotaasal_cari = input("Masukkan Kota Asal : ") # user input kota asal
            hasil_cari = cari_penerbangan(kotaasal_cari, 2)  # pemanggilan fungsi cari_penerbangan dengan parameterkotaasal, kriteria idx kolom 2 dan hasil akan di tampung di variable hasil_cari
            if len(hasil_cari) > 0:  # cek kondisi jika hasil pencarian di temukan
                print("================================")  # jika benar  cetak header pencarian
                print("HASIL PENCARIAN DENGAN KOTA ASAL")
                print("================================")
                print("-" * 150)
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan"))  #cetak header format
                print("-" * 150)

                for data in hasil_cari:  #dilakukan iterasi di dalam  hasil_cari
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data))  # mencetak data yang terdapat dalam hasil_cari dengan mengunakan format
                print("-" * 150)
            else:#jikasalah
              print()
              print("Notifikasi!")  #cektak notifikasi
              print("----------")
              print("Penerbangan tidak ditemukan.")
              print()

        elif cari_menu == 4:
            banasal_cari = input("Masukkan Bandara Asal: ")  # user input bandara asal
            hasil_cari = cari_penerbangan(banasal_cari, 3)  # pemanggilan fungsi cari_penerbangan dengan parameter banasal, kriteria idx kolom 3 dan hasil akan di tampung di variable hasil_cari
            if len(hasil_cari) > 0:  # cek kondisi jika hasil pencarian di temukan
                print("===================================") # jika benar  cetak header pencarian
                print("HASIL PENCARIAN DENGAN BANDARA ASAL")
                print("===================================")
                print("-" * 150)
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan"))  #cetak header format
                print("-" * 150)

                for data in hasil_cari:  #dilakukan iterasi di dalam  hasil_cari
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data))  # mencetak data yang terdapat dalam hasil_cari dengan mengunakan format
                print("-" * 150)
            else: #jikasalah
              print()
              print("Notifikasi!") #cektak notifikasi
              print("----------")
              print("Penerbangan tidak ditemukan.")
              print()

        elif cari_menu == 5:
            kotu_cari = input("Masukkan Kota Tujuan: ") # user input kota tujuan
            hasil_cari = cari_penerbangan(kotu_cari, 4)  # pemanggilan fungsi cari_penerbangan dengan paramete kotu, kriteria idx kolom 4 dan hasil akan di tampung di variable hasil_cari
            if len(hasil_cari) > 0:  # cek kondisi jika hasil pencarian di temukan
                print("==================================")  # jika benar  cetak header pencarian
                print("HASIL PENCARIAN DENGAN KOTA TUJUAN")
                print("==================================")
                print("-" * 150)
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan"))   #cetak header format
                print("-" * 150)

                for data in hasil_cari:  #dilakukan iterasi di dalam  hasil_cari
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data))  # mencetak data yang terdapat dalam hasil_cari dengan mengunakan format
                print("-" * 150)
            else: #jikasalah
              print()
              print("Notifikasi!")  #cektak notifikasi
              print("----------")
              print("Penerbangan tidak ditemukan.")
              print()

        elif cari_menu == 6:
            batu_cari = input("Masukkan Bandara Tujuan: ")  # user input bandara tujuan
            hasil_cari = cari_penerbangan(batu_cari, 5) # pemanggilan fungsi cari_penerbangan dengan paramete batu, kriteria idx kolom 5 dan hasil akan di tampung di variable hasil_cari
            if len(hasil_cari) > 0:  # cek kondisi jika hasil pencarian di temukan
                print("=====================================")  # jika benar  cetak header pencarian
                print("HASIL PENCARIAN DENGAN BANDARA TUJUAN")
                print("=====================================")
                print("-" * 150)
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Maskapai", "Nomor Penerbangan", "Kota Asal", "Bandara Asal", "Kota Tujuan", "Bandara Tujuan", "Waktu Keberangkatan")) #cetak header format
                print("-" * 150)

                for data in hasil_cari:  #dilakukan iterasi di dalam  hasil_cari
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*data))   # mencetak data yang terdapat dalam hasil_cari dengan mengunakan format
                print("-" * 150)
            else:  #jikasalah
              print()
              print("Notifikasi!") #cektak notifikasi
              print("----------")
              print("Penerbangan tidak ditemukan.")
              print()

        else: #jika pilihan tidak di temukan
          print()
          print("Notifikasi!") #cektak notifikasi
          print("----------")
          print("Pilihan Tidak Di temukan.")
          print()

  elif pilih == 3:
    print("---------------------------------") #cetak header menu menampilan informasi penerbangan
    print("Menampilkan Informasi Penerbangan")
    print("---------------------------------")
    tampilkan_semua_penerbangan() #pemanggilan fungsi tampilkan_semua_penerbanga

  elif pilih == 4:
    break # Lopping menu akan berhenti dan program selesai
  else: # jika pilihan tidak di temukan
    print()
    print("Notifikasi!") #cektak notifikasi
    print("----------")
    print("Pilihan Tidak Di temukan.")
    print()
