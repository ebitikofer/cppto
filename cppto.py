#!/usr/bin/python

# Eric Bitikofer
# 01.31.17
# CS 3200 Project 1
# A Python program that takes a valid C++ program and converts it to a Python 3 program. 

#You may design your program to quit if the number of arguments is incorrect or
# prompt the user for the missing file names.

import sys, getopt, re #import argv, exit, parser, and regular expressions

tokens = [ 'A-z', 'include', 'using', 'main', 'if', 'else', 'do', 'while', 'for', 'cout', 'cin', '0-9', ' ', ';', '+', '-', '*', '/', '=', '<', '>', '(', ')', '{', '}', '[', ']', '#' ]

def main(argv): #main with input 
    infile = '' #declared input file string
    outfile = '' #declared output file string
    try: #try block for argument check 
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="]) #parse funtion for cmdline arguments
    except getopt.GetoptError: #option error?
        print('Option not allowed') #print proper format of arguments
        print('program.py -i <infile> -o <outfile>') #print proper format of arguments
        sys.exit(2) #exit with error code 2 signifying a command line syntax error
    if 1 > len(argv) > 4:
        print('Too many arguments') #print proper format of arguments
        print('program.py -i <infile> -o <outfile>') #print proper format of arguments
        sys.exit()
    for opt, arg in opts: #loop through arguments looking for the input file and output file
        if opt == '-h': #-h for help prompt
            print('test.py -i <infile> -o <outfile>') #print proper format of arguments
            sys.exit() #exit
        elif opt in ("-i", "--ifile"): #if -i option
            infile = arg #take in its argument
        elif opt in ("-o", "--ofile"): #if -o option
            outfile = arg #take in it argument
    isfile = open(infile, 'r') 
    strs = [] #"" for line in isfile]
    pattern = " +"
    for line in isfile:
        #print(line)
        print(line.split())
    #print(strs)
        #get and parse the line into tokens


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

if __name__ == "__main__":
    main(sys.argv[1:])

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