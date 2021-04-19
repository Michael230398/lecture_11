import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    return data[field]

def linear_search(sequence, number):
    indices = []
    count = 0
    idx = 0
    while idx < len(sequence):
        if sequence[idx] == number:
            count += 1
            indices.append(idx)
        idx += 1
    return {"position": indices, "count": count}










def main():
    sequence = (read_data("sequential.json", "unordered_numbers",))
    print(sequence)
    results = linear_search(sequence, 0)
    print(results)


if __name__ == '__main__':
    main()