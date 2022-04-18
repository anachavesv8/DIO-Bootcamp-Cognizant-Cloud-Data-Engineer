import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') #algortimo

hash1.update(open(arquivo1, 'rb').read())  #faz a comparação do hash, rb= abertura em, modo binario

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():   #digest resume os dados passados pelo update
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')

