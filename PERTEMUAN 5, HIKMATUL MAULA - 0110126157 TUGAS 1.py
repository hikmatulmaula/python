print("=== Alat hitung luas bangunan")
print("pilih 1 untuk menghitung luas persegi")
print("pilih 2 untuk menghitung luas lingkaran")
print("pilih 3 untuk menghitung luas segitiga")

pilihan = input("masukkan pilihan (1/2/3):")

match pilihan:
    case 1:
        s=int(input("masukkan panjang sisi persegi:12"))
        luas= s+s
        print(f"luas persegi adalah: {luas}")
        
    case 2:
        r=int(input("masukkan panjang lingkaran:7"))
        pi=3.14
        luas= pi * r * 2
        print(f"luas lingkaran adalah: {luas}")
        
    case 3:
        a= int(input("masukkan panjang alas segitiga:3"))
        t= int(input("masukkan panjang tinggi segitiga:6"))
        luas= a * t / 2
        print(f"luas segitiga adalah: {luas}")
        
    case _:
        print("masukkan pilihan dengan benar")