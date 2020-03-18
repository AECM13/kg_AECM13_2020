import argparse
import sys

##############################################################################
def map_char(s1, s2):
    count = {}
    counter = 0
    match = 0

    if len(s1) != len(s2):
        print("false")
    else:
        for char in s1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for key in count:
            if count[key] > 1:
                print("false")
                break
            else:
                match += 1
    if len(s1) == match:
        print("true")

##############################################################################
def main():

    if len(sys.argv) <2:
        print("Missing arguments")
        sys.exit(0)
    if len(sys.argv) < 1:
        print("One more argument needed")
        sys.exit(0)

    parser = argparse.ArgumentParser(description="mapping")
    parser.add_argument(action='store',dest='s1', type=str)
    parser.add_argument(action='store',dest='s2', type=str)

    options = parser.parse_args()

    s1 = options.s1
    s2 = options.s2

    map_char(s1,s2)


main()
