import json
# Importing built-in Python module 'json'
# This module helps us read and work with JSON files


def read_json(file_path):
    # Function to read JSON file
    # file_path = location of JSON file (e.g., "test_data/login_data.json")

    with open(file_path) as f:
        # Open the file in read mode || 👉 If you don’t specify mode, Python uses:
        # default mode = "r" (read mode)
        # 'f' is the file object (like a connection to the file)

        return json.load(f)
        # json.load(f) reads JSON content from file
        # and converts it into Python dictionary
        # Example:
        # JSON → {"username": "admin"}
        # Python → {"username": "admin"} (dict)