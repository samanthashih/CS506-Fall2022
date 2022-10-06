import csv;

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file_lines= []
    with open(csv_file_path) as f:
        lines = list(f.readlines())
        print(lines)
        for line in lines:
            file_lines.append(line)

    f.close()
    return file_lines