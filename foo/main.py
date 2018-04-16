import foo.subpkg1
import foo.subpkg2

import argparse

def main():
    parser = argparse.ArgumentParser(prog='my_megazord_program')
    parser.add_argument('-i', nargs='?', help='help for -i blah')
    args = parser.parse_args()
    foo.subpkg1.f('foo.subpkg1.f')
    foo.subpkg2.f('foo.subpkg2.f')

if __name__ == "__main__":
    main()
