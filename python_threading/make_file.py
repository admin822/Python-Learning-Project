import os
import pandas as pd
import csv
import random

text_handler=open('ping.txt','w')
another_text_handler=open("secondping.txt",'w')
another_text_handler.write("this is the second ping")
text_handler.write("this is a ping")
csv_handler=open('ping.csv','w')
fieldnames=['p','i','n','g']
ping_dict={k:random.randint(1,10) for k in fieldnames}
csv_writer=csv.DictWriter(csv_handler,fieldnames)
csv_writer.writeheader()
csv_writer.writerow(ping_dict)