import sys
import fileinput
import re
import argparse

parser = argparse.ArgumentParser(description="Faux grep")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-f", dest="show_file_name", action="store_true", help="Show file name")
parser.add_argument("-c", dest="count_lines", action="store_true", help="Show line count")

parser.add_argument("pattern", help="pattern to find")

parser.add_argument("files", nargs="*", help="files to search")

args = parser.parse_args()  # process sys.argv by default

rx_pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)

line_count = 0

for raw_line in fileinput.input(args.files):  # for each file in sys.argv, open and read one line at a time
    if rx_pattern.search(raw_line):
        if not args.count_lines:
            if args.show_file_name:
                print(fileinput.filename(), end=': ')
            line = raw_line.rstrip()
            print(line)
        line_count += 1

print(line_count)


perl = """
while (my $line = <>) {
    ;
}
"""
