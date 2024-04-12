import re

def main():
    line="[dataListenerContainer-route-1 com.indigo.esb.MessageRoute:211 ] - [SQU-OTO] IF ID :IF_KAI_MPSS_001, Queue Name :KAI.MQ.DB.RCV, Reply_Queue Name :KAI.MQ.DB.SND.RPL, Dest ID :IF_DEST_MPSS_001"
    text_for_pattern = re.findall(r'\[(.*?)\ ]', line)
    remain_text = re.findall(r'\ -\s*(.*?)$', line)
    print(text_for_pattern)
    print(remain_text)

main()
