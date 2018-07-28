import socket


def testarConexao(ip, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((str(ip), int(porta)))
    sock.close()

    return result == 0


def mantemAnalise(ip, inicio, fim):
    for i in range(inicio, fim + 1):
        r = testarConexao(ip, i)

        if r:
            print 'PORTA {:4d}'.format(i) + ': ABERTA'
        else:
            print 'PORTA {:4d}'.format(i) + ': FECHADA'


def inicio():
    #ip = '10.125.229.195'
    ip = 'www.google.com'
    inicio = input('Entre com o valor inicial da porta..: ')
    fim = input('Entre com o valor final da porta....: ')
    mantemAnalise(ip, inicio, fim)


if __name__ == '__main__':
    inicio()
