# =========================================
# FASE 5 - FUNDAMENTOS DE PROGRAMACION
# Problema 3 - Control de Inventario
# Juan David Rojas
# =========================================

# Matriz de inventario
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 15, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Impresora", 12, 12],
    ["A105", "Auriculares", 2, 6]
]

# Funcion para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# Encabezado
print("======================================")
print("   REPORTE DE REABASTECIMIENTO")
print("======================================")

# Recorrer matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print(f"\nCodigo: {codigo}")
    print(f"Articulo: {nombre}")
    print(f"Stock Actual: {stock_actual}")
    print(f"Stock Minimo: {stock_minimo}")
    print(f"Cantidad a Pedir: {pedido}")

print("\n======================================")
print("       FIN DEL REPORTE")
print("======================================")