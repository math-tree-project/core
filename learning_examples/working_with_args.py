import argparse

parser = argparse.ArgumentParser("This is an argparse demo")

parser.add_argument('necessary', type=int, help ='This argument should always be supplied')
parser.add_argument('--flag', action='store_true', default=False, help='If you use this argument flag would be set to True, else it is False')
parser.add_argument('--filename', type=str, default='some_file.txt', help="Filename")


args=parser.parse_args()

print("""

Necessary argument is {}

Flag argument is {}

Filename argument is {}

""".format(args.necessary, args.flag, args.filename))