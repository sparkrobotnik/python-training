from custom_utils import clear
from time import sleep

clear()
app_config = {
	'nome':		"library assistant",
	'versao': "1.0",
	'autor':	"spark robotnik"
}
usuario = {
	'nome':	input("informe seu nome(completo): "),
	'idade':input("qual a sua idade: "),
	'email':input("email: ")
}

clear()
print(f"NOME: 	{usuario['nome']}")
print(f"IDADE:	{usuario['idade']} anos")
print(f"EMAIL:	{usuario['email']}")