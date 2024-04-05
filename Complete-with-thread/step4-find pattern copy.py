import re

def suffix_array(words):
    n = len(words)
    suffixes = [(words[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def lcp_array(words, suffix_array):
    n = len(words)
    lcp = [0] * n
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and words[i + k] == words[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

def find_all_repeating_patterns(file_path, output_file):
    with open(file_path, 'r') as file:
        text = file.readlines()
        processed_text = []
        for line in text:
            if re.findall(r'\d+:', line):
                processed_text.append(line + '\n')
            else:
                processed_text.append(line)

        suffix_arr = suffix_array(processed_text)
        lcp_arr = lcp_array(processed_text, suffix_arr)
        repeating_patterns = {}
        for i, lcp in enumerate(lcp_arr):
            if lcp >= 10 and lcp < 20:
                pattern = ''.join(processed_text[suffix_arr[i]: suffix_arr[i] + lcp])
                if pattern in repeating_patterns:
                    repeating_patterns[pattern] += 1
                else:
                    repeating_patterns[pattern] = 1

    # 결과를 output_file에 출력
    with open(output_file, 'w') as out_file:
        for pattern, count in repeating_patterns.items():
            out_file.write(f"Pattern:\n\n{pattern}")
            out_file.write(f"\nRepeats: {count}\n\n")

file_path = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/3.thread-scaled.txt"
output_file = "/mnt/c/LogPatternFinder/Complete-with-thread/conclusion/4.patterns_copy.txt"
find_all_repeating_patterns(file_path, output_file)
