#!/usr/bin/env python3
"""a module that create a file"""
import os
import json

def create(filename, title='', body=''):
    """
     a function that handle file creation and input title and body
     Args:
        filename: name of the file create
        title: title of the document
        body: information to be contained in file
    """
    try:
        if os.path.exists(f'{filename}.json'):
            raise FileExistsError("Cannot create file, filename already exist")
        with open(f'{filename}.json', 'w') as file:
            content = {"title": title, "body": body}
            json.dump(content, file, indent = 4)
            return True
    except Exception as e:
        print(f'An error occured: {e}')
        return False