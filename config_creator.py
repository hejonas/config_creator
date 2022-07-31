# config_creator.py

import sys
import os
import argparse
import logging
import glob

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

    for filename in glob.glob(os.path.join(input_path, '**/*.c'), recursive=True):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            logging.info('Searched file: {}'.format(filename)) 
    
    sys.exit(0)