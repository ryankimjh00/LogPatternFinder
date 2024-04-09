import re
from helper_functions import suffix_array, lcp_array, extract_number_after_colon

def find_all_repeating_patterns(file_path, output_file):
    print("Finding repeating patterns...")
    with open(file_path, 'r') as file:
        text = file.readlines() 
        processed_text = []
        for line in text: 
            text_for_pattern = re.findall(r'\[(.*?)\ ]', line)  # 패턴을 찾기 위한 텍스트
            remain_text = re.split(r'\[(.*?)\ ]', line)  # 패턴과 매칭되지 않는 텍스트를 분리합니다.
            remain_text = [text for text in remain_text if text not in text_for_pattern and text != '']  # 패턴과 매칭되지 않은 텍스트만 선택합니다.
            processed_text.extend(text_for_pattern + remain_text)  # 패턴과 매칭되는 텍스트를 찾고 나머지 텍스트를 처리하여 리스트에 추가합니다.
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp >= 2 and lcp < 10:  # 빈 패턴이 아닌 경우
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

                
# file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/2.thread-grouping-cleaned.txt"
# output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
# find_all_repeating_patterns(file_path, output_file)
