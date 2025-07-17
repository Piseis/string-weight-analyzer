import argparse
from .models.client import StringClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="String Processing Client")
    parser.add_argument("-n", "--num_strings", type=int, default=1_000_000, help="Number of strings to generate")
    parser.add_argument("-ht", "--host", type=str, default='localhost', help="Host of server application")
    parser.add_argument("-p", "--port", type=int, default=65432, help="Port of server application")
    args = parser.parse_args()

    client = StringClient(host=args.host, port=args.port)
    client.genereate_file(args.num_strings)
    client.process_strings()