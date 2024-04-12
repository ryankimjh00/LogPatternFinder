import re

input_file_path = "/mnt/c/LogPatternFinder/CromaDB/exception.log"
output_file_path = "/mnt/c/LogPatternFinder/CromaDB/output.log"

with open(input_file_path, "r") as input_file:
    with open(output_file_path, "w") as output_file:
        for line in input_file:
            # 정규 표현식을 사용하여 숫자를 제거
            modified_line = re.sub(r'\d+', '', line)
            output_file.write(modified_line)
