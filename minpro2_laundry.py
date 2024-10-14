# Aris Candra Muzaffar | 2409116088 | Sistem Informasi C '24
# Program Pengelolaan Laundry

# Ketentuannya:
# a. Terdapat 2 role, yaitu pembeli dan admin. (Dapat berupa role lain, misal pasien dan admin) CHECK
# b. Menu untuk role admin bisa melakukan CRUD (Create, Read, Update, dan Delete) CHECK
# c. Menu untuk role pembeli hanya dapat melakukan transaksi. (Aktivitas role lainnya bisa disesuaikan. Contoh role pasien dapat mendaftarkan diri untuk antrian) CHECK
# d. Menerapkan Login CHECK
# e. Membuat flowchart
# f. Memiliki tampilan yang dapat dimengerti user
# g. Membuat file README.md yang didalamnya terdapat gambar flowchart dan penjelasan beserta screenshoot bagaimana programnya berjalan dari awal hingga akhir.
# h. Mengumpulkan melalui github (file python Mini Project 2 dan README.md). Yang dikumpulkan di classroom adalah link repository nya. 
# Nilai tambahan (Bersifat Opsional) :
# Menggunakan PrettyTable CHECK

# Import library
from prettytable import PrettyTable
from datetime import datetime # Untuk tanggal dan waktu
import pwinput, string, random # pwinput untuk password ****, string dan random untuk buat kode di struk

# Daftar jasa laundry dengan harga, angka di luar kurung adalah id jasa, dirujuk var key. INGAT!
jasa = {
    '1': {'nama': 'Cuci', 'harga': 8000},
    '2': {'nama': 'Setrika', 'harga': 5000},
    '3': {'nama': 'Cuci + Setrika', 'harga': 10000},
    '4': {'nama': 'Dry Cleaning', 'harga': 15000},
    '5': {'nama': 'Cuci Karpet', 'harga': 25000},
    '6': {'nama': 'Cuci Sepatu', 'harga': 20000}
}

# untuk menampilkan tabel
table = PrettyTable()

def tampilkan_jasa():
    # Fungsi untuk menampilkan daftar jasa laundry
    table.title, table.field_names = "LAUNDRY ARIS", ['No', 'Daftar Jasa', 'Harga (Rp)']
    table.clear_rows()
    # k itu key untuk id jasa, v itu value untuk isinya
    # sorted itu untuk mengurutkan berdasarkan id jasa, untuk mastikan nomornya itu benar
    [table.add_row([k, v['nama'], f'Rp {v["harga"]}']) for k, v in sorted(jasa.items(), key=lambda x: int(x[0]))]
    print(table)

def login_admin():
    # Fungsi untuk login admin
    print('+' + '='*21 + '+\n|     LOGIN ADMIN     |\n+' + '='*21 + '+')
    if input("Username: ") == "admin" and pwinput.pwinput(prompt='Password: ', mask='*') == "admin123":
        print("Login berhasil!\n")
        menu_admin()
    else:
        print("Username atau password salah.\n")

def menu_admin():
    while True: # looping agar bisa kembali ke menu admin
        print('+' + '='*21 + '+\n|     MENU ADMIN      |\n+' + '='*21 + '+')
        print('1. Lihat Semua Jasa\n2. Tambah Jasa\n3. Update Jasa\n4. Hapus Jasa\n5. Logout') # Pakai \n untuk hemat baris kode
        pilihan = input("Pilih (1-5): ")
        if pilihan == "1": tampilkan_jasa()
        elif pilihan == "2": tambah_jasa()
        elif pilihan == "3": update_jasa()
        elif pilihan == "4": hapus_jasa()
        elif pilihan == "5": 
            print("Logout berhasil.\n")
            break
        else: print("Pilihan tidak valid. Silakan coba lagi.\n")

def tambah_jasa():
    # Fungsi untuk menambahkan jasa baru
    nama_jasa = input("Masukkan nama jasa: ")
    while True:  # Looping untuk memastikan input harga valid
        try:
            harga_jasa = int(input("Masukkan harga jasa: "))
            jasa[str(len(jasa) + 1)] = {'nama': nama_jasa, 'harga': harga_jasa}  # Menambahkan jasa baru ke dictionary
            print(f"Jasa '{nama_jasa}' dengan harga Rp {harga_jasa} berhasil ditambahkan.\n")
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka untuk harga jasa.")
    tampilkan_jasa()



def update_jasa():
    # Fungsi untuk memperbarui jasa
    tampilkan_jasa()
    while True:
        jasa_id = input("Jasa No. berapa yang ingin Anda ubah? ")
        if jasa_id in jasa: # cek apakah id jasa ada di dictionary
            nama_baru = input("Masukkan nama baru (biarkan kosong jika tidak ingin diubah): ")
            while True: # looping agar bisa kembali ke menu update jasa
                harga_input = input("Masukkan harga baru (biarkan kosong jika tidak ingin diubah): ")
                if harga_input == "": 
                    harga_baru = jasa[jasa_id]['harga'] # jika tidak ingin diubah, maka harga baru tetap sama dengan harga lama
                    break
                try:
                    harga_baru = int(harga_input) # cek apakah input harga baru adalah angka
                    break
                except ValueError: 
                    print("Input tidak valid. Masukkan angka untuk harga baru.")
            if nama_baru: jasa[jasa_id]['nama'] = nama_baru # jika nama baru ada, maka ubah nama jasa
            jasa[jasa_id]['harga'] = harga_baru
            print(f"Jasa no. {jasa_id} berhasil diperbarui.\n")
            break
        else:
            print("No. jasa yang Anda masukkan tidak ada. Silakan coba lagi.\n")

def hapus_jasa():
    # Fungsi untuk menghapus jasa
    tampilkan_jasa()
    while True: # looping agar bisa kembali ke menu hapus jasa
        jasa_id = input("Jasa No. berapa yang ingin Anda hapus? ")
        if jasa_id in jasa: # jika no. jasa yang ingin dihapus ada di dictionary jasa
            del jasa[jasa_id]
            update_no_jasa()
            print("Jasa berhasil dihapus.\n")
            break
        else: # jika no. jasa yang ingin dihapus tidak ada di dictionary jasa
            print("No. jasa yang Anda masukkan tidak ada. Silakan coba lagi.\n")

def update_no_jasa():
    # Fungsi untuk memperbarui nomor / id jasa setelah penghapusan
    global jasa
    # i itu index, v itu value. (i, v) itu listnya. sorted itu untuk mengurutkan dictionary berdasarkan key. 
    jasa = {str(i): v for i, (_, v) in enumerate(sorted(jasa.items(), key=lambda x: int(x[0])), start=1)}

def validasi_tanggal(hari, bulan, tahun):
    # Fungsi untuk memvalidasi format tanggal
    try:
        datetime.strptime(f"{hari}-{bulan}-{tahun}", "%d-%m-%Y") # "%d-%m-%Y" itu format tanggal yang diinginkan.
        return True # kalau benar, True
    except ValueError:
        return False # kalau salah, False

def menu_kustomer():
    # Fungsi untuk mengelola menu kustomer dan proses pemesanan
    while True: # kalau pengguna memilih 2 di menu utama, maka akan masuk ke looping ini
        print("\nBerikut adalah jasa yang kami sediakan:")
        tampilkan_jasa()
        # len(jasa) itu untuk menghitung jumlah jasa yang ada. +1 itu untuk opsi kembali ke menu utama, karena menambah dari jumlah list jasanya.
        print(f"{len(jasa) + 1}. Kembali ke Menu Utama")
        pilihan_jasa = input(f"Pilih jasa yang anda inginkan (1-{len(jasa) + 1}): ").strip() # strip itu untuk menghapus spasi di depan dan belakang inputan.
        
        if pilihan_jasa == str(len(jasa) + 1): # kalau pilihan_jasa = len(jasa) + 1, berarti balik ke menu utama.
            print("Kembali ke menu utama.\n")
            return # return itu untuk keluar dari fungsi.
        elif pilihan_jasa not in jasa:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
            continue # continue itu untuk mengulang dari awal looping.
        else:
            print(f"Anda memilih jasa: {jasa[pilihan_jasa]['nama']}")

        # Mengumpulkan data kustomer
        nama = input("Masukkan nama Anda: ").strip()
        skrg = datetime.now() # untuk ambil tanggal dan waktu sekarang.
        tgl_pemesanan, jam_pemesanan = skrg.strftime("%d-%m-%Y"), skrg.strftime("%H:%M")
        sembarang = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9)) # buat kode pesanan acak
        
        # Input dan validasi berat laundry
        while True: # kalau inputan bukan angka, maka akan muncul pesan error, kustomer input ulang.
            try:
                berat = float(input("Masukkan berat laundry (kg): "))
                if berat > 0: break
                print("Berat harus lebih dari 0. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.")
        
        total_harga = berat * jasa[pilihan_jasa]['harga']
        
        # Input dan validasi tanggal pengambilan
        while True:
            print("Kapan laundry anda ingin diambil?")
            # Input tanggal pengambilan
            hari, bulan, tahun = input("Tanggal (dd): ").strip(), input("Bulan (mm): ").strip(), input("Tahun (yyyy): ").strip()
            if validasi_tanggal(hari, bulan, tahun):
                tanggal_ambil = f"{hari}-{bulan}-{tahun}"
                # Cek tanggal pengambilan, jika tanggal pengambilan sebelum tanggal pemesanan, maka akan muncul pesan error.
                if datetime.strptime(tanggal_ambil, "%d-%m-%Y") < datetime.strptime(tgl_pemesanan, "%d-%m-%Y"):
                    print("Tanggal pengambilan tidak boleh sebelum tanggal pemesanan.")
                else:
                    # Paket 1 day express jika tanggal pengambilan hanya 1 hari setelah tanggal pemesanan, maka akan dikenakan biaya tambahan (10000).
                    if (datetime.strptime(tanggal_ambil, "%d-%m-%Y") - datetime.strptime(tgl_pemesanan, "%d-%m-%Y")).days == 1:
                        total_harga += 10000
                        print("Anda akan dikenakan biaya tambahan paket 1 day express.")
                    else:
                        print("Anda akan dikenakan tarif normal.")
                    break
            else:
                print("Tanggal tidak valid atau mustahil. Silakan masukkan kembali.")
        
        # Input dan validasi nomor telepon
        while True:
            nomor_telepon = input("Masukkan no. telepon anda: ").strip()
            # memastikan bahwa nomor telepon hanya berisi angka dan memiliki panjang minimal 10 digit
            if nomor_telepon.isdigit() and len(nomor_telepon) >= 10: break
            print("No. Telepon hanya boleh berisi angka dan minimal 10 digit. Silakan coba lagi.")

        # Membuat dan menampilkan struk
        table = PrettyTable()
        table.field_names = ["LAUNDRY ARIS"]
        table.add_rows([
            [f"Nama: {nama}"],
            [f"Tanggal Pemesanan: {tgl_pemesanan}"],
            [f"Waktu Pemesanan: {jam_pemesanan}"],
            [f"Tanggal Pengambilan: {tanggal_ambil}"],
            [f"Nomor Telepon: {nomor_telepon}"],
            [f"Jumlah Total: Rp {total_harga}"],
            [f"Kode Pelayanan Anda #{sembarang}"],
            ["Silakan foto struk ini."]
        ])
        print(table)
        print("Terima kasih atas pesanan Anda. Silakan ambil barang Anda pada tanggal pengambilan dengan menunjukkan struk ini.\n")
        break

def menu_utama():
    # Fungsi menu utama untuk menjalankan program
    while True:
        print('+' + '='*32 + '+\n| Selamat Datang di Laundry Aris |\n+' + '='*32 + '+')
        print("Silakan Pilih Role Anda\n1. Admin\n2. Kustomer\n3. Keluar") # Hemat baris
        pilihan = input("Pilih (1-3): ")
        if pilihan == "1": login_admin()
        elif pilihan == "2": menu_kustomer()
        elif pilihan == "3":
            print("Terima kasih atas kunjungan Anda!\n")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
menu_utama()