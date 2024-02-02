import sys

#  sys.stdin  sys.stdout  sys.stderr

print("All is well")

print("Whoopsie", file=sys.stderr)

word = sys.stdin.readline()

print(f"{word = }")
