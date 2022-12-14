# Span back end coding challenge solution
Note that only the Python files corresponding to the command line application itself (league_rank.py) and the PyTest (league_rank_test.py) have been Git included.

The only dependencies are standard Python libraries and the PyTest package.

The application can be run from the command line (see <b>python league_rank.py -h</b> for usage). The \<inputfile> and \<outputfile> paths are relative to the root directory (e.g. myinput.txt, myoutput.txt).

Testing is done using <b>python -m pytest league_rank_test.py</b> and places input and output files for comparison in a <b>/test</b> directory that is created if it doesn't exist. Three tests have been written handling:

1. the expected input and output from the problem description
2. teams with multiple spaces in names 
3. the single match edge case.
