
# Created using Python 3 
__author__ = "Henry Blackie"
__copyright__ = "Copyright (C) 2019 Henry Blackie"
__license__ = "MIT License"
__version__ = "0.1"

import argparse # for parsing arguments
import datetime # for utilising date and time values
import hashlib # for file hashing
import os # for managing file paths

# define import arguments
parser = argparse.ArgumentParser(description="Command line tool, designed for parsing drone flight logs")
parser.add_argument('-importPath', help='filepath to flight log')
parser.add_argument('-droneModel', type=str, choices=['phantom3', 'phantom4', 'mavic2'], help='drone model associated with flight log')

# process arguments and assign to variables
args = parser.parse_args()

if args.importPath is not None:
    inputLogPath = args.importPath
else:
    inputLogPath = input("Input source file path: ")

if args.droneModel is not None:
	droneModel = args.droneModel

# verify import path
if os.path.isfile(inputLogPath):
    # import file if path is correct
    inputLogName = os.path.basename(inputLogPath)
    print(datetime.datetime.now().strftime('%H:%M:%S') + "\t" + "Located " + inputLogName)

    # hash file before processing
    inputLog = open(inputLogPath, 'rb')
    inputContents = inputLog.read()
    inputMD5 = hashlib.md5()
    inputSHA1 = hashlib.sha1()

    inputMD5.update(inputContents)
    print(datetime.datetime.now().strftime('%H:%M:%S') + "\t" + "MD5 Hash: " + inputMD5.hexdigest())
    inputSHA1.update(inputContents)
    print(datetime.datetime.now().strftime('%H:%M:%S') + "\t" + "SHA1 Hash: " + inputSHA1.hexdigest())

    inputContents = inputLog.read(128)
    print(inputContents)
else:
    print("Invalid file path")
    exit()