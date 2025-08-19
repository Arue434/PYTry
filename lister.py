Imlist = ["banana", "apple", "orange", "grape"]
print("list mamam:", Imlist)
Imlist.sort()

rata = ["70", "85", "60", "90", "75"]
nilai = [float(i) for i in rata]
print("list grade:", rata)

def ratalist(rata):
    """
    menghitung rata-rata 
    """
    if not rata:
        return 0
    return sum(rata) / len(rata)

average = ratalist(nilai)
print(f"rata-rata nya dari {nilai} adalah: {average}")

alpha =  5
beta = 7
theta = 9
delta = 8

jumlah = alpha + beta + theta + delta
print("jumlah :", jumlah)

kalian = alpha * beta * theta * delta
print("hasil :", kalian)

bagian = alpha / beta
print("hasil :", bagian)

itungan = [alpha / delta] + [beta * theta]
print("hasil :", itungan)

# a = 1
# b = 0

# hehe = a / b 
# print("hasil:", hehe) 

listener = ["a", "i", "u", "e", "o"]
jumlah_listener = len(listener)
print("jumlah listener:", jumlah_listener)

