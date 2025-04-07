def slice_simple():
    texto = "Awesome"
    primeras_3 = texto[:3].lower()
    print(primeras_3)
    letras_en_medio = texto[2:5].lower()
    print(letras_en_medio)

    letras_rango_1 = texto[:4].lower()
    letras_rango_2 = texto[-3:].lower()
    print(letras_rango_1 + letras_rango_2)
