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


