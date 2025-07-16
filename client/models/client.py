import time
import socket
from string_generator import StringGenerator
from ...config.logging import logger

class StringClient:
    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.generator = StringGenerator()

    def genereate_file(self, num_strings=1_000_000, filename="chain.txt"):
        with open(filename, 'w') as f:
            for _ in range(num_strings):
                s = self.generator.generate_string()
                f.write(s + '\n')

            logger.info(f'Generated {num_strings} strings in {filename}')

    def process_strings(self, input_file="chain.txt", output_file="results.txt"):
        start_time = time.time()

        with open(input_file, 'r') as infile, \
             open(output_file, 'w') as outfile, \
             socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            
            sock.connect((self.host, self.port))
            logger.info(f'Connected to server at {self.host}:{self.port}')

            for line in infile:
                string = line.strip()
                sock.sendall(string.encode('utf-8'))
                weight = sock.recv(1024).decode('utf-8')
                
                outfile.write(f'{string} | {weight}\n')

        elapsed = time.time() - start_time
        logger.info(f'Process completed in {elapsed} seconds')