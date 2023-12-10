def guess_number():    
    angka_rahasia = 18
    batas = 3
    penghitung = 0

    while penghitung < batas:
        user = int(input("Masukkan Angka"))
        
        if user == angka_rahasia:
            print("Selamat!")
            break
        else:
            print("Salah")
            penghitung += 1
    if penghitung == batas:
        print(f"Maaf anda gagal. angka rahasianya adalah{18}.")
