import re
from helper_functions import suffix_array, lcp_array

def find_all_repeating_patterns(file_path, output_file):
    with open(file_path, 'r') as file:
        text = file.readlines() 
        repeating_patterns = {} 
        pattern_indices = []  # 각 패턴이 나타나는 줄의 인덱스를 저장할 리스트
        for i, line in enumerate(text): 
            text_for_pattern = re.findall(r'\[(.*?)\ ]', line)
            remain_text = re.split(r'\[(.*?)\ ]', line)
            remain_text = [text.strip() for text in remain_text if text.strip() != '']
            if text_for_pattern:
                for pattern_text in text_for_pattern:
                    if pattern_text in repeating_patterns:
                        repeating_patterns[pattern_text] += remain_text
                    else:
                        repeating_patterns[pattern_text] = remain_text
                        pattern_indices.append(i)  # 해당 패턴이 나타나는 줄의 인덱스 저장

        processed_text = [text for sublist in repeating_patterns.values() for text in sublist]
        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        
        for pattern, remain_text in repeating_patterns.items():
            pattern_len = len(pattern)
            for i, lcp in enumerate(lcp_arr):
                if lcp == pattern_len:
                    current_pattern = '\n'.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                    if current_pattern == pattern:
                        repeating_patterns[pattern] = remain_text
                        break
        
    sorted_patterns = sorted(repeating_patterns.items(), key=lambda x: (len(x[0]), x[0]))
    print(sorted_patterns)

    # with open(output_file, 'w') as out_file:
    #     for pattern, remain_text in sorted_patterns:
    #         pattern_count = remain_text.count(pattern)
    #         if pattern_count >= 2:
    #             out_file.write(f"Pattern: {pattern}\n")
    #             out_file.write("Repeats:\n")
    #             for idx, line_idx in enumerate(pattern_indices):
    #                 if pattern in text[line_idx]:
    #                     out_file.write(f"{text[line_idx]}")  # 패턴이 나타나는 줄 출력
    #                     # out_file.write(f"{remain_text[idx]}\n")  # 해당 패턴에 대응되는 텍스트 출력
    #             out_file.write("\n")

file_path = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/2.thread-grouping-cleaned.txt"
output_file = "/mnt/c/LogPatternFinder/tester_with_body/conclusion/3.patterns.txt"
find_all_repeating_patterns(file_path, output_file)
