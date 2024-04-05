import re

# 정규 표현식 패턴
pattern = r"\[.*?\] \[.*?\]  \[(\w*-+.*?)\]"

def suffix_array(string):
    # 모든 접미사를 생성하고 시작 인덱스와 함께 저장
    suffixes = [(string[i:], i) for i in range(len(string))]
    # 접미사를 사전순으로 정렬
    suffixes.sort()
    # 정렬된 접미사들의 시작 인덱스를 반환
    return [suffix[1] for suffix in suffixes]

def lcp_array(string, suffix_array):
    n = len(string)
    lcp = [0] * n  # 최장 공통 접두사 배열 초기화
    rank = [0] * n  # 접미사 배열의 인덱스에 대응하는 랭크 배열 초기화
    
    # 각 접미사의 랭크를 설정
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    
    k = 0  # 공통 접두사 길이를 저장하는 변수 초기화
    for i in range(n):
        # 접미사 배열의 마지막 인덱스일 경우 k를 0으로 초기화하고 다음으로 넘어감
        if rank[i] == n - 1:
            k = 0
            continue
        # 다음 접미사와의 공통 접두사의 길이를 계산
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and string[i + k] == string[j + k]:
            k += 1
        # 공통 접두사의 길이를 저장
        lcp[rank[i]] = k
        # k가 0보다 크면 1 감소시켜 준다
        if k > 0:
            k -= 1
    # 최장 공통 접두사 배열 반환
    return lcp

def find_longest_repeating_pattern(string):
    # 문자열의 접미사 배열 생성
    suffix_arr = suffix_array(string)
    # LCP 배열 생성
    lcp_arr = lcp_array(string, suffix_arr)
    # LCP 배열에서 가장 큰 값(가장 긴 반복 패턴의 길이)을 찾음
    max_length = max(lcp_arr)
    
    # 만약 최장 공통 접두사의 길이가 0이라면 빈 문자열 반환
    if max_length == 0:
        return ""
    else:
        # 최장 공통 접두사의 길이를 갖는 반복 패턴을 반환
        idx = lcp_arr.index(max_length)
        return string[suffix_arr[idx]: suffix_arr[idx] + max_length]

def process_file(input_file_path):
    # 추출된 데이터를 저장할 리스트
    extracted_data = []
    # 파일 열기
    with open(input_file_path, 'r') as input_file:
        # 파일의 각 줄에 대해 작업 수행
        for line in input_file:
            # 패턴 매칭
            match = re.search(pattern, line)
            # 매칭된 결과 추가
            if match:
                result = match.group(1)
                # 숫자로 끝나지 않으면 결과에 추가
                if not result[-1].isdigit():
                    extracted_data.append(result + " \n")
    # 추출된 데이터를 문자열로 결합
    text = " ".join(extracted_data)
    # 최장 반복 패턴 찾기
    longest_pattern = find_longest_repeating_pattern(text)

    return longest_pattern

input_file_path = "/mnt/c/LogPatternFinder/완성/test.log"
# 추출된 데이터로부터 최장 반복 패턴 찾기
longest_pattern = process_file(input_file_path)
print("========================== 패턴 분석 결과 ==========================")
print(longest_pattern)
print("==================================================================")

