def hitungkata():    

    "hitung kata"

    text = input("Masukkan teks: ")
    word = text.split()
    juka = len(word)
    print(f"Jumlah kata: {juka}")
    
hitungkata()

while True:
    text = input("Masukkan teks (atau ketik 'done' untuk keluar): ")
    if text.lower() == 'done':
        print("berhasil keluar")
        break
    
    if text.strip():
        hitungkata()
    else:
        print("Teks tidak boleh kosong")