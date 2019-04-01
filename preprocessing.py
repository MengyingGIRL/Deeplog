import os
import os.path
import gzip
import csv
from dateutil.parser import parse
import pandas as pd
import re

strZipFile = '/Users/wangmengying/Downloads/bgl2.gz'
strDstFile = 'bgl2.dat'

def gzfile2txt(inputfile):
    file = gzip.GzipFile(inputfile,'r')
    with open('bgl2.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time','log'])
        for line in file:
            print(line)
            line = line.strip()
            line = str(line)
            date = line.split(" ")[4]
            time = " ".join(date.split(".")[:2])
            time = time.replace(".", ":")
            log = " ".join(line.split(" ")[7:])
            log = re.sub('[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', " ", log)
            writer.writerow([time, log])

#quchong
def filter1(inputfile):
    df = pd.read_csv(inputfile, header=0, sep=',')
    datalist = df.drop_duplicates()
    datalist.to_csv('bgl.csv', sep='\t', header=True, index=False)

def anamolyfile(inputfile):
    file = open(inputfile, 'r')
    i = 0
    label = "normal"
    with open('file.csv', 'w') as f1:#, open('errorfile.dat','w') as f2:
        for line in file:
            if i == 0:
                i += 1
                continue
            line = line.replace("\n","\t")
            # mins = line.split(' ')[1]
            # mins = mins.split('\t')[0]
            # log = line.split('\t',1)[1]
            # # line_seen.append(log)
            if ("WARNING" or "ERROR" or "FAILURE") in line.split():
                label = "ananomly"
                f1.write(line + label + "\n")
            elif "FATAL" in line.split():
                label = "error"
                f1.write(line + label + "\n")
            else:
                f1.write(line + label + "\n")
            # if ("WARNING" or "ERROR" or "FAILURE" )in line.split():
            #     f2.write(line)

# gzfile2txt(strZipFile)
# filter1('bgl2.csv')
anamolyfile('bgl.csv')









