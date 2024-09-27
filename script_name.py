# Lista de archivos Markdown en el orden deseado
markdown_files = [
    '0LUNES30.md',
    '1MARTES.md',
    '2MIERCOLES.md',
    '3JUEVES.md',
    '4VIERNES.md',
    '5SABADO.md',
    '6DOMINGO.md',
    '7LUNES.md',
    '8MARTES.md',
    '9MIERCOLES.md',
    '10JUEVES.md'
]

# Crear el contenido del menú
menu_content = '# Menú de Navegación\n\n'
for md_file in markdown_files:
    menu_content += f'- [{md_file}]({md_file})\n'

# Guardar el archivo de menú
menu_filename = 'README.md'
with open(menu_filename, 'w') as menu_file:
    menu_file.write(menu_content)

print(f'Menú de navegación actualizado en {menu_filename}')