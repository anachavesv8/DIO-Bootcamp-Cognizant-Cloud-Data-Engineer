import random
import string

tamanho = int(input('Digite o tmanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + '!@#$%*()-=+'

rnd = random.SystemRandom() #os.urandom gera numero aleatorios

print(''.join(rnd.choice(chars) for i in range(tamanho))) #rnd.choice, retorna uma lista com numero randomicos, charas vai passar uma letra, e vai gerar um numero, ate chegar no tamanho de 16 caracters.
