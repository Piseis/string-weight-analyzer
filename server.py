import logging
import time
import socket
from threading import Thread

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='server.log',
    filemode='w'
)
logger = logging.getLogger(__name__)


class StringProcessor:

    @staticmethod
    def calculate_weight(string):
        letters = sum(c.isalpha for c in string)
        numbers = sum(c.isdigit for c in string)
        spaces = string.count(' ')

        return (letters * 1.5 + numbers * 2) / spaces
    

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