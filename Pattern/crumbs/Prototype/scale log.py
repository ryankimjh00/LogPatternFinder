def remove_non_starting_with_bracket(text):
    # 줄바꿈으로 문장을 구분하고, [로 시작하지 않는 문장을 필터링합니다.
    filtered_text = [sentence for sentence in text.split('\n') if sentence.startswith('[')]
    # 필터링된 문장들을 다시 줄바꿈으로 이어붙여 반환합니다.
    return '\n'.join(filtered_text)

def main(file_path, output_file):
    with open(file_path, 'r') as file:
        text = file.read().strip()
    
    # [로 시작하지 않는 문장을 제거합니다.
    filtered_text = remove_non_starting_with_bracket(text)
    
    # 결과를 파일에 씁니다.
    with open(output_file, 'w') as out_file:
        out_file.write(filtered_text)

file_path = "/mnt/c/LogPatternFinder/extract2.txt"
output_file = "filtered_text.txt"
main(file_path, output_file)
