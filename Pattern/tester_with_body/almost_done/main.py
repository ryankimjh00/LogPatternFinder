from step1_group_by_thread_name_with_no_mix import group
from step2_scale_group import scale_group
from step3_find_pattern2 import find_all_repeating_patterns
from step4_scale_pattern import scale_patterns


def main(input_file, output_file):
    # 1. 그룹핑
    input_file = "/mnt/c/LogPatternFinder/tester_with_body/proto/tester.log"
    group_output = "/mnt/c/LogPatternFinder/tester_with_body/almost_done/result/1.thread-grouping.txt"
    group(input_file, group_output)

    # 2. 스케일링
    scale_output = "/mnt/c/LogPatternFinder/tester_with_body/almost_done/result/2.thread-grouping-cleaned.txt"
    scale_group(group_output, scale_output)

    # 3. 패턴 찾기
    pattern_output = "/mnt/c/LogPatternFinder/tester_with_body/almost_done/result/3.patterns.txt"
    find_all_repeating_patterns(scale_output, pattern_output)

    # 4. 패턴 스케일링
    output_file = "/mnt/c/LogPatternFinder/tester_with_body/almost_done/result/4.conclusion.txt"
    scale_patterns(pattern_output, output_file)