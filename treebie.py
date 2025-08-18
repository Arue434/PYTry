def cabangan(a):
    """
    positif atau negatif
    """

    if a > 0:
        return "bilangan positif"
    elif a < 0:
        return "bilangan negatif"
    else:
        return "bilangan nol"
    
    # bilangan = 5
    # hasil = cabangan(bilangan) 
    # print(f"a {bilangan} adalah {hasil}") #bilangan positif

    # bilangan = -5
    # hasil = cabangan(bilangan) 
    # print(f"a {bilangan} adalah {hasil}") #bilangan negatif

    # bilangan = 0
    # hasil = cabangan(bilangan) 
    # print(f"a {bilangan} adalah {hasil}") #bilangan nol

# a = int(input("Masukkan bilangan: "))
# hasil = cabangan(a)
# print(f"Bilangan yang dimasukkan adalah {hasil}") 

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

