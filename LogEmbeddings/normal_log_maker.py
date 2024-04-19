import os

def filter_logs(input_dir, output_dir):
    # 출력 디렉토리 생성
    os.makedirs(output_dir, exist_ok=True)

    # 입력 디렉토리의 모든 .txt 파일에 대해 반복
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".txt"):
            with open(os.path.join(input_dir, file_name), 'r') as input_file:
                with open(os.path.join(output_dir, file_name), 'w') as output_file:
                    # INFO나 DEBUG를 포함하지 않은 라인만을 새로운 파일에 쓰기
                    for line in input_file:
                        if 'INFO' in line or 'DEBUG' in line:
                            output_file.write(line)
                        else:
                            pass
            print(f'✅ Complete {file_name}')
# mixed_docs 디렉토리의 파일을 필터링하여 normal_docs에 저장
filter_logs("/mnt/c/LogPatternFinder/LogEmbeddings/mixed_docs", "/mnt/c/LogPatternFinder/LogEmbeddings/normal_docs")
