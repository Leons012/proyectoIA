import matplotlib.font_manager as fm

# Obtener la lista de todas las fuentes del sistema
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# Imprimir los nombres de las fuentes que contienen 'segoe'
for font in font_list:
    if 'segoe' in font.lower():
        font_prop = fm.FontProperties(fname=font)
        print(f"Ruta: {font} - Nombre de la fuente: {font_prop.get_name()}")