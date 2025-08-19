import random

# print("Program angka Acak")
# liest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# randomses = random.choice(liest)
# print(f"angka acak yang di pilih: {randomses}")

def tebakan():

    secnum = random.randint(1, 10)
    tebak = None
    jumtebak = 0

    print("Selamat datang di permainan Tebak Angka!")
    print("pilih antara angka 1 hingga 10.")

    while tebak != secnum:
        try:
            tebak = int(input("masukan angka yang anda pilih: "))
            jumtebak += 1

            if tebak < secnum:
                print("Tebakan terlalu rendah")
            elif tebak > secnum:
                print("Tebakan terlalu tinggi")   
            else:
                print(f"Tebakan benar {secnum}, dengan jumlah tebakan sebanyak {jumtebak} percobaan.")
        
        except ValueError:
            print("error not found")
        
if __name__ == "__main__":
    tebakan()

while True:
    text = input("Masukkan angka terserah (atau ketik 'done' untuk keluar): ")
    if text.lower() == 'done':
        print("berhasil keluar")
        break
    
    if text.lstrip("-").isdigit():
        a = int(text)
        hasil = tebakan()
        print(f"bilangan {a} adalah {hasil}")

    else:
        print("Error")