from types import FunctionType
from inspect import getmembers


def api(obj):
    return [name for name in dir(obj) if name[0] != '_']


def attrs(obj):
    disallowed_properties = {
        name for name, value in getmembers(type(obj)) 
            if isinstance(value, (property, FunctionType))}
    return {
        name: getattr(obj, name) for name in api(obj) 
            if name not in disallowed_properties and hasattr(obj, name)}

# for attr in dir(self):
#     print("%s=%r" % (attr, getattr(self, attr)))