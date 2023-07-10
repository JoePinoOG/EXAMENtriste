def op1(listasientos,listasigold,listasilver,listadd,listnom,gan1,gan2,gan3):
    ent=0
    asi=0
    while True:
        try:
            print("VALORES ENTRADA")
            print("1.Platinum, $120.000. (Asientos del 1 al 20).")
            print("2.Gold, $80.000. (Asientos del 21 al 50).")
            print("3.Silver, $50.000. (Asientos del 51 al 100.).")
            print("4.salir")
            ent=int(input("elija el tipo de entrada que desea:"))
            if ent>0 and ent<5:
                if ent==1:
                    print("una entrada platinum agregada.")
                    while True:
                        try:
                            print("LISTA ASIENTOS DISPONIBLES")
                            print(listasientos)
                            asi=int(input("seleccione el asiento que desea: "))
                            if asi>0 and asi<21:
                                print("asiento reservado con exito!")
                                listadd.append(asi)
                                gan1.append(120000)

                            else:
                                print("seleccione un asiento valido")


                            break

                        except:
                            print("error")
                    while True:
                        try:
                            nom=input("ingrese el nombre titular de las entradas: ")
                            listnom.append(nom)
                            print("TITULAR AGREGADO CON EXITO")
                            break
                        except:
                            print("error")        


                if ent==2:
                    print("una entrada gold agregada.")
                    while True:
                        try:
                            print("LISTA ASIENTOS DISPONIBLES")
                            print(listasigold)
                            asi=int(input("seleccione el asiento que desea: "))
                            if asi>20 and asi<51:
                                print("asiento reservado con exito!")
                                listadd.append(asi)
                                gan2.append(80000)
                            else:
                                print("seleccione un asiento valido")


                            break

                        except:
                            print("error")
                    while True:
                        try:
                            nom=input("ingrese el nombre titular de las entradas: ")
                            listnom.append(nom)
                            print("TITULAR AGREGADO CON EXITO")
                            break
                        except:
                            print("error")        


                if ent==3:
                    
                    print("una entrada silver agregada.")
                    while True:
                        try:
                            print("LISTA ASIENTOS DISPONIBLES")
                            print(listasilver)
                            asi=int(input("seleccione el asiento que desea: "))
                            if asi>50 and asi<101:
                                print("asiento reservado con exito!")
                                listadd.append(asi)
                                gan3.append(50000)
                                
                            else:
                                print("seleccione un asiento valido")


                            break

                        except:
                            print("error")
                    while True:
                        try:
                            nom=input("ingrese el nombre titular de las entradas: ")
                            listnom.append(nom)
                            print("TITULAR AGREGADO CON EXITO")
                            break
                        except:
                            print("error")        

                if ent==4:
                    break
            else:
                print("error")
        except:
            print("error")
def op2(listasientos,listasigold,listasilver,listadd,listnom,gan1,gan2,gan3):
    while True:
        try:
            print("LISTA ASIENTOS DISPONIBLES")
            print(listasientos)
            print(listasigold)
            print(listasilver)
            break
        except:
            print("error")
def op3(listasientos,listasigold,listasilver,listadd,listnom,gan1,gan2,gan3):
    while True:
        try:
            print("LOS ASISTENTES SON: ")
            print(listnom)
            break
        except:
            print("error")
def op4(listasientos,listasigold,listasilver,listadd,listnom,gan1,gan2,gan3):
    while True:
        try:
            print(f"Asientos platinum reservados:{len(gan1)}")
            print(f"Asientos gold reservados:{len(gan1)}")
            print(f"Asientos silver reservados:{len(gan1)}")
            suma1=len(gan1)*120000
            suma2=len(gan2)*80000
            suma3=len(gan3)*50000
            sumatotal=suma1+suma2+suma3
            print(f"las ganancias son de: {sumatotal}")
            break
        except:
            print("error")
