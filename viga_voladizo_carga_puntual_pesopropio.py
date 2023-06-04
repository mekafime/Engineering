# Este código fue creado por mekafime. 
# Para calcular la deflexión máxima y el esfuerzo máximo en una viga en voladizo
# Considerar:
# - La viga está empotrada en uno de sus extremos.
# - La viga es de sección tubular rectangular o cuadrada.
# - La carga distribuida es el peso de la viga.
# - La carga puntual es el peso de algún objeto sobre la viga, como luminaria, aire acondicionado, etc.

def calcular_deformacion_y_esfuerzo(largo, carga_distribuida, carga_puntual, posicion_carga, ancho, altura, espesor, modulo_elasticidad):

    # Calcular el peso de la viga
    peso_especifico_acero = 7850  # Peso específico del acero en kgf/m³
    peso_viga = peso_especifico_acero * (ancho * altura - (ancho - 2 * espesor) * (altura - 2 * espesor)) * largo

    # Calcular el momento de inercia de la sección de la viga
    momento_inercia = (ancho * altura**3 - (ancho - 2 * espesor) * (altura - 2 * espesor)**3) / 12

    # Calcular la deformación por carga puntual
    deformacion_puntual = (carga_puntual * posicion_carga**3) / (3 * modulo_elasticidad * momento_inercia)

    # Calcular la deformación por carga distribuida
    deformacion_distribuida = (carga_distribuida * largo**4) / (8 * modulo_elasticidad * momento_inercia)

    # Calcular la deformación total
    deformacion_total = deformacion_puntual + deformacion_distribuida

    # Calcular el esfuerzo máximo en el extremo empotrado
    esfuerzo_maximo_empotrado = ((carga_puntual * posicion_carga + carga_distribuida * largo_viga**2 / 2) * (altura / 2)) / momento_inercia

    return deformacion_total, esfuerzo_maximo_empotrado


# Solicitación de los valores de entrada
largo_viga = float(input("Ingrese la longitud de la viga (m): "))
ancho_seccion = float(input("Ingrese el ancho de la sección de la viga (m): "))
altura_seccion = float(input("Ingrese la altura de la sección de la viga (m): "))
espesor_seccion = float(input("Ingrese el espesor de la sección de la viga (m): "))

modulo_elasticidad_acero = 2.1e11  # Módulo de elasticidad del acero en Pascal

carga_puntual = float(input("Ingrese la carga aplicada en el extremo de la viga (N): "))
posicion_carga = float(input("Ingrese la posición de la carga puntual respecto al lado empotrado de la viga (m): "))

# Calcular la carga distribuida debido al peso propio de la viga
peso_especifico_acero = 7850  # Peso específico del acero en kgf/m³
carga_distribuida = peso_especifico_acero * (ancho_seccion * altura_seccion - (ancho_seccion - 2 * espesor_seccion) * \
(altura_seccion - 2 * espesor_seccion)) * 9.81 # Carga en Newtons

deformacion, esfuerzo = calcular_deformacion_y_esfuerzo(largo_viga, carga_distribuida, carga_puntual, posicion_carga, \
ancho_seccion, altura_seccion, espesor_seccion, modulo_elasticidad_acero)

print("Deflexión máxima: {:.2f} mm".format(deformacion * 1000))
print("Esfuerzo máximo: {:.2f} MPa".format(esfuerzo / 1e6))