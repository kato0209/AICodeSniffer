import socket



host_ip = socket.gethostbyname(socket.gethostname())        #ホストのIPを取る
port = 1890

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ソケット作成

server.bind((host_ip, port))                                #IPとポート結び付け

server.listen(1)                                            #接続数

print ("[*]Server waiting on %s : %s" % (host_ip, port))    

client, addr = server.accept()                              

print ("[Connection from %s:%s ]" % (addr[0], addr[1])) 



def input_encode():                                         #送るメッセージ入力
    data = input("[Server] > ")

    if data == "exit":                                      #終了条件
        client.send(b'exit')
        print ("////Finish Connect////")
        server.shutdown(1)
        server.close()
        exit()

    else:
        data = data.encode('utf-8')                         #エンコード
        return data

def decode(response):                                       #デコード 
    response = response.decode()

    if response == "exit":                                  #終了条件
        print ("////Finish Connect////")
        client.close()
        exit()

    return response



while True:
    response_data = client.recv(1024)                       #データ受け取り
    response_data = decode(response_data)
    print ("[Client] > %s " % (response_data))              

    client.send(input_encode())                             #メッセージ送信
