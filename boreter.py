def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    text = input("Masukkan teks (atau ketik 'done' untuk keluar): ")
    if text.lower() == 'done':
        print("berhasil keluar")
        break
    
    if text.strip():
        if text.isdigit():
            num = int(text)
        is_prime(num)
        print(f"{num} adalah bilangan prima" if is_prime(num) 
                                             else f"{num} bukan bilangan prima")
    else:
        print("teks harus angka")
else:
        print("Teks tidak boleh kosong")
