def cabangan(a):
    """
    bilangan genap atau ganjil
    """

    if a % 2 == 0:
        return "bilangan genap"
    else:
        return "bilangan ganjil"
    
while True:
    text = input ("Masukkan bilangan (atau ketik 'exit' untuk keluar): ")
    if text.lower() == 'exit':
            print("Keluar dari program, terima kasih!")
            break
        
    if text.lstrip("-").isdigit():
        a = int(text)
        hasil = cabangan(a)
        print(f"bilangan {a} adalah {hasil}")

    else:
        print("Input tidak valid.")