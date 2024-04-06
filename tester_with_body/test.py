import re

def main(line):
    text_for_pattern = re.findall(r'\[(.*?)\ ]', line)
    remain_text = re.split(r'\[(.*?)\ ]', line)
    remain_text = [text for text in remain_text if text not in text_for_pattern and text != '']
    print(text_for_pattern, remain_text)

main("[dataListenerContainer-return-7 com.indigo.esb.ReturnMessage:57 ] - =========================RQU-OTO Bean SU Start=========================")
