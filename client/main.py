import argparse
from .models.client import StringClient

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="String Processing Client")
    parser.add_argument("-n", "--num_strings", type=int, default=1_000_000, help="Number of strings to generate")
    args = parser.parse_args()

    client = StringClient()
    client.genereate_file(args.num_strings)
    client.process_strings()