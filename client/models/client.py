import time
import socket
from client.models.string_generator import StringGenerator
from config.logging import logger

class StringClient:
    """
    A client class that handles string generation and server communication.
    
    Responsibilities:
    - Generate files containing random strings following specific rules
    - Send strings to a server for processing
    - Handle and store the server's responses
    
    Args:
        host (str): Server host address. Defaults to 'localhost'.
        port (int): Server port number. Defaults to 65432.
    """

    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.generator = StringGenerator()

    def generate_file(self, num_strings=1_000_000, filename="chain.txt"):
        """
        Generate a file containing random strings.
        
        Args:
            num_strings (int): Number of strings to generate. Defaults to 1,000,000.
            filename (str): Output file name. Defaults to "chain.txt".
            
        Note:
            Uses StringGenerator to create each string with proper formatting rules.
            Logs the completion of file generation.
        """
        with open(filename, 'w') as f:
            for _ in range(num_strings):
                s = self.generator.generate_string()
                f.write(s + '\n')

            logger.info(f'Generated {num_strings} strings in {filename}')

    def process_strings(self, input_file="chain.txt", output_file="results.txt"):
        """
        Process strings through the server and store results.
        
        Args:
            input_file (str): File containing strings to process. Defaults to "chain.txt".
            output_file (str): File to store processed results. Defaults to "results.txt".
            
        Process:
            1. Establishes connection with the server
            2. Sends each string for processing
            3. Receives and stores the weight metrics
            4. Excludes strings that trigger the 'double a' rule (weight=1000)
            5. Logs the total processing time
            
        Note:
            The format of results is: "original_string | calculated_weight"
        """
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
                if weight != "1000":
                    outfile.write(f'{string} | {weight}\n')

        elapsed = time.time() - start_time
        logger.info(f'Process completed in {elapsed} seconds')