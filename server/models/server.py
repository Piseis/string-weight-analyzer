from config.logging import logger
from server.models.string_processor import StringProcessor
import time
import socket
from threading import Thread

class Server:
    """
    A multi-threaded server that processes string metrics from clients.
    
    The server handles multiple client connections simultaneously, calculating string weights
    according to specific business rules and logging processing information.
    
    Args:
        host (str): Host address to bind the server. Defaults to 'localhost'.
        port (int): Port number to listen on. Defaults to 65432.
        
    Attributes:
        processor (StringProcessor): Instance responsible for string metric calculations.
    """

    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port
        self.processor = StringProcessor()

    def handle_client(self, conn, address) -> None:
        """
        Handle communication with a single client connection.
        
        Args:
            conn (socket.socket): The client connection socket.
            address (tuple): Client address (host, port).
            
        Process:
            1. Receives strings from the client
            2. Checks for double 'a' pattern
            3. Calculates string weight using StringProcessor
            4. Sends back the calculated weight
            5. Logs processing time and special cases
            
        Note:
            - Special case (double 'a') returns weight 1000 and logs a warning
            - Processing time is logged when connection ends
        """
        with conn:
            logger.info(f'Connected by {address}')
            start_time = time.time()

            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                if self.processor.has_double_a(data):
                    weight = 1000
                    logger.warning(f"Double 'a' rule detected >> '{data}'")
                else:
                    weight = self.processor.calculate_weight(data)

                conn.sendall(str(weight).encode('utf-8'))
            
            elapsed = time.time() - start_time
            logger.info(f'Process completed in {elapsed} seconds.')
    
    def start(self) -> None:
        """
        Start the server and listen for incoming connections.
        
        Creates a main listening socket that spawns a new thread for each client connection.
        Runs indefinitely until manually stopped.
        
        Note:
            - Uses threading to handle multiple clients concurrently
            - Logs server startup information
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            logger.info(f'Server started at {self.host}:{self.port}')

            while True:
                conn, address = s.accept()
                thread = Thread(target=self.handle_client, args=(conn, address))
                thread.start()