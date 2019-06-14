from os import path


def load_text(data_dir, filename):
    filepath = path.join(data_dir, filename)
    with open(filepath, 'r') as infile:
        return infile.read()


def load_data(data_dir, filename):
    filepath = path.join(data_dir, filename)
    with open(filepath, 'r') as infile:
        return infile.readlines()


def parse_data(data):
    rows = []
    for raw in data:
        parsed = raw.strip().split(',')
        rows.append(parsed)
    return rows


def fetch_data(data_dir, filename):
    raw_data = load_data(data_dir, filename)
    cleaned_data = parse_data(raw_data)
    return cleaned_data
