# String Analyzer Solution

## Overview

This project implements a scalable and configurable client-server solution for analyzing string metrics according to specific business rules. The client generates a file with random strings, sends them to the server via sockets, and stores the server's analysis results. The server processes each string, applies the required rules, and returns the calculated metric.

## Features

-   Generates at least 1,000,000 random strings with specific formatting rules
-   Sends strings from client to server using TCP sockets
-   Server calculates a custom metric for each string
-   Special handling and logging for strings with double 'a' (case-insensitive)
-   Multi-threaded server for scalability
-   Configurable parameters (number of strings, host, port)
-   Uses only Python built-in libraries
-   Centralized logging for both client and server

## Directory Structure

```
Solution/
├── client/
│   ├── main.py
│   └── models/
│       ├── client.py
│       └── string_generator.py
├── server/
│   ├── main.py
│   └── models/
│       ├── server.py
│       └── string_processor.py
├── config/
│   └── logging.py
├── chain.txt
├── results.txt
├── .gitignore
└── README.md
```

## Installation

1. **Requirements:**

    - Python 3.7 or higher
    - No external dependencies (uses only Python standard library)

2. **Clone the repository:**
    ```sh
    git clone https://github.com/Piseis/string-weight-analyzer.git
    cd string-weight-analyzer
    ```

## Configuration

-   **Logging:**
    -   Logging is configured in `config/logging.py`.
-   **Client Parameters:**
    -   Number of strings, server host, and port can be set via command-line arguments.
-   **Server Parameters:**
    -   Server port can be set via command-line arguments.

## Usage

### 1. Start the Server

Run the following command to start the server (default port: 65432):

```sh
python -m server.main --port 65432
```

### 2. Run the Client

Generate strings and process them through the server:

```sh
python -m client.main --num_strings 1000000 --host localhost --port 65432
```

-   `--num_strings`: Number of strings to generate (default: 1,000,000)
-   `--host`: Server host (default: localhost)
-   `--port`: Server port (default: 65432)

### 3. Output Files

-   `chain.txt`: Contains the generated strings (one per line)
-   `results.txt`: Contains the original string and its calculated metric, separated by `|`
