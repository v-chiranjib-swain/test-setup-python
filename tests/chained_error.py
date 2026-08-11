try:
    1 / 0
except ZeroDivisionError as error:
    raise RuntimeError("wrapped") from error