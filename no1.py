##nomor1
##string = ""
##bar = 1
##
##x=int (input("Cetak siku:"))
##
##while bar <= x:
##    kol = bar
##
##    while kol >0:
##        string = string + " * "
##        kol = kol - 1
##        
##    string = string + "\n"
##    bar = bar + 1
##print (string)

##nomor2
def gambarlahPersegiEmpat (tinggi,lebar):
    for i in range (tinggi):
        if i== 0 or i==tinggi-1:
            print (lebar * "@")
        else:
            print ("@"+ " " * (lebar-2) + "@")
