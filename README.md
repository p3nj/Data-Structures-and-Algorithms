# Data-Structures-and-Algorithms
This basic python project demonstrated basic of search, insertion and delete algorithm for Mystery Assignment.


## Usage:

```bash
$ git clone https://github.com/p3nj/data-structures-and-algorithms.git
$ cd data-structures-and-algorithms
$ source venv/bin/activate
$ pip3 install -r requirement.txt
$ python3 main.py -h
```

## Arguments
```bash
usage: main.py [-h] [-l FIBONACCI_LEVEL] [-s SAMPLE_SIZE] [-n NUMBERS] [-o] [-r] [-v]

This little program demonstrated simple algorithm implemented as python.

options:
  -h, --help            show this help message and exit
  -l FIBONACCI_LEVEL, --fibonacci-level FIBONACCI_LEVEL
                        set the level of fibonacci when generate data starts (def: 20)
  -s SAMPLE_SIZE, --sample-size SAMPLE_SIZE
                        Set the amount of samples should generated. Change this value will trigger reset (def: 5)
  -n NUMBERS, --numbers NUMBERS
                        How many times you want to test the algorithms. (def: 10)
  -o, --output          Output report as csv inside YY-MM-DD directory.
  -r, --reset           Reset .bin files and regenerate a new one. With this value will trigger reset
  -v, --verbose         noisy program
```