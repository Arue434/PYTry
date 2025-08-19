
data = [
    {"nama": "John Doe", "alamat": "six street 23", "umur": 30, "hobi": ["membaca", "bersepeda", "memasak"]},
    {"nama": "jane doe", "alamat": "luofu 55", "umur": 25,"hobi": ["menulis", "berjalan-jalan", "bermain musik"]} ]

def cekdata(enter):
    if not isinstance(enter, dict):
        return False
    
    except_keys = ["nama", "alamat", "umur", "hobi"]
    for key in except_keys:
        if key not in enter:
            return False
    
    if not isinstance(enter["nama"], str): 
        return False
    if not isinstance(enter["alamat"], str):
        return False
    if not isinstance(enter["umur"], int):
        return False
    if not isinstance(enter["hobi"], list):
        return False
    
    return True

for item in data:
    print("nama:", item["nama"])
    print("alamat:", item["alamat"])
    print("umur:", item["umur"])
    print("hobi:", ", ".join(item["hobi"]))
    print("-" * 30)
else:
    print("error")


