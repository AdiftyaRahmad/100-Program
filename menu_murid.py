import os
os.system("cls" if os.name == "nt" else "clear")

murid = []

def lihat_nama():
    if len(murid) == 0:
        print("\tTidak ada data murid.")
    else:
        print("\t", "="*31)
        print("\t\tDaftar Nama Murid")
        print("\t", "="*31)
        for i, nama in enumerate(murid):
            print(f"\t{i+1}. {nama}")

def tambah_nama():
    print()
    murid_baru = input("Inputkan nama murid baru: ")
    if murid_baru in murid:
        print("Nama sudah ada, coba masukkan nama lain.")
    else:
        murid.append(murid_baru)
        print(f"Nama {murid_baru} telah ditambahkan.")

def edit_nama():
    if len(murid) == 0:
        print("\n\tTidak ada data murid untuk diedit.")
        return
    print()
    lihat_nama()
    try:
        index = int(input("Masukkan nomor murid yang ingin diedit: ")) - 1
        if 0 <= index < len(murid):
            murid_baru = input("Inputkan nama baru: ")
            murid[index] = murid_baru
            print("Nama murid berhasil di edit.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def hapus_nama():
    if len(murid) == 0:
        print("\n\tTidak ada data murid untuk dihapus.")
        return
    print()
    lihat_nama()
    try:
        index = int(input("Masukkan nomor murid yang ingin dihapus: ")) - 1
        if 0 <= index < len(murid):
            murid_terhapus = murid.pop(index)
            print(f"Nama {murid_terhapus} berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def cari_nama():
    print()
    nama_cari = input("Inputkan nama murid yang ingin dicari: ")
    if nama_cari in murid:
        print(f"Nama {nama_cari} ditemukan.")
    else:
        print("Nama tidak ditemukan.")

def menu():
    while True:
        print("\n")
        print("\t", "="*23)
        print("\t\tMain Menu")
        print("\t", "="*23)
        print()

        daftar_menu = [
            "Lihat",
            "Tambah",
            "Edit",
            "Hapus",
            "Cari",
            "Keluar"
        ]

        for i, data in enumerate(daftar_menu, 1):
            print(f"\t {i}: {data}")
        print()

        try:
            pilihan = int(input("Pilih Menu (1-6): "))
            print()

            if pilihan == 1:
                lihat_nama()
            elif pilihan == 2:
                tambah_nama()
            elif pilihan == 3:
                edit_nama()
            elif pilihan == 4:
                hapus_nama()
            elif pilihan == 5:
                cari_nama()
            elif pilihan == 6:
                print("Terima Kasih.")
                break
            else:
                print("Pilihan tidak ada.")
        except ValueError:
            print("Masukkan angka yang valid.")

menu()