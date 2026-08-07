import sys

print("Traceback (most recent call last):", file=sys.stderr)
print('  File "tests/legacy_traceback.py", line 4, in <module>', file=sys.stderr)
print("    items[1]", file=sys.stderr)
print("IndexError: list index out of range", file=sys.stderr)
sys.exit(1)
