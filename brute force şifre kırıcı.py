def şifre_kırıcı():
    alfabe = "abcdefghijklmnopqrstuvwxyz0123456789"
    alfabe0 = "abcdefghijklmnopqrstuvwxyz"
    şifre = input("şifre belirleyin = ")
    sayaç = 0
    bulundu = False
    alfabe1 = "12345"
    while not bulundu:
        for a in alfabe:
            cvp0 = a
            print(cvp0)
            sayaç+=1
            if cvp0 == şifre:
                print("şifre kırıldı")
                print("şifre = {}. {} kere denendi".format(şifre,sayaç))
                bulundu = True
                break
        break 
                        
    while not bulundu:          
        for a in alfabe:
            for b in alfabe:
                cvp1 = a+b
                print(cvp1)
                sayaç+=1
                if cvp1 == şifre :
                    bulundu = True
                    break
            if cvp1 == şifre :
                print("şifre kırıldı")
                print("şifre = {}. {} kere denendi".format(şifre,sayaç))
                bulundu = True
                break
        break

    while not bulundu:          
        for z in alfabe:
            for x in alfabe:
                for c in alfabe:
                    cvp2 = z+x+c
                    print(cvp2)
                    sayaç+=1
                    if cvp2 == şifre :
                        bulundu = True
                        break
                if cvp2 == şifre :
                    bulundu = True
                    break
            if cvp2 == şifre :
                print("şifre kırıldı")
                print("şifre = {}. {} kere denendi".format(şifre,sayaç))
                bulundu = True
                break
        break

    while not bulundu:          
        for z in alfabe:
            for x in alfabe:
                for c in alfabe:
                    for v in alfabe:
                        cvp2 = z+x+c+v
                        print(cvp2)
                        sayaç+=1
                        if cvp2 == şifre :
                            bulundu = True
                            break
                    if cvp2 == şifre :
                        bulundu = True
                        break
                if cvp2 == şifre :
                    bulundu = True
                    break
            if cvp2 == şifre :
                print("şifre kırıldı")
                print("şifre = {}. {} kere denendi".format(şifre,sayaç))
                bulundu = True
                break
        break

    while not bulundu:          
        for z in alfabe:
            for x in alfabe:
                for c in alfabe:
                    for v in alfabe:
                        for b in alfabe:
                            cvp2 = z+x+c+v+b
                            print(cvp2)
                            sayaç+=1
                            if cvp2 == şifre :
                                bulundu = True
                                break
                        if cvp2 == şifre :
                            bulundu = True
                            break
                    if cvp2 == şifre :
                        bulundu = True
                        break
                if cvp2 == şifre :
                    bulundu = True
                    break
            if cvp2 == şifre :
                print("şifre kırıldı")
                print("şifre = {}. {} kere denendi".format(şifre,sayaç))
                bulundu = True
                break
        break



şifre_kırıcı()

























