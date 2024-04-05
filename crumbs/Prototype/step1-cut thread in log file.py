import re

def extract_and_group_patterns(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # 1단계: 정규식에 맞는 문자열 추출
    matched_strings = re.findall(r"\[.*?\] \[.*?\]  \[(\w*-+.*?)\]", text)

    # 2단계: 추출된 문자열들 중에서 \b\w+(?:-\w+)+\b 패턴에 맞는 문자열들을 그룹화
    grouped_patterns = {}
    for string in matched_strings:
        # 특정 패턴에 맞는 문자열 추출 및 그룹화
        if re.match(r".*:*", string):
            first_char = string.split()[0][0]
            if first_char in grouped_patterns:
                grouped_patterns[first_char].append(string)
            else:
                grouped_patterns[first_char] = [string]

    # 추가로 \b\w+(?:-\w+)+\b 패턴에 맞는 문자열들을 묶어줌
    additional_patterns = re.findall(r"\b\w+(?:-\w+)+\b", text)
    for pattern in additional_patterns:
        first_char = pattern[0]
        if first_char in grouped_patterns:
            grouped_patterns[first_char].append(pattern)
        else:
            grouped_patterns[first_char] = [pattern]

    return grouped_patterns

def main(file_path, output_file):
    grouped_patterns = extract_and_group_patterns(file_path)

    # 그룹화된 패턴 출력
    with open(output_file, 'w') as out_file:
        for first_char, patterns in grouped_patterns.items():
            out_file.write(f"Patterns starting with '{first_char}':\n")
            for pattern in patterns:
                out_file.write(f"{pattern}\n")
            out_file.write("\n")

file_path = "./proto/indigo.log"
output_file = "./conclusion/1.cutted.txt"
main(file_path, output_file)
