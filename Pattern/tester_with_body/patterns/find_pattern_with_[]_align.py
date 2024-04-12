from helper_functions import suffix_array, lcp_array, extract_number_after_colon

def find_all_repeating_patterns(file_path, output_file):
    print("Finding repeating patterns...")
    with open(file_path, 'r') as file:
        text = file.readlines() 
        processed_text = []
        for line in text:
            pattern = ""  # 패턴을 저장할 변수
            remain_text = ""  # 패턴과 매칭되지 않은 텍스트를 저장할 변수
            for char in line:
                if char == '[':
                    pattern += char  # 패턴의 시작 문자 '['를 추가
                elif char == ' ]':
                    pattern += char  # 패턴의 종료 문자 ']'를 추가
                    processed_text.append(pattern)  # 완성된 패턴을 리스트에 추가
                    pattern = ""  # 패턴 초기화
                else:
                    pattern += char  # 일반 텍스트는 패턴에 추가
                    remain_text += char  # 패턴과 매칭되지 않은 텍스트에 추가
            if pattern:  # 마지막 라인에 패턴이 끝나지 않은 경우
                processed_text.append(pattern)  # 남은 패턴을 리스트에 추가
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp >= 2 and lcp <= 20:  # 빈 패턴이 아닌 경우
                pattern = ''.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                if pattern in repeating_patterns:
                    repeating_patterns[pattern] += 1
                else:
                    repeating_patterns[pattern] = 1

    sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: (extract_number_after_colon(x[0]), len(x[0]), x[0]))

    with open(output_file, 'w') as out_file:
        for pattern, count in sorted_patterns:
            if count >= 2:
                out_file.write(f"Pattern: \n{pattern}\n")
                out_file.write(f"Repeats: {count}\n\n")
    print("Repeating patterns found")

file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/1.thread-grouping.txt"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
find_all_repeating_patterns(file_path, output_file)
