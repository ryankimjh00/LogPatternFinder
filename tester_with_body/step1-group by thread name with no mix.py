import re

def group_patterns_by_word(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 정규식에 맞는 단어들을 추출하여 그룹화
    grouped_patterns = {}
    for line in lines:
        # "SQU-OTO"와 "RQU-OTO"를 제외한 모든 하이픈(-)으로 연결된 단어 찾기
        matches = re.findall(r'\b\w+(?:-\w+)+\b', line)
        
        # 각 패턴을 그룹화
        for match in matches:
            if match in grouped_patterns:
                grouped_patterns[match].append(line.strip())
            else:
                grouped_patterns[match] = [line.strip()]

    return grouped_patterns

def write_grouped_patterns(grouped_patterns, output_file):
    with open(output_file, 'w') as file:
        # 발견된 순서대로 정렬하여 파일에 쓰기
        for pattern, lines in sorted(grouped_patterns.items(), key=lambda x: int(re.search(r'\d+', x[1][0]).group())):
            for line in lines:
                file.write(f"{line}\n")
            file.write("\n")

def main(input_file, output_file):
    grouped_patterns = group_patterns_by_word(input_file)
    write_grouped_patterns(grouped_patterns, output_file)

input_file = "/mnt/c/LogPatternFinder/tester_with_body/proto/tester.log"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/1.thread-grouping.txt"
main(input_file, output_file)
