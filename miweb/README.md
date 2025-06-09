# Enrutamiento en Django - Semana 2

Este proyecto contiene tres rutas principales:

1. `/`  
   - Muestra un saludo fijo: "¡Hola desde Django!"

2. `/saludo/<nombre>/`  
   - Saluda al usuario según el nombre pasado en la URL.  
   - Ejemplo: `/saludo/Ana/` muestra "Hola, Ana!"

3. `/edad/<edad>/`  
   - Muestra un mensaje con la edad del usuario.  
   - Ejemplo: `/edad/25/` muestra "Tienes 25 años."

Los archivos principales son:
- `views.py`: contiene las funciones que devuelven los mensajes.
- `urls.py` (de la app): define las rutas.
