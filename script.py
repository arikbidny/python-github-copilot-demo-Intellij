# Calculate the days between  two dates and print the result
# Usage: python script.py 2020-01-01 2020-01-10

import sys
from datetime import datetime

def main():
    if len(sys.argv) != 3:
        print('Usage: python script.py <date1> <date2>')
        sys.exit(1)

    date1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
    date2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')

    delta = date2 - date1
    print(f'There are {delta.days} days between {date1} and {date2}')

if __name__ == '__main__':
    main()

# Run the script
# python script.py 2020-01-01 2020-01-10


