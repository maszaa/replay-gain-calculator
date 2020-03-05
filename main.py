import sys

from calculate_rg import read_path

def main(argv):
  if len(argv) != 1:
    raise ValueError("Invalid amount of arguments passed, please pass one (input directory)")

  return read_path(argv[0])

if __name__ == "__main__":
  main(sys.argv[1:])
