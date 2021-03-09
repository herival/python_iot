# exo cmd.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("test", type=float)
args = parser.parse_args()
print(args.test)