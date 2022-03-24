import socket
import sys


def main() -> object:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!!!')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso')

    HostAlvo = str(input('Digite o Host ou IP a ser conectado: '))
    PortaAlvo = int(input('Digite a porta a ser conectada: '))

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP conectado com Sucesso no Host' + HostAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar no Host: ' + HostAlvo)
        print('Erro: {}'.format(e))
        sys.exit()


if __name__ == '__main__':
    main()
