#Transformación de Cadenas

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Primero, divide el texto en cada oración para trabajar con su contenido:
oraciones = text.split('. ')
oraciones
palabras_clave = ['average','temperature','distance']
# for busca in oraciones:
#     for palabra in palabras_clave:
#         if palabra in busca:
#             print(busca)
for busca in oraciones:
    for palabra in palabras_clave:
        if palabra in busca:
            print(busca.replace('C','Celcius'))
