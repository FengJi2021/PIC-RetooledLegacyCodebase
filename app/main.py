import argparse
import sys
import traceback

# import app here

def main():
    # handle command line arguments
    # start app here
    print("Hello World!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # add arguments 
    args = parser.parse_args()
    
    # run main with arguments
    main()