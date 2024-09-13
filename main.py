from POO.mi_clase import MiClase

def main():
    calculadora = MiClase()
    
    while True:
        calculadora.mostrar_menu()
        opcion = input("Escolle unha das opcions (1/2/3/4/5): ")

        if opcion == '5':
            print("Ata logo!")
            break

        num1 = float(input("Introdza o primeiro número: "))
        num2 = float(input("Introdza o segundo número: "))

        if opcion == '1':
            print("Resultado:", calculadora.sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", calculadora.restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", calculadora.multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", calculadora.dividir(num1, num2))
        else:
            print("Opción non válida, por favor intentao novamente.")

if __name__ == "__main__":
    main()
