# Advent of Code 2023
  
This is a repository for tackling the 2023 Advent of Code Challenge set.  
Each day will be given its own folder, and we will work through them one-by-one.  
  
## To test a solution
  
To test a solution to a challenge, use `pytest` to run the test in that challenge's folder.  
Find an installation of Python 3 on your machine, use 3.10 if you can (since that's our company's target version)  
Once you do, create a virtual environment, activate it, and then install `pytest` into that environment, as in  
  
```bash
cd path/to/aoc2023
path/to/python3 -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

Now, test the solution by running pytest like so  
  
```bash
pytest 1-trebuchet
```
  
Puzzle inputs are specific to each user in Advent of Code, so they are ignored by git.  
Test inputs come from the body of the challenge, so they are not, like in https://adventofcode.com/2023/day/1.  
Once the test(s) pass(es), you will need to get your unique Puzzle Input for a challenge and add it to the appropriate folder.  
For day 1, you can get your input here: https://adventofcode.com/2023/day/1/input  
Copy the contents of that page into `1-trebuchet/input` and then run your solution code like so:  
  
```bash
python 1-trebuchet/solution.py
```
  
The output (your challenge submission) will then be printed to the console.  
Submit and progress, rinse and repeat~
