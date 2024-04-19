import os

def remove_duplicate_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    line_counts = {}
    for line in lines:
        line_counts[line] = line_counts.get(line, 0) + 1

    filtered_lines = [line for line in lines if line_counts[line] <= 2]
    
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                remove_duplicate_lines(file_path)

if __name__ == "__main__":
    directory_path = "/mnt/c/LogPatternFinder/CromaDB/OpenstackModel/test/out"
    process_directory(directory_path)
