class CustomFailure(Exception):
    pass


CustomFailure.__module__ = "package.errors"
raise CustomFailure("qualified failure")
