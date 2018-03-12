#!/usr/bin/python
import datetime, getopt, os, random, string
import sys, time
from subprocess import call

def main(argv):
    string_type = string.ascii_letters
    string_length = 8
    record_file_path = os.path.join(os.path.sep, 'tmp')
    delay = 0
    replay_file_path = ''

    try:
        opts, args = getopt.getopt(argv, 'hpa0nl:f:d:r:', ['length=', 'file=', 'delay=', 'file='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-p':
            string_type = string.printable
        elif opt == '-a':
            string_type = string.ascii_letters
        elif opt == '-0':
            string_type = string.ascii_letters + u"\u0000"
            print(string_type)
        elif opt == '-n':
            string_type = string.digits
        elif opt == '-l':
            string_length = random.randrange(int(arg) + 1)
        elif opt == '-f':
            if arg.__contains('.'):
                arg.split('.')
            record_file_path = os.path.join(record_file_path, arg + datetime.datetime.now().strftime('%a%Y%b%d%H%M%S'))
            print(record_file_path)
        elif opt == '-d':
            delay = float(arg)
        elif opt == '-r':
            replay_file = arg + datetime.datetime.now().strftime('%a%Y%b%d%H%M%S')
            print(replay_file)

    fuzzy_out(string_type, string_length, delay) 


def fuzzy_out(string_type, string_length, delay=0):
    out = generate_string(string_type, string_length)
    if delay == 0:
        print(out)
    else:
        for s in out:
            time.sleep(delay)
            print(s)


def usage():
    print('usage: string-generator.py <program> <program arguments> <options> <arguments>')
    print('-h           prints this help')
    print('-p           generate only the printable ASCII characters')
    print('-a           generate all ASCII characters')
    print('-0           include the null (0 byte) character')
    print('-n           generate only digits')
    print('-l <range>   generate random length lines within <range> (\\n terminated strings)')
    print('-f <name>    record characters in file <name>')
    print('-d <seconds> waits <seconds> following each character')
    print('-r <name>    replay characters in file <name> to output')


def generate_string(string_type, length):
    return ''.join(random.choice(string_type) for i in range(length))


if __name__ == "__main__":
   main(sys.argv[1:])

