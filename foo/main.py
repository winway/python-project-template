import foo

import argparse

def main():
    parser = argparse.ArgumentParser(prog='my_megazord_program')
    parser.add_argument('-i', nargs='?', help='help for -i blah')
    args = parser.parse_args()
    foo.helloworld(args.i)

if __name__ == "__main__":
    foo.helloworld("main")
