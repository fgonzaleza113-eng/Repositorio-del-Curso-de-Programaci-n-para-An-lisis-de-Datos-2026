# 1. Crear la lista
producto = ["Cafe", 5000, 20]

# 2. Extraer los datos usando los índices
nombre = producto[0]
precio_actual = producto[1]
unidades_actuales = producto[2]

# 3. Calcular el descuento y el precio promocional
descuento = precio_actual * 15 / 100
precio_promocional = precio_actual - descuento

# 4. Calcular el ingreso actual
ingreso_actual = precio_actual * unidades_actuales

# 5. Calcular el aumento del 20% en las ventas
aumento_ventas = unidades_actuales * 20 / 100
unidades_proyectadas = unidades_actuales + int(aumento_ventas)

# 6. Calcular el ingreso con la promoción
ingreso_promocion = precio_promocional * unidades_proyectadas

# 7. Calcular la diferencia entre ambos ingresos
diferencia = ingreso_promocion - ingreso_actual

# 8. Tomar la decisión
if diferencia > 0:
    recomendacion = "lanzar"
elif diferencia < 0:
    recomendacion = "no lanzar"
else:
    recomendacion = "indiferente"

# 9. Mostrar el reporte
print("ANÁLISIS DE PROMOCIÓN")
print(f"Producto: {nombre}")
print(f"Precio actual: ₡{precio_actual}")
print(f"Unidades actuales: {unidades_actuales}")
print(f"Ingreso actual: ₡{ingreso_actual}")
print(f"Descuento: 15%")
print(f"Precio promocional: ₡{precio_promocional:.0f}")
print(f"Unidades proyectadas (supuesto +20%): {unidades_proyectadas}")
print(f"Ingreso con promoción: ₡{ingreso_promocion:.0f}")
print(f"Diferencia: ₡{diferencia:.0f}")
print(f"RECOMENDACIÓN: {recomendacion}.")