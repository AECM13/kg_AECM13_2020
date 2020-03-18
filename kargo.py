import argparse
'''
Question:
Determine whether a one-to-one character mapping exists from one string, s1, to another string,
s2.
For example, given ​ s1 = abc ​ and ​ s2 = bcd , ​ print "​ true" into stdout ​ since we can map each
character in "abc" to a character in "bcd".
Given ​ s1 = foo ​ and ​ s2 = bar ​ , print "​ false" ​ since the character ‘o’ cannot map to two characters.
But given ​ s1 = bar a
nd ​ s2 = foo ​ , print "true​ " ​ since each character in "bar" can be mapped to a
character in "foo"
'''


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

def main():

    parser = argparse.ArgumentParser(description="mapping")
    parser.add_argument(action='store',dest='s1', type=str)
    parser.add_argument(action='store',dest='s2', type=str)

    options = parser.parse_args()

    s1 = options.s1
    s2 = options.s2

    map_char(s1,s2)

main()
