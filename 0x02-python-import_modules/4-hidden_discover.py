#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4.pyc

    names = dir(hidden_4.pyc)
    for name in names:
        if name[:2] != "__":
            print(name)