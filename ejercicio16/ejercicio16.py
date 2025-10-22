from PIL import Image

# Abrir la imagen
imagen = Image.open("gatitos.jpg")
imagen = imagen.convert("RGB")

ancho, alto = imagen.size  # dimensiones originales

# ---------- ROTACIÓN 90° ----------
rotada90 = Image.new("RGB", (alto, ancho))

for x in range(ancho):
    for y in range(alto):
        pixel = imagen.getpixel((x, y))
        nuevo_x = y
        nuevo_y = ancho - 1 - x
        rotada90.putpixel((nuevo_x, nuevo_y), pixel)

# Mostrar imagen rotada 90°
rotada90.show()

# ---------- ROTACIÓN 180° ----------
rotada180 = Image.new("RGB", (ancho, alto))

for x in range(ancho):
    for y in range(alto):
        pixel = imagen.getpixel((x, y))
        nuevo_x = ancho - 1 - x
        nuevo_y = alto - 1 - y
        rotada180.putpixel((nuevo_x, nuevo_y), pixel)

# Mostrar imagen rotada 180°
rotada180.show()
