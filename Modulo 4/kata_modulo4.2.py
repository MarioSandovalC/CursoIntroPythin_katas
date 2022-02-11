# Datos 
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#Titulo

titulo = (f'Gravity Facts about {name}')

#Plantilla

plantilla=(f"""{titulo}
______________________________________________________________
Planet Name : {planet}
Gravity on {name}:  {gravity*1000}""")
# print(plantilla)

name ='Marte'
gravity = 0.00143
name ='Ganímides'
# print(plantilla)

plantilla_nueva="""
Gravity Facts about {0}
______________________________________________________________
Planet Name : {1}
Gravity on {2}:  {3}"
"""

print(plantilla_nueva.format(name,planet,name,(gravity*1000)))

