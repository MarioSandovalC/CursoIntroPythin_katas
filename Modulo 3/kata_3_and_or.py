# En este ejercicio, aprenderás información más matizada sobre cuándo los asteroides 
# representan un peligro para la Tierra, y utilizarás esa información para 
# mejorar nuestro sistema de advertencia. Aquí está la nueva información que necesitas saber:

# *Los asteroides de menos de 25 metros en su dimensión más grande probablemente se quemarán 
# a medida que entren en la atmósfera de la Tierra.

# Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña 
# que 1000 metros golpeara la Tierra, causaría mucho daño.

# La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad 
# superior a 25 kilómetros por segundo (km/s) merece una advertencia.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, 
# a veces produce un rayo de luz que se puede ver desde la Tierra.

vel_ast=20
dimension = 22

if vel_ast > 25 and dimension > 25:
    print("Se acerca un asteroide muy grande muy rápido")
elif vel_ast <=20 and dimension > 25:
    print("Se acerca lentamente un gran asteroide")
elif vel_ast >25 and dimension < 25:
    print("Mira al cielo por una gran vista")
else:
    print("Mira al cielo por una gran vista")