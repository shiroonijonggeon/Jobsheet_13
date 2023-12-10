def weight_convertion():   
   weight= float(input("Masukkan berat badan: "))
   tipe = input("Dalam (Kg)K/(Lbs)L: ").upper()
   if tipe == "K":
      print ("berat dalam Lbs: ", weight*2.2, "Pounds")
   elif tipe == "L":
      print("berat dalam Kg: ", weight/2.2, "Kg")
      