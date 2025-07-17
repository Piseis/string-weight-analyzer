import argparse
from server.models.server import Server

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="String Processing Server")
    parser.add_argument("-p", "--port", type=int, default=65432, help="Port number to run the application")
    args = parser.parse_args()

    server = Server(port=args.port)
    server.start()