def generar_ticket_perfumeria():
    x = 1
    while True:
        yield f"P - {x}"
        x += 1

def generar_ticket_farmacia():
    x = 1
    while True:
        yield f"F - {x}"
        x += 1

def generar_ticket_cosmetica():
    x = 1
    while True:
        yield f"C - {x}"
        x += 1

def decorador_rubo(principal):
    print("\n" + "*"*23)
    print("Su numero es:")
    print(next(principal))
    print("Aguarde y serà atendido")
    print("*"*23 + "\n")


def iniciar():
    p = generar_ticket_perfumeria()
    f = generar_ticket_farmacia()
    c = generar_ticket_cosmetica()

    while True:
        respuesta = input(
            "seleccione el area al que se quire dirigir\n[P] Perfumeria\n[F] Farmacia\n[C] Cosmetica\n").lower()

        try:
            if respuesta == 'p':
                decorador_rubo(p)

            elif respuesta == 'f':
                decorador_rubo(f)

            elif respuesta == 'c':
                decorador_rubo(c)

            else:
                print('opciòn no permitida')
        except:
            print('algo se rompiò :(')

        else:
            romper = False
            while True:
                continuar = input('¿desea sacar otro ticket?\n[S] si\n[N] n\n').lower()
                if continuar == 's':
                    break
                elif continuar == 'n':
                    romper = True
                    break
                else:
                    print("Comando no se entiende")

            if romper == True:
                print("fue un gusto atenderlo")
                break

iniciar()