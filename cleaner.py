def remove_nulls(data):
    return [item for item in data if item is not None]

def standardize_case(data):
    return [str(item).lower() for item in data]

def deduplicate(data):
    return list(set(data))
