
from django.http import HttpResponse

# Ruta fija
def saludo(request):
    return HttpResponse("¡Hola desde Django!")

# Ruta con parámetro tipo texto
def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!")

# Ruta con parámetro numérico
def mostrar_edad(request, edad):
    return HttpResponse(f"Tienes {edad} años.")
