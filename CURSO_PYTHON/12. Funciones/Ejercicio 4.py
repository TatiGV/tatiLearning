# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def factura():
    importe = float(input('Inserta el importe sin IVA: '))
    porcentajeIva = int(input('Inserta el tanto por ciento de IVA a aplicar: '))
    if porcentajeIva != 0:
        if porcentajeIva > 0:
            iva = (importe * porcentajeIva) / 100
            total = iva + importe
            return total
        else:
            return 'El IVA no es correcto'
    else:
        iva21 = (importe * 21) / 100
        total2 = iva21 + importe
        return total2

    


print(factura())