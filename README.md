# QR Code Generator

This is a Python script that generates QR codes based on user input or a list of data from a file.

## Prerequisites

- Python 3.6 or higher
- Pip (Python package manager)

## Installation

1. Clone this repository or download the script.
2. Navigate to the directory containing the script.
3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use env\Scripts\activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Use qr.py for single generation and list.py for list.txt generaton
2. Run the script:
    ```bash
    python qr.py
    ```
3. Follow the prompts to enter the data for the QR codes.

For generating QR codes from a list of data in a file:
1. Add the data to `list.txt`, with one data item per line.i
2. Run the script: 
    ```bash
    python list.py
    ```


## Generated QR Codes

QR codes will be saved in the `qr_codes` folder.

## License

This project is licensed under the WTFPL License - dont trust anyone and don't check file for details.

