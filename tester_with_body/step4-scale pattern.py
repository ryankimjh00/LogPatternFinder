import re

# 입력 파일 경로
input_file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
# 출력 파일 경로
output_file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/4.conclusion.txt"

# 정규 표현식
pattern = r":\d+ "

# 입력 파일 열기
with open(input_file_path, 'r') as input_file:
    # 입력 파일 내용 읽기
    lines = input_file.readlines()

    # 필터링된 줄을 담을 리스트 초기화
    filtered_lines = []

    # 각 줄에 대해 패턴 확인
    for line in lines:
        # "-"가 포함되어 있고 ":"가 있는 경우 또는 "Pattern: "이 있는 경우
        if ("-" in line and ":" in line) or "Pattern: " in line or "Repeats: " in line:
            # 패턴이 "Pattern: "인 경우 줄바꿈 추가
            if "Pattern: " in line:
                line = line.replace("Pattern: ", "------------------------------------------------------------------------------------------\nPattern:")
            filtered_lines.append(line)

    # 필터링된 줄을 하나의 문자열로 결합
    content = ''.join(filtered_lines)

    # 정규 표현식에 매칭되는 패턴을 찾아서 줄바꿈 추가
    new_content = re.sub(pattern, lambda match: match.group(0) , content)

# 출력 파일에 쓰기
with open(output_file_path, 'w') as output_file:
    output_file.write(new_content)
