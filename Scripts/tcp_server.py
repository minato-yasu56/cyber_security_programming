import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # サーバーの接続待ちIPアドレスとポート番号を指定
    server.bind((IP, PORT))
    # 最大接続数を5に設定して、待ち受けを開始するようにサーバーを指示する
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # client変数にクライアントのソケットを、address変数にリモート接続の詳細を受け取る
        client, address = server.accept() # def accept() -> tuple[socket, _RetAddress]
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()