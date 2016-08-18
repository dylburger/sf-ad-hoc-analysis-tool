""" Helper functions
"""


def bytes_to_str(data):
    """ In Python 3, we need a function to decode binary to Unicode
    """
    if isinstance(data, bytes):
        value = data.decode('utf-8')
    else:
        value = data
    return value
