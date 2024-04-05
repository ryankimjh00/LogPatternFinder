import re

# 파일 경로
file_path = "/mnt/c/Log Pattern/extracted_data.txt"

# 정규 표현식 패턴
pattern = r" .*:*"

# 패턴과 개수를 저장할 딕셔너리
pattern_count = {}

# 파일 열기
with open(file_path, 'r') as file:
    # 파일의 각 줄에 대해 작업 수행
    for line in file:
        # 패턴 추출
        match = re.search(pattern, line)
        if match:
            current_pattern = match.group(0)
            # 딕셔너리에 패턴 카운트 추가
            if current_pattern not in pattern_count:
                pattern_count[current_pattern] = 1
            else:
                pattern_count[current_pattern] += 1

# 추출된 패턴과 그에 대한 카운트 출력
for pattern, count in pattern_count.items():
    print(f"{pattern}: {count}")