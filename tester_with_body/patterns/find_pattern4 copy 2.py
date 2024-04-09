import math
import re
from helper_functions import suffix_array, lcp_array, extract_number_after_colon

def find_all_repeating_patterns(file_path, output_file):
    print("Finding repeating patterns...")
    with open(file_path, 'r') as file:
        text = file.readlines() 
        processed_text = []
        line_indices = []  # 각 텍스트의 원본 라인 인덱스를 저장하는 리스트
        line_counts = []  # 각 텍스트의 라인 수를 저장하는 리스트
        for line_index, line in enumerate(text): 
            text_for_pattern = re.findall(r'\[(.*?)\ ]', line)  # 패턴을 찾기 위한 텍스트
            remain_text = re.split(r'\[(.*?)\ ]', line)  # 패턴과 매칭되지 않는 텍스트를 분리합니다.
            remain_text = [text for text in remain_text if text != '']  # 패턴과 매칭되지 않은 텍스트만 선택합니다.
            
            # # remain_text 출력
            # if remain_text:
            #     print(f"remain_text: {', '.join([f'{text}({line_index+1})' for text in remain_text])}")
            
            # # text_for_pattern 출력
            # if text_for_pattern:
            #     print(f"text_for_pattern: {', '.join([f'{text}({line_index+1})' for text in text_for_pattern])}")
            
            # 나머지 로직은 동일하게 유지합니다.
            line_indices.extend([line_index] * len(text_for_pattern))  # 각 텍스트의 원본 라인 인덱스를 저장합니다.
            line_counts.extend([len(text_for_pattern)] * len(text_for_pattern))  # 각 텍스트의 라인 수를 저장합니다.
            if remain_text:  # 패턴이 아닌 텍스트가 있는 경우에만 추가합니다.
                processed_text.extend(remain_text)  # 매칭되지 않는 텍스트를 리스트에 추가합니다.
                line_indices.extend([-1] * len(remain_text))  # 매칭되지 않는 텍스트에는 -1을 저장합니다.
                line_counts.extend([1] * len(remain_text))  # 매칭되지 않는 텍스트에는 1을 저장합니다.
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp >= 7:  # 빈 패턴이 아닌 경우
                pattern = ''.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                start_line_index = line_indices[suffix_arr[i]]
                line_count = sum(line_counts[suffix_arr[i]: suffix_arr[i] + lcp])
                if start_line_index != -1:
                    if pattern in repeating_patterns:
                        repeating_patterns[pattern].append((start_line_index, line_count))
                    else:
                        repeating_patterns[pattern] = [(start_line_index, line_count)]

    sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: (extract_number_after_colon(x[0]), len(x[0]), x[1]))

    with open(output_file, 'w') as out_file:
        for pattern, indices in sorted_patterns:
            if len(indices) >= 2:
                out_file.write(f"Pattern: \n{pattern}\n")
                out_file.write("Start Line Indices: " + ", ".join([f"{index[0]+1}({math.ceil(index[1]/2)})" for index in sorted(indices, key=lambda x: x[0])]) + "\n")
                out_file.write(f"Repeats: {len(indices)}\n\n")
    print("Repeating patterns found")

                
file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/1.thread-grouping.txt"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
find_all_repeating_patterns(file_path, output_file)
