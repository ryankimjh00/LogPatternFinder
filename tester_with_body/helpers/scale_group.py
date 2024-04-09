import re

def scale_group(input_file_path, output_file_path):
    print("found file to scale")
    # 입력 파일 경로
    input_file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/1.thread-grouping.txt"
    # 출력 파일 경로
    output_file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/2.thread-grouping-cleaned.txt"

    # 첫 번째 정규식 패턴
    pattern1 = r'\[\d{2}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}\] \[[A-Z]+ \] '

    # 두 번째 정규식 패턴
    pattern2 = r'\[\d{2}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}\] \[[A-Z]+\] '

    # 입력 파일 열기
    with open(input_file_path, 'r') as input_file:
        # 입력 파일 내용 읽기
        content = input_file.read()

        # 첫 번째 정규식에 매칭되는 부분 제거
        cleaned_content = re.sub(pattern1, '', content)
        # 두 번째 정규식에 매칭되는 부분 제거
        cleaned_content = re.sub(pattern2, '', cleaned_content)

    # 출력 파일에 쓰기
    with open(output_file_path, 'w') as output_file:
        output_file.write(cleaned_content)
    print("scaling done")