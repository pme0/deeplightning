import argparse

import requests


parser = argparse.ArgumentParser()
parser.add_argument(
    "file_path",
    type=str,
    default=None,
    help="Checkpoint name",
)
parser.add_argument(
    "--host",
    type=str,
    default="127.0.0.1",
    help="Host address",
)
parser.add_argument(
    "--port",
    type=int,
    default=5000,
    help="Host port",
)
parser.add_argument(
    "--service",
    type=str,
    default="predict",
    help="Service name",
)
args = parser.parse_args()


url = f"http://{args.host}:{args.port}/{args.service}/"


with open(args.file_path, "rb") as f:
    # Equivalent to 
    # ```bash 
    # curl -X 'POST' 'http://127.0.0.1:5000/predict/' -F 'file=@<FILEPATH>' `
    # ```
    response = requests.post(url, files={"file": f})


try:
    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError as http_e:
    print(f"HTTP Error: {http_e}")

except Exception as e:
    print(f"Error: {e}")
