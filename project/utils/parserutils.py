def split(sequence: list, sep):
    """
    Splits sequence list into list of lists by sep value
    """
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk
