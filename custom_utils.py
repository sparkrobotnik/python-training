from os import system, name

def clear(): 
	#para windows 
	if name == 'nt': 
		_ = system('cls') 
	#para mac ou linux(aqui, os.name vai ser 'posix') 
	else:
			_ = system('clear')