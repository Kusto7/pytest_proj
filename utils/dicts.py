# файл dicts.py
def get_val(collection, key, default='git'):
    if collection:
        for k, v in collection.items():
            if key == k:
                return v
            else:
                return default
    else:
        return default

