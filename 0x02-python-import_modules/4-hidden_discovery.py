#!/usr/bin/python3
if __name__ == "__main__":
    """task 4."""
    import hidden_4
    result = dir(hidden_4)
    for i in range(result):
        if i[:2] != "__":
            print(i)
