oreList = []
for i in range(1, 4):   #matriks
    row = []
    for j in range(1, 4):
        row.append(i * j)
    oreList.append(row)
print(oreList)

oreList = []
for i in range(1, 10):
    oreList.append(i)
print(oreList)

# --------------------------------------------------------------------------------------
print("ketik 'done' untuk selesai atau ketik apa saja untuk memulai")
lister = []

while True:
    text = input ("Masukkan item anda: ")
    if text.lower() == 'done':
            print("pesanan selesai, terima kasih!")
            break
    lister.append(text)

print("Daftar item anda:")
for i, item in enumerate(lister, start=1):

    print(f"{i}. {item}")
