import re

# 파일 경로
input_file_path = "/mnt/c/LogPatternFinder/Road-info.log"
output_file_path = "/mnt/c/LogPatternFinder/extracted_data11.txt"

# 정규 표현식 패턴
pattern = r"\[.*?\] \[.*?\] \[(\w*-+.*?)\]"

# 결과를 저장할 리스트
extracted_data = []

# 파일 열기
with open(input_file_path, 'r') as input_file:
    # 파일의 각 줄에 대해 작업 수행
    for line in input_file:
        # 패턴 매칭
        match = re.search(pattern, line)
        
        # 매칭된 결과 추가
        if match:
            result = match.group(1)
            extracted_data.append(result)

# 결과를 파일에 저장
with open(output_file_path, 'w') as output_file:
    for data in extracted_data:
        output_file.write(data + '\n')

print("추출된 데이터가", output_file_path, "에 저장되었습니다.")
