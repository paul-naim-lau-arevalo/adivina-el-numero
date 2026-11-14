import random


def elegir_dificultad():
    print("\nElegí la dificultad:")
    print("1. Fácil (1 al 10)")
    print("2. Medio (1 al 20)")
    print("3. Difícil (1 al 50)")

    niveles = {"1": 10, "2": 20, "3": 50}

    while True:
        opcion = input("Opción: ").strip()
        if opcion in niveles:
            return niveles[opcion]
        print("Elegí una opción del 1 al 3.")


def pedir_numero(limite):
    while True:
        respuesta = input(f"Ingresá un número entre 1 y {limite}: ").strip()
        try:
            numero = int(respuesta)
        except ValueError:
            print("Ingresá un número entero.")
            continue

        if 1 <= numero <= limite:
            return numero
        print(f"El número debe estar entre 1 y {limite}.")


def jugar():
    limite = elegir_dificultad()
    secreto = random.randint(1, limite)
    intentos_maximos = 5

    print(f"\nAdiviná el número secreto entre 1 y {limite}.")
    print(f"Tenés {intentos_maximos} intentos. ¡Suerte!")

    for intento in range(1, intentos_maximos + 1):
        print(f"\nIntento {intento} de {intentos_maximos}")
        numero = pedir_numero(limite)

        if numero == secreto:
            print(f"¡Excelente! Adivinaste el número en {intento} intento(s).")
            return
        if numero < secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

    print(f"\nSe terminaron los intentos. El número secreto era {secreto}.")


def preguntar_si_repite():
    while True:
        respuesta = input("\n¿Quieren jugar otra vez? (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Respondé con s o n.")


# APORTE COMPAÑERO 1:
# Propuesta: mejorar la presentación del menú o los mensajes.
# Pueden trabajar aquí y después integrar los cambios al juego.


# APORTE COMPAÑERO 2:
# Propuesta: agregar un contador de partidas ganadas y perdidas.
# Pueden trabajar aquí y después integrar los cambios al juego.


def main():
    print("=== ADIVINA EL NÚMERO ===")
    while True:
        jugar()
        if not preguntar_si_repite():
            print("¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()
