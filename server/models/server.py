from config.logging import logger
from server.models.string_processor import StringProcessor
import time
import socket
from threading import Thread

class Server:
    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.processor = StringProcessor()

    def handle_client(self, conn, address):
        with conn:
            logger.info(f'Connected by {address}')
            start_time = time.time()

            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                weight = self.processor.calculate_weight(data)
                conn.sendall(str(weight).encode('utf-8'))
            
            elapsed = time.time() - start_time
            logger.info(f'Process completed in {elapsed} seconds.')
    
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            logger.info(f'Server started in {self.host}:{self.port}')

            while(True):
                conn, address = s.accept()
                thread = Thread(target=self.handle_client, args=(conn, address))
                thread.start()