def check_vowels():
    nombre = input("Ingresar Nombre: ")
    nombre = nombre.lower()
    print("Contiene a:", {"a" in nombre})
    print("Contiene e:", {"e" in nombre})
    print("Contiene i:", {"i" in nombre})
    print("Contiene o:", {"o" in nombre})
    print("Contiene u:", {"u" in nombre})

    # Código a implementar utilizando input.
check_vowels()

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
