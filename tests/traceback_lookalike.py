import sys

print('  File "tests/traceback_lookalike.py", line 4, in report', file=sys.stderr)
print("    informational context", file=sys.stderr)
print("not actually a Python exception", file=sys.stderr)
sys.exit(1)
