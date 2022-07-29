# config_creator.py

import sys
import os
import argparse
import string

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description='Generates a config file template for a C repository'
    )
    parser.add_argument('Path',
        metavar='path',
        type=str, 
        help='path of the top level folder') 
    
    args = parser.parse_args()

    input_path = args.Path
    
    if not os.path.isdir(input_path):
        print('The path specified does not exist')
        sys.exit(1)

    print('\n'.join(os.listdir(input_path)))
    
    sys.exit(0)