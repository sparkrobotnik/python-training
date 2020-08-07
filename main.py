from custom_utils import clear
from time import sleep

app_config = {
	'nome':		"library assistant",
	'versao': "1.0",
	'autor':	"spark robotnik"
}
usuario = {
	'nome':		"",
	'idade':	0,
	'email':	""
}

#MOSTRAR INFORMACOES DO APP
clear()
print(f"{app_config['nome']} versão: {app_config['versao']} - autor: {app_config['autor']}")

#PEDIR CREDENCIAIS DO USUARIO
sleep(2)

resposta = "";
while resposta != "S":
	resposta = ""
	
	clear()
	
	print("\t———CADASTRO DE USUARIO———\n")
	usuario['nome']	= input("NOME(COMPLETO): ")
	usuario['idade']= input("IDADE:\t\t")
	usuario['email']= input("EMAIL:\t\t")
	
	#PEDIR CONFIRMAÇÃO DOS DADOS
	while resposta != "S" and resposta != "N":
		clear()
		
		print("\t———CONFIRMAÇÃO DE DADOS———\n")
		print(f"NOME: 	{usuario['nome']}")
		print(f"IDADE:	{usuario['idade']} anos")
		print(f"EMAIL:	{usuario['email']}")
		
		resposta = input("\n\tESTE DADOS ESTÃO CORRETOS? (S / N): ").upper()