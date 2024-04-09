import re

def filter_lines(input_file, output_file, pattern):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    filtered_lines = [line.strip() for line in lines if re.search(pattern, line)]
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(filtered_lines))

input_file_path = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/2.thread-grouping.txt"
output_file_path = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/3.thread-scaled.txt"
pattern_to_keep = r'.*:.+'

filter_lines(input_file_path, output_file_path, pattern_to_keep)
