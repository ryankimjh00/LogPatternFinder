import re
from helper_functions import suffix_array, lcp_array, extract_number_after_colon

def find_all_repeating_patterns(file_path, output_file):
    print("Finding repeating patterns...")
    with open(file_path, 'r') as file:
        text = file.readlines() 
        processed_text = []
        processed_text.extend(text)
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
            if count >= 1:
                out_file.write(f"Pattern: \n{pattern}\n")
                out_file.write(f"Repeats: {count}\n\n")
    print("Repeating patterns found")

                
file_path = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/1.cutted.txt"
output_file = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/4.patterns_copy.txt"
find_all_repeating_patterns(file_path, output_file)
