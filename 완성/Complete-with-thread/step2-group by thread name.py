import re

def group_patterns_by_word(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 정규식에 맞는 단어들을 추출하여 그룹화
    grouped_patterns = {}
    for line in lines:
        matches = re.findall(r'\b(\w+(?:-\w+)+)\b', line)
        for match in matches:
            if match in grouped_patterns:
                grouped_patterns[match].append(line.strip())
            else:
                grouped_patterns[match] = [line.strip()]

    return grouped_patterns

def write_grouped_patterns(grouped_patterns, output_file):
    with open(output_file, 'w') as file:
        for pattern, lines in grouped_patterns.items():
            file.write(f"Pattern: {pattern}\n")
            for line in lines:
                file.write(f"{line}\n")
            file.write("\n")

def main(input_file, output_file):
    grouped_patterns = group_patterns_by_word(input_file)
    write_grouped_patterns(grouped_patterns, output_file)

input_file = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/1.cutted.txt"
output_file = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/2.thread-grouping.txt"
main(input_file, output_file)
