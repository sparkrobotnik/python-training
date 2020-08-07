from custom_utils import clear
from time import sleep

#MOSTRAR INFORMACOES DO APP
clear()
app_config = {
	'nome':		"library assistant",
	'versao': "1.0",
	'autor':	"spark robotnik"
}
print(f"{app_config['nome']} versão: {app_config['versao']} - autor: {app_config['autor']}")

#PEDIR CREDENCIAIS DO USUARIO
resposta = "";
sleep(2)
clear()
usuario = {
	'nome':	input("informe seu nome(completo): "),
	'idade':input("qual a sua idade: "),
	'email':input("email: ")
}

#PEDIR CONFIRMAÇÃO DOS DADOS
clear()
print(f"NOME: 	{usuario['nome']}")
print(f"IDADE:	{usuario['idade']} anos")
print(f"EMAIL:	{usuario['email']}")

resposta = input("\n\tESTE DADOS ESTÃO CORRETOS? (S / N): ").upper()