import re

def group_patterns_by_word(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    grouped_patterns = {}
    for line in lines:
        matches = re.findall(r'\b\w+(?:-\w+)+\b', line)
        
        for match in matches:
            if match in grouped_patterns:
                grouped_patterns[match].append(line.strip())
            else:
                grouped_patterns[match] = [line.strip()]

    return grouped_patterns

def write_grouped_patterns(grouped_patterns, output_file):
    with open(output_file, 'w') as file:
        for pattern, lines in sorted(grouped_patterns.items(), key=lambda x: int(re.search(r'\d+', x[1][0]).group())):
            for line in lines:
                file.write(f"{line}\n")
            file.write("\n")

def group(input_file, output_file):
    print("found file to group")
    grouped_patterns = group_patterns_by_word(input_file)
    write_grouped_patterns(grouped_patterns, output_file)
    print("grouping done")

input_file = "/mnt/c/LogPatternFinder/tester_with_body/proto/tester.log"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/1.thread-grouping.txt"
group(input_file, output_file)
