calchie = [{'nama': 'pai', 'harga': 5000}, 
        {'nama': 'anggur', 'harga': 12000}
        , {'nama': 'susu', 'harga': 15000},
        {'nama': 'selada', 'harga': 20000},]

print ("Daftar Barang:", calchie)

nilai = [float(i["harga"]) for i in calchie]

def tambah(nilai):
    """
    menghitung barang
    """
    if not nilai:
        return 0
    return sum(nilai)   

while True:
    print("ketik 'done' untuk keluar atau ketik 'total' untuk menjumlahkan keseluruhan.")
    nama_barang = input("Masukkan nama barang: ")
    if nama_barang.lower() == 'done':
        print("Berhasil keluar")
        break

    if nama_barang.lower() == 'total':
        total = tambah(nilai)
        print("\n = nama barang =")
        for idx, item in enumerate(calchie, start=1):
            print(f"{idx}. {item['nama']} {item['harga']}")
        print(f"Total barang: Rp.{total}\n")
        continue  

    found = False
    for item in calchie:
        if item["nama"].lower() == nama_barang.lower():
            print(f"Harga {item['nama']} : {item['harga']}")
            found = True
            break
    if not found:
        print("tidak ditemukan dalam daftar barang.")






