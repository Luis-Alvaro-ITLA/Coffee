from interfaz import InterfazConsola, crear_maquina

if __name__ == "__main__":
    try:
        InterfazConsola(crear_maquina()).ejecutar()
    except (KeyboardInterrupt, EOFError):
        print("\n¡Hasta luego!")
