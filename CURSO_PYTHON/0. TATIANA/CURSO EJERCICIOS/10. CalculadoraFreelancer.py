# Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, 
# para ello solo necesita establecer el precio de su trabajo por hora.
# Se estiman 40 horas de trabajo a la semana.
# Las Fórmulas para calcular el pago Semanal y Mensual son:
# 1) Pago_Semanal = (DolaresPorHora x 40)
# 2) Pago_Mensual = (DolaresPorHora x 160)

# ► Variables:

# Dolares_Por_Hora: Cantidad de Dólares que gana el Freelancer por hora.

# Pago_Semanal: Almacena el resultado del pago semanal.

# Pago_Mensual: Almacena el resultado del pago mensual.

dolares_Hora = int(input('¿Cuantos dólares ganas a la hora?: '))

horas_Semanales = 40
horas_Mensuales = 160

pago_Semanal = float(dolares_Hora * horas_Semanales)
pago_Mensual = float(dolares_Hora * horas_Mensuales)

print('El pago semanal es de: ',pago_Semanal)
print('El pago mensual es de: ',pago_Mensual)

