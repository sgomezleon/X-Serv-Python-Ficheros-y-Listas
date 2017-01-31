#!/usr/bin/python3

# 13.4 Ficheros y listas

fich = open("/etc/passwd","r")
usuarios = fich.readlines()



for usuario in usuarios:
	print(usuario)
	nick = usuario[:usuario.find(':')]
	shell = usuario[usuario.rfind(':')+1:-1]
	print(nick,usuario.find(':'), shell,usuario.rfind(':'))

for usuario in usuarios:
	nick = usuario.split(':')[0]
	shell = usuario.split(':')[-1][:-1]
	print(nick, shell)
	
print('Numero de usuarios: ',len(usuarios))


fich.close()
