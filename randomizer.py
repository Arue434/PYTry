import random

print("===============================================================")

nama_list = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah",]

quote_list = [
    "Hidup adalah petualangan, nikmati setiap momennya.",
    "Keberanian adalah kunci untuk membuka pintu kesuksesan.",
    "Setiap hari adalah kesempatan baru untuk belajar dan tumbuh.",
    "Jadilah perubahan yang ingin kamu lihat di dunia.",
    "Kegagalan adalah batu loncatan menuju keberhasilan.",]

list_depan = [
    "Cepat", "Cerdas", "Berani", "Bijaksana", "Kreatif", "Setia",
    "Ramah", "Tangguh", "Penuh semangat", "Inovatif"]

list_belakang = [
    "seperti singa", "seperti elang", "seperti serigala", "seperti harimau",
    "seperti gajah", "seperti kuda", "seperti macan tutul", "seperti burung hantu",
    "seperti lumba-lumba", "seperti beruang"]

password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

def get_random_name():
    return random.choice(nama_list)

def get_random_quote():
    return random.choice(quote_list)

def generate_random_phrase():
    depan = random.choice(list_depan)
    belakang = random.choice(list_belakang)
    return f"{depan} {belakang}"

def generate_random_password(length=16):
    return ''.join(random.choice(password_chars) for _ in range(length))

while True:
    print("Nama acak:     ", get_random_name())
    print("Kutipan acak:  ", get_random_quote())
    print("Frasa acak:    ", generate_random_phrase())
    print("Password acak: ", generate_random_password())
    print("===============================================================")

    while True:
        lanjut = input("Ketik 'y' untuk lanjut atau 'n' untuk keluar: ").strip().lower()
        if lanjut == 'n':
            print("Terima kasih telah menggunakan program ini!!!")
            exit()
        elif lanjut == 'y':
            print("===============================================================")
            break 
        else:
            print("Input tidak valid!")
            print("===============================================================")
