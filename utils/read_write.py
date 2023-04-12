import pickle
import numpy as np
import pandas as pd
import os

def read_pickle_file(file_path):
    """
    Reads a pickled file and returns the object stored in the file.

    Args:
        file_path (str): The path to the pickled file.

    Returns:
        The object stored in the pickled file.
    """
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

def read_last_line(file_path):
    """
    Reads the last line of a file.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        The last line of the file as a string.
    """
    with open(file_path, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        return f.readline().decode().strip()

import zipfile

def read_csv_from_zip(zip_file_path, csv_file_name):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        with zip_file.open(csv_file_name) as csv_file:
            df = pd.read_csv(csv_file)
            return df

import requests
from io import BytesIO

def read_csv_from_url(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Get the content of the response
    content = response.content

    # Create a BytesIO object from the content
    zipfile_bytes = BytesIO(content)

    # Create a ZipFile object from the BytesIO object
    with zipfile.ZipFile(zipfile_bytes, "r") as zip_ref:
        # Extract the CSV file from the ZIP file
        csv_file = zip_ref.read(filename)

    # Create a Pandas dataframe from the CSV data
    df = pd.read_csv(BytesIO(csv_file))

    return df


def write_pickle_file(file_path, data):
    """
    Writes a pickled file with the given data.

    Args:
        file_path (str): The path to the pickled file.
        data (object): The object to be pickled.
    """
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def save_to_csv_file(array, file_path):
    """
    Saves a numpy array to a CSV file.

    Args:
        array (ndarray): The numpy array to be saved.
        file_path (str): The path to the output CSV file.
    """
    np.savetxt(file_path, array, delimiter=',')

def save_dataframe_to_csv(df, file_path):
    """
    Saves a Pandas DataFrame to a CSV file.

    Args:
        df (DataFrame): The Pandas DataFrame to be saved.
        file_path (str): The path to the output CSV file.
    """
    df.to_csv(file_path, index=False)


