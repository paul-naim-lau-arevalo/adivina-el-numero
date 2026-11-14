import random


def mostrar_bienvenida():
    print("\n" + "=" * 42)
    print("          ADIVINA EL NÚMERO")
    print("=" * 42)
    print("  El juego elegirá un número secreto.")
    print("  Tendrás 5 intentos para encontrarlo.")
    print("  Después de cada intento recibirás una pista.")
    print("=" * 42)


def elegir_dificultad():
    print("\n  ELEGÍ LA DIFICULTAD")
    print("  " + "-" * 29)
    print("  [1] Fácil    · del 1 al 10")
    print("  [2] Medio    · del 1 al 20")
    print("  [3] Difícil  · del 1 al 50")
    print("  " + "-" * 29)

    niveles = {"1": 10, "2": 20, "3": 50}

    while True:
        opcion = input("  Tu opción: ").strip()
        if opcion in niveles:
            return niveles[opcion]
        print("  Elegí una opción válida: 1, 2 o 3.")


def pedir_numero(limite):
    while True:
        respuesta = input(f"  Tu número (1 a {limite}): ").strip()
        try:
            numero = int(respuesta)
        except ValueError:
            print("  Escribí un número entero para continuar.")
            continue

        if 1 <= numero <= limite:
            return numero
        print(f"  El número debe estar entre 1 y {limite}.")


def jugar():
    limite = elegir_dificultad()
    secreto = random.randint(1, limite)
    intentos_maximos = 5

    print("\n" + "=" * 42)
    print("              ¡A JUGAR!")
    print("=" * 42)
    print(f"  Número secreto: entre 1 y {limite}")
    print(f"  Intentos disponibles: {intentos_maximos}")

    for intento in range(1, intentos_maximos + 1):
        print(f"\n  --- Intento {intento} de {intentos_maximos} ---")
        numero = pedir_numero(limite)

        if numero == secreto:
            print("\n" + "*" * 42)
            print("              ¡GANASTE!")
            print(f"  Adivinaste el número {secreto} en {intento} intento(s).")
            print("*" * 42)
            return
        if numero < secreto:
            print("  Pista: el número secreto es MAYOR.")
        else:
            print("  Pista: el número secreto es MENOR.")

    print("\n" + "-" * 42)
    print("  Se terminaron los intentos.")
    print(f"  El número secreto era {secreto}.")
    print("  ¡Podés volver a intentarlo!")
    print("-" * 42)


def preguntar_si_repite():
    while True:
        respuesta = input("\n¿Quieren jugar otra vez? (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Respondé con s o n.")





# APORTE COMPAÑERO 2:
# Propuesta: agregar un contador de partidas ganadas y perdidas.
# Pueden trabajar aquí y después integrar los cambios al juego.


def main():
    mostrar_bienvenida()
    while True:
        jugar()
        if not preguntar_si_repite():
            print("\n  ¡Gracias por jugar! Hasta la próxima.\n")
            break


if __name__ == "__main__":
    main()
