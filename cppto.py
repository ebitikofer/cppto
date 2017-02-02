#!/usr/bin/python

# Eric Bitikofer
# 01.31.17
# CS 3200 Project 1
# A Python program that takes a valid C++ program and converts it to a Python 3 program. 

#You may design your program to quit if the number of arguments is incorrect or
# prompt the user for the missing file names.

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is', inputfile
    print 'Output file is', outputfile
    infile = open(inputfile, 'r')
    for line in infile:
        print line
if __name__ == "__main__":
    main(sys.argv[1:])
        #if letter A-z
            #if space after, assignment
                 # if x = 1;
                    #then x = 1
            #if letters after
                #if space after
                    #if letter after, variable dec
                        # if int x = 1;
                            #x = 1
                    #if << or >> after, i/o
                        # if cout << x;
                            #print x, (comma for not endl)
                        # if cin >> x;
                            #x = input("Enter two integers ")
                #if () after
                    #if { after, blocks
                        # if blocks ('{' and '}' on separate lines)
                            #something
                        # if int main(){}
                            #def main():
                        # if if(){}
                            #if :
                        # if while(){}
                            #while :
                    #if nothing after, function
                        # if if(){}
                            #if :
                        # if while(){}
                            #while :

        #elif symbol / or #
            #if / after, comment
                # if line = //
                    ##
            #if include after, 
                # if line = #include || using
                    #ignore

#Graduate students:
#Your program should also recognize:
# Functions other than main and function calls.
# Comments at the end of the line

#Programming style:
# Documentations throughout the program
# Documentation of each the functions, their parameters, and their return values.
# Use meaningful identifier (variable) names
# Use lower case letters for identifier names.
# Add spaces around operators
# Use uppercase for constants
# Skip lines between logical groups of statements
# Break long statements into either multiple statements or multiple lines