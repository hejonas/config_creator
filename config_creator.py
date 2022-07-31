# config_creator.py

import sys
import os
import argparse
import logging
import glob

def get_containing_defines_in_file(f):
    """
    Returns a list of all possible defines in a file

    Keyword arguments:
    f -- file handle to input file
    """
    included_defines = []

    for line in f:
        # Find every #ifdef
        if line.startswith('#ifdef '):
            included_defines.append(line[len('#ifdef '):])

        # Find every #ifndef
        if line.startswith('#ifndef '):
            included_defines.append(line[len('#ifndef '):])

        # TODO: Find every #if defined(XYZ)
        # TODO: Find every #if defined(XYZ) || defined(ZYX)

    return included_defines


def generate_config_file(defines):
    """
    Generates a config file with all possible defines in a path
    commented out.

    Keyword arguments:
    defines -- list of defines to include in config file
    """
    f = open("config_file.h", 'w')
    for define in defines:
        f.write("//#define {}\n".format(define))
    f.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Generates a config file template for a C repository'
    )
    parser.add_argument('Path',
        metavar='path',
        type=str, 
        help='path of the top level folder') 

    parser.add_argument('--loglevel',
        type=str,
        default='WARNING',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set level of logging. Default is warning.')
    
    args = parser.parse_args()

    input_path = args.Path
    loglevel = args.loglevel

    # Configure logger
    # TODO: consider having an option for inputting the log file name
    logging.basicConfig(filename='log.log',
                        filemode='w',
                        level=loglevel) 

    if not os.path.isdir(input_path):
        logging.error('The path specified does not exist')
        sys.exit(1)

    defines_in_path = []
    for filename in glob.glob(os.path.join(input_path, '**/*.c'), recursive=True):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            logging.info('Searching file: {}'.format(filename)) 
            defines_in_path.extend(get_containing_defines_in_file(f))
    
    # Remove doubles
    defines_in_path = list(dict.fromkeys(defines_in_path))

    generate_config_file(defines_in_path)

    sys.exit(0)