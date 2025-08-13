
from tabulate import tabulate
from datetime import date

customers = {
   'fs7005102': {'nama': 'febrian sinagar', 'tanggal lahir': date(1970, 5, 10), 'gaji': 3000000, 'status perkawinan': 'kawin', 'alamat': 'sumatera utara'},
   'aj01030911': {'nama': 'ardi jono', 'tanggal lahir': date(2001, 3, 9), 'gaji': 0, 'status perkawinan': 'belum kawin', 'alamat': 'dki jakarta'},
   'ap87012312': {'nama': 'ani pulungan', 'tanggal lahir': date(1987, 1, 23), 'gaji': 2500000, 'status perkawinan': 'kawin', 'alamat': 'jawa barat'},
   'mr99061327': {'nama': 'mutiara rahayu', 'tanggal lahir': date(1999, 6, 13), 'gaji': 5000000, 'status perkawinan': 'janda/duda', 'alamat': 'sulawesi tengah'},
   'dk75121716': {'nama': 'dian kusuma', 'tanggal lahir': date(1975, 12, 17), 'gaji': 8000000, 'status perkawinan': 'belum kawin', 'alamat': 'jawa timur'},
   'as85051212': {'nama': 'agus sutanto', 'tanggal lahir': date(1995, 5, 12), 'gaji': 12000000, 'status perkawinan': 'kawin', 'alamat': 'jawa barat'},
   'bw90041514': {'nama': 'bima wicaksono', 'tanggal lahir': date(1990, 4, 15), 'gaji': 9500000, 'status perkawinan': 'belum kawin', 'alamat': 'jawa tengah'},
}

savingaccount = {
    'as85242026': {'c_id': 'as85051212', 'open date': date(2019, 8, 14), 'balance': 735000, 'status': 'active'},
    'as85251533': {'c_id': 'as85051212', 'open date': date(2020, 3, 21), 'balance': 0, 'status': 'closed'},
    'as85242029': {'c_id': 'as85051212', 'open date': date(2019, 10, 17), 'balance': 1095000, 'status': 'active'},
    'as85242033': {'c_id': 'as85051212', 'open date': date(2021, 8, 10), 'balance': 438000, 'status': 'active'},
    'as85242013': {'c_id': 'as85051212', 'open date': date(2019, 10, 1), 'balance': 618000, 'status': 'active'},
    'as85241826': {'c_id': 'as85051212', 'open date': date(2020, 6, 14), 'balance': 103000, 'status': 'active'},
    'as85242022': {'c_id': 'as85051212', 'open date': date(2019, 12, 10), 'balance': 910000, 'status': 'dormant'},
    'bw90242529': {'c_id': 'bw90041514', 'open date': date(2020, 10, 15), 'balance': 505000, 'status': 'active'},
    'fs70760221': {'c_id': 'fs7005102', 'open date': date(2019, 7, 21), 'balance': 7050000, 'status': 'active'},
    'dk75216933': {'c_id': 'dk75121716', 'open date': date(2019, 7, 30), 'balance': 6060000, 'status': 'active'},
    'mr99152340': {'c_id': 'mr99061327', 'open date': date(2019, 5, 27), 'balance': 8874000, 'status': 'dormant'},
    'ap87212435': {'c_id': 'ap87012312', 'open date': date(2018, 2, 23), 'balance': 1236000, 'status': 'active'},
    'aj01931336': {'c_id': 'aj01030911', 'open date': date(2018, 1, 22), 'balance': 9630000, 'status': 'active'}
}

#credit → saldo bertambah, debit → saldo berkurang
transaction = {
    '210526as85242026': {'s_id': 'as85242026', 'transaction type': 'credit', 'transaction amount': 500000.00, 'transaction time': date(2021, 5, 26)},
    '210526as852420291': {'s_id': 'as85242029', 'transaction type': 'debit', 'transaction amount': 25000.00, 'transaction time': date(2021, 5, 26)},
    '210525as85242029': {'s_id': 'as85242029', 'transaction type': 'credit', 'transaction amount': 300000.00, 'transaction time': date(2021, 5, 25)},
    '210525ap87212435': {'s_id': 'ap87212435', 'transaction type': 'credit', 'transaction amount': 1000000.00, 'transaction time': date(2021, 5, 25)},
    '210525dk75216933': {'s_id': 'dk75216933', 'transaction type': 'credit', 'transaction amount': 560000.00, 'transaction time': date(2021, 5, 25)},
    '210525fs70760221': {'s_id': 'fs70760221', 'transaction type': 'debit', 'transaction amount': 150000.00, 'transaction time': date(2021, 5, 25)},
    '210524bw90242529': {'s_id': 'bw90242529', 'transaction type': 'debit', 'transaction amount': 115000.00, 'transaction time': date(2021, 5, 24)},
    '210524as85241826': {'s_id': 'as85241826', 'transaction type': 'credit', 'transaction amount': 10000.00, 'transaction time': date(2021, 5, 24)},
    '210524ap87212435': {'s_id': 'ap87212435', 'transaction type': 'debit', 'transaction amount': 15000.00, 'transaction time': date(2021, 5, 24)},
    '210524ap872124351': {'s_id': 'ap87212435', 'transaction type': 'credit', 'transaction amount': 40000.00, 'transaction time': date(2021, 5, 24)},
    '210524mr99152340': {'s_id': 'mr99152340', 'transaction type': 'debit', 'transaction amount': 26000.00, 'transaction time': date(2021, 5, 24)},
    '210523ap87212435': {'s_id': 'ap87212435', 'transaction type': 'credit', 'transaction amount': 50000.00, 'transaction time': date(2021, 5, 23)},
    '210522as85242026': {'s_id': 'as85242026', 'transaction type': 'credit', 'transaction amount': 24000.00, 'transaction time': date(2021, 5, 22)},
    '210522ap87212435': {'s_id': 'ap87212435', 'transaction type': 'debit', 'transaction amount': 24000.00, 'transaction time': date(2021, 5, 22)},
    '210521ap87212435': {'s_id': 'ap87212435', 'transaction type': 'credit', 'transaction amount': 64000.00, 'transaction time': date(2021, 5, 21)},
    '210521as85242013': {'s_id': 'as85242013', 'transaction type': 'debit', 'transaction amount': 32000.00, 'transaction time': date(2021, 5, 21)},
    '210521as85242033': {'s_id': 'as85242033', 'transaction type': 'credit', 'transaction amount': 18000.00, 'transaction time': date(2021, 5, 21)},
    '210521ap872124351': {'s_id': 'ap87212435', 'transaction type': 'debit', 'transaction amount': 39000.00, 'transaction time': date(2021, 5, 21)},
    '210521ap872124352': {'s_id': 'ap87212435', 'transaction type': 'credit', 'transaction amount': 40000.00, 'transaction time': date(2021, 5, 21)},
    '210521as852420261': {'s_id': 'as85242026', 'transaction type': 'debit', 'transaction amount': 39000.00, 'transaction time': date(2021, 5, 21)},
    '210520aj01931336': {'s_id': 'aj01931336', 'transaction type': 'debit', 'transaction amount': 70000.00, 'transaction time': date(2021, 5, 20)}
}


# Helper Functions
def validate_choice(prompt, choices):
    value = input(prompt).strip().lower()
    while value not in choices:
        print(f"Pilihan tidak valid. Pilihan yang tersedia: {', '.join(choices)}")
        value = input(prompt).strip().lower()
    return value

def validate_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            tahun, bulan, hari = map(int, value.split("-"))
            return date(tahun, bulan, hari)
        except (ValueError, TypeError):
            print("Format tanggal harus YYYY-MM-DD.")

def validate_existing_id(prompt, data_dict):
    value = input(prompt).strip().lower()
    while value not in data_dict:
        print("ID tidak ditemukan!")
        value = input(prompt).strip()
    return value

def validate_amount(prompt, allow_negative=False):
    while True:
        value = input(prompt).strip()
        if value.replace(".", "", 1).isdigit():
            value = float(value)
            if not allow_negative and value < 0:
                print("Nilai tidak boleh negatif.")
                continue
            return value
        print("Harus berupa angka.")

def readData():
    while True:
        print('''\n=== Menu Read ===
1. All data pada tabel
2. Satu data berdasarkan primary key pada tabel
3. Kembali ke Menu Utama''')

        menu = validate_choice("Masukkan pilihan (1/2/3): ", ["1", "2", "3"])

        # Pilihan 1 - Tampilkan semua data
        if menu == "1":
            print('''\nTabel yang ingin ditampilkan:
1. Customers
2. Saving Account
3. Transaction
4. Kembali ke Menu Read''')

            tabel_pilih = validate_choice("Masukkan pilihan (1/2/3/4): ", ["1", "2", "3", "4"])
            if tabel_pilih == "4":
                continue
            elif tabel_pilih == "1":
                tabel = customers
            elif tabel_pilih == "2":
                tabel = savingaccount
            elif tabel_pilih == "3":
                tabel = transaction

            if tabel:
                table_data = []
                for key, value in tabel.items():
                    row = {"id": key}
                    if isinstance(value, dict):
                        row.update(value)
                    table_data.append(row)

                if table_data:
                    # Sorting 
                    kolom_list = list(table_data[0].keys())
                    print(f"Kolom tersedia: {', '.join(kolom_list)}")
                    kolom_input = validate_choice(
                        "Masukkan nama kolom untuk sort: ",
                        [k.lower() for k in kolom_list]
                    )
                    kolom_sort = next(k for k in kolom_list if k.lower() == kolom_input)
                    urutan = validate_choice("Urutkan Ascending (A) atau Descending (D)? ", ["a", "d"]).lower()
                    reverse_flag = True if urutan == "d" else False

                    table_data = sorted(table_data, key=lambda x: x[kolom_sort], reverse=reverse_flag)
                    print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("Data kosong.")
            else:
                print("Data tidak ditemukan.")

        # Pilihan 2 - Tampilkan satu data
        elif menu == "2":
            print('''\nTabel yang ingin diakses:
1. Customers
2. Saving Account
3. Transaction
4. Kembali ke Menu Read''')

            tabel_pilih = validate_choice("Masukkan pilihan (1/2/3/4): ", ["1", "2", "3", "4"])
            if tabel_pilih == "4":
                continue
            elif tabel_pilih == "1":
                tabel = customers
            elif tabel_pilih == "2":
                tabel = savingaccount
            elif tabel_pilih == "3":
                tabel = transaction


            if tabel:
                pk = validate_existing_id("Masukkan primary key: ", tabel)
                value = tabel[pk]
                table_data = [{"Field": k, "Value": v} for k, v in value.items()]
                print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))

            else:
                print("Data tidak ditemukan.")

        # Pilihan 3 - Kembali ke menu utama
        elif menu == "3":
            return


def createData():
    while True:
        print('''\n=== Menu Create ===
1. Tambah Data Customer
2. Tambah Data Saving Account
3. Tambah Data Transaction
4. Kembali ke Menu Utama''')

        menu = validate_choice("Masukkan pilihan (1/2/3/4): ", ["1", "2", "3", "4"])
        if menu == "4":
            break

        if menu == "1":
            tabel = customers
        elif menu == "2":
            tabel = savingaccount
        elif menu == "3":
            tabel = transaction

        kolom = next(iter(tabel.values()))
        kolom_list = list(kolom.keys())

        # Minta primary key (key dict)
        pk = input("Masukkan ID: ").strip()
        if pk in tabel:
            print("ID sudah ada!")
            continue

        data_baru = {}
        for kolom in kolom_list:
            if "tanggal lahir" in kolom or "open date" in kolom or "transaction time" in kolom:
                nilai = validate_date(f"Masukkan {kolom}: ")

            elif kolom == "c_id" and menu == "2":
                nilai = validate_existing_id(f"Masukkan {kolom}: ", customers)

            elif kolom == "s_id" and menu == "3":
                nilai = validate_existing_id(f"Masukkan {kolom}: ", savingaccount)

            elif kolom == "transaction type":
                nilai = validate_choice(f"Masukkan {kolom} (debit/credit): ", ["debit", "credit"])

            elif kolom == "transaction amount":
                jumlah = validate_amount(f"Masukkan {kolom}: ")
                if data_baru.get("transaction type", "").lower() == "debit":
                    saldo_sekarang = savingaccount[data_baru["s_id"]]["balance"]
                    while jumlah > saldo_sekarang:
                        print(f"Saldo tidak cukup. Saldo saat ini: {saldo_sekarang}")
                        jumlah = validate_amount(f"Masukkan {kolom}: ")
                nilai = jumlah

            else:
                nilai = input(f"Masukkan {kolom}: ").strip()

            data_baru[kolom] = nilai

        tabel[pk] = data_baru
        print("Data berhasil ditambahkan!")

def updateData():
    while True:
        print('''\n=== Menu Update ===
1. Update Data Berdasarkan Primary Key
2. Kembali ke Menu Utama''')

        menu = validate_choice("Masukkan pilihan (1/2): ", ["1", "2"])
        if menu == "2":
            break

        print('''\nPilih tabel yang ingin diupdate:
1. Customers
2. Saving Account
3. Transaction
4. Kembali ke Menu Update''')

        tabel = validate_choice("Masukkan pilihan (1/2/3/4): ", ["1", "2", "3", "4"])
        if tabel == "4":
            continue
        elif tabel == "1":
            tabel = customers
        elif tabel == "2":
            tabel = savingaccount
        elif tabel == "3":
            tabel = transaction

        pk = input("Masukkan primary key: ").strip()
        if pk not in tabel:
            print("Data tidak ditemukan.")
            continue

        value = tabel[pk]
        print("\n=== Data Saat Ini ===")
        for k, v in value.items():
            print(f"{k}: {v}")

        kolom = input("Masukkan nama kolom yang ingin diubah persis seperti yang ditampilkan: ").strip()

        if kolom.lower() in ["c_id", "s_id"]:
            print(f"Kolom '{kolom}' tidak dapat diubah karena memiliki relasi ke tabel lain.")
            continue
        if kolom not in value:
            print("Kolom tidak ditemukan.")
            continue

        nilai_baru = input("Masukkan nilai baru: ").strip()

        # Khusus untuk transaksi
        if tabel == "3":
            old_trans = transaction[pk]
            s_id_lama = old_trans["s_id"]
            tipe_lama = old_trans["transaction type"].lower()
            jumlah_lama = old_trans["transaction amount"]

            # Batalkan efek lama
            if tipe_lama == "credit":
                savingaccount[s_id_lama]["balance"] -= jumlah_lama
            else:
                savingaccount[s_id_lama]["balance"] += jumlah_lama

            if kolom == "transaction amount":
                nilai_baru = float(nilai_baru)

            old_trans[kolom] = nilai_baru

            # Terapkan efek baru
            s_id_baru = old_trans["s_id"]
            tipe_baru = old_trans["transaction type"].lower()
            jumlah_baru = old_trans["transaction amount"]

            if tipe_baru == "credit":
                savingaccount[s_id_baru]["balance"] += jumlah_baru
            else:
                savingaccount[s_id_baru]["balance"] -= jumlah_baru

            print("Transaksi berhasil diperbarui, saldo sudah disesuaikan.")

        else:
            value[kolom] = nilai_baru
            print("Data berhasil diperbarui.")

def deleteData():
    while True:
        print('''\n=== Menu Delete ===
1. Hapus Data
2. Kembali ke Menu Utama''')

        menu = validate_choice("Masukkan pilihan (1/2): ", ["1", "2"])
        if menu == "2":
            return

        # Pilih tabel
        print('''\nTabel yang ingin diakses:
1. Customers
2. Saving Account
3. Transaction
4. Kembali ke Menu Delete''')

        tabel = validate_choice("Masukkan pilihan (1/2/3/4): ", ["1", "2", "3", "4"])
        if tabel == "4":
            continue
        elif tabel == "1":
            tabel = customers
        elif tabel == "2":
            tabel = savingaccount
        elif tabel == "3":
            tabel = transaction

        pk = validate_existing_id("Masukkan primary key: ", tabel)

        # Khusus untuk hapus transaction
        if tabel == "3":
            trans = transaction[pk]
            s_id = trans["s_id"]
            tipe = trans["transaction type"].lower()
            jumlah = trans["transaction amount"]

            if tipe == "credit":
                savingaccount[s_id]["balance"] -= jumlah
            else:
                savingaccount[s_id]["balance"] += jumlah

            del transaction[pk]
            print("Transaksi dihapus dan saldo saving account diperbarui.")
            continue

        # Validasi relasi sebelum hapus
        if tabel == "1":  # Customers
            if any(sa["c_id"] == pk for sa in savingaccount.values()):
                print("Tidak bisa menghapus customer ini karena masih memiliki saving account.")
                continue
        elif tabel == "2":  # Saving Account
            if any(tr["s_id"] == pk for tr in transaction.values()):
                print("Tidak bisa menghapus saving account ini karena masih memiliki transaksi.")
                continue

        # Hapus data biasa
        del tabel[pk]
        print("Data berhasil dihapus.")


def mainMenu():
    while True:
        
        print('''Menu layanan:
1. Menampilkan data
2. Membuat data baru
3. Memperbarui data
4. Menghapus data
5. Keluar
        ''')

        action = int(input("Silakan pilih menu yang diinginkan (1/2/3/4/5): "))
        if action == 1:
            readData()
        elif action == 2:
            createData()
        elif action == 3:
            updateData()
        elif action == 4:
            deleteData()
        elif action == 5:
            print("Anda telah keluar dari program.")
            break
        else:
            action = int(input("Pilihan anda tidak valid.\nSilakan pilih menu yang diinginkan (1/2/3/4/5): "))

mainMenu()
