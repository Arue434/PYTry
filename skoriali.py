score = 0

while True:
    user_input = input("ketik 't' untuk menambah skor dan 'q' untuk keluar: ")
    if user_input == 't':
        skor_input = input("skor yang ingin ditambahkan: ")
        try:
            increment = int(skor_input)
            score += increment
        except ValueError:
            print("Input tidak valid!")
            continue
        print(f"Skor Anda: {score}")
    elif user_input == 'q':
        print("Terima kasih!")
        print(f"Skor akhir : {score}")
        break
    else:
        print("Input tidak valid! Ketik 't' untuk menambah skor.")

