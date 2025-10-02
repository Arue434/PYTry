def calculator():
    print("Kalkulator Sederhana ketik 'exit' untuk mengakhiri programs")
    while True:
        a = input("Masukkan angka pertama: ")
        if a.lower() == 'exit':
            print("Terima kasih.")
            break
        
        op = input("Masukkan operator (tambah, kali, kurang, bagi): ").strip()
        if op.lower() == 'exit':
            print("Terima kasih.")
            break
        b  = input("Masukkan angka kedua: ")
        if b.lower() == 'exit':
            print("Terima kasih.")
            break

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")
            continue
        
        if  op == "tambah":
            print(f"Hasil: {a + b}")
        elif op == "kali":
            print(f"Hasil: {a * b}")
        elif op == "kurang":
            print(f"Hasil: {a - b}")
        elif op == "bagi":
            if b != 0:
                print(f"Hasil: {a / b}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
        else:
            print("Operator tidak dikenali. Silakan gunakan tambah, kali, kurang, atau bagi.")

calculator()