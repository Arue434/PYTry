def cabangan(a):
    """
    bilangan grade a sampe f
    """
    
    if a >= 90:
        return "Grade A"
    elif a >= 75:
        return "Grade B"
    elif a >= 60:
        return "Grade C"
    elif a >= 45:   
        return "Grade D"
    else:
        return "Grade F"
    
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
