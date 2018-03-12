#!/usr/bin/python
import datetime, getopt, os, random, string
import sys, time
from subprocess import call

def main(argv):
    string_type = string.ascii_letters
    string_length = 8
    record_file_path = ''
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
            if arg.__contains__('.'):
                name, suffix = arg.split('.')
                record_file_path = os.path.join(os.sep, 'tmp', record_file_path, name +'-'+ datetime.datetime.now().strftime('%a%Y%b%d%H%M%S' +'.'+ suffix))
            else:
                record_file_path = os.path.join(os.sep, 'tmp', record_file_path, arg + datetime.datetime.now().strftime('%a%Y%b%d%H%M%S'))
            print(record_file_path)
        elif opt == '-d':
            delay = float(arg)
        elif opt == '-r':
            replay_file_path = arg
            print(replay_file_path)

    fuzzy_out(string_type, string_length, delay, record_file_path, replay_file_path) 


def fuzzy_out(string_type, string_length, delay=0, record_file='', replay_file=''):
    out = generate_string(string_type, string_length)
    if len(replay_file) > 0 and os.path.exists(replay_file):
        rp = open(replay_file, 'r')
        print(rp.read())
        rp.close()
        return

    if delay == 0:
        print(out)
    else:
        for s in out:
            time.sleep(delay)
            print(s)
    
    if len(record_file) > 0:
        rf = open(record_file, 'wb')
        rf.write(out +'\n')
        rf.close()


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

