def read_classification_from_file(path: str):
    dictionary = {}
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            dictionary[line.split(' ')[0]] = line.strip('\n').split(' ')[1]
    return dictionary