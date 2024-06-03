def save_file(name, data):
    with open(name, 'w') as file:
        file.write(data)


def read_file(name):
    with open(name, 'r') as file:
        return file.read().strip()
