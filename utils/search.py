import os
import fnmatch

def find_files_with_string(string, path='.'):
    """
    Recursively searches for files containing a specified string in the current directory
    and all subdirectories.

    Args:
        string (str): The string to search for.
        path (str): The starting path for the recursive search (default is the current directory).

    Returns:
        A list of paths to all files containing the specified string.
    """
    file_paths = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*'):
            if string in open(os.path.join(root, filename)).read():
                file_paths.append(os.path.join(root, filename))
    return file_paths

def find_files_with_string_in_filename(string, path='.'):
    """
    Recursively searches for files with a specified string in their filename in the current directory
    and all subdirectories.

    Args:
        string (str): The string to search for in the filenames.
        path (str): The starting path for the recursive search (default is the current directory).

    Returns:
        A list of paths to all files with filenames containing the specified string.
    """
    file_paths = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if string in filename:
                file_paths.append(os.path.join(root, filename))
    return file_paths

def find_files_with_extension(extension, path='.'):
    """
    Recursively searches for files with a specified extension in their filename in the current directory
    and all subdirectories.

    Args:
        extension (str): The extension to search for in the filenames.
        path (str): The starting path for the recursive search (default is the current directory).

    Returns:
        A list of paths to all files with filenames ending in the specified extension.
    """
    file_paths = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(extension):
                file_paths.append(os.path.join(root, filename))
    return file_paths

def count_string_occurrences(file_path, target_string):
    """
    Counts the number of occurrences of a string in a file.
    """
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            count += line.count(target_string)
    return count

import pandas as pd

def count_missing_values(df):
    """
    Count the number of missing values in each column of a pandas data frame
    
    Args:
    - df: pandas data frame
    
    Returns:
    - pandas series with column names as index and number of missing values as values
    """
    return df.isnull().sum()
