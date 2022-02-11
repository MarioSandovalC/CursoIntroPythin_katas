# Para este ejercicio, escribirás una lógica condicional que imprima una advertencia 
# si un asteroide se acerca a la Tierra demasiado rápido. 
# La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, 
# y cualquier velocidad superior a 25 kilómetros por segundo (km/s)
# merece una advertencia.

# Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

vel_ast=49

if vel_ast >= 25:
    print("Un asteroide se acerca muy rápido")
else:
    print("Aun tenemos tiempo para vivir"),