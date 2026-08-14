import builtins
import sys


exception_name = sys.argv[1]
exception_type = getattr(builtins, exception_name)
raise exception_type("built-in exception fixture")
