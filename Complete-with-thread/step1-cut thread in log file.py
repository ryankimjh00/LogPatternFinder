import re

def extract_and_group_patterns(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # 1단계: 첫 번째 정규식에 맞는 문자열 추출
    matched_strings = re.findall(r"\[(\w*-+.*?) \]", text)

    # 2단계: 추출된 문자열들 중에서 두 번째 정규식에 맞는 문자열들을 그룹화
    grouped_patterns = {}
    for string in matched_strings:
        # 두 번째 정규식에 맞는 문자열을 그룹화
        matches = re.findall(r'\b\w+(?:-\d+)', string)
        for match in matches:
            if match in grouped_patterns:
                grouped_patterns[match].append(string.strip())
            else:
                grouped_patterns[match] = [string.strip()]

    return grouped_patterns

def main(file_path, output_file):
    grouped_patterns = extract_and_group_patterns(file_path)

    # 그룹화된 패턴을 파일에 출력
    with open(output_file, 'w') as out_file:
        for _, strings in grouped_patterns.items():
            for string in strings:
                out_file.write(f"{string}\n")
            out_file.write("\n")

file_path = "/mnt/c/LogPatternFinder/Complete-with-thread/proto/tester.log"
output_file = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/1.cutted.txt"
main(file_path, output_file)
