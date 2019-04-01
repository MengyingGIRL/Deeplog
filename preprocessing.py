import os
import os.path
import gzip
import csv
from dateutil.parser import parse
import pandas as pd

strZipFile = '/Users/wangmengying/Downloads/bgl2.gz'
strDstFile = 'bgl2.csv'


def gzfile2csv(inputfile,outputfile):
    file = gzip.GzipFile(inputfile,"r")
    with open(outputfile,"w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["date","time","contents"])
        levels = []
        i = 0
        for line in file:
            # if i == 0:
            #     time0 = line.split(" ")[4]
            #     time0 = time0.replace(".",":")
            #     time0 = " ".join(time0.split(":")[:-1])
            #     print (time0)
            #     a = parse(time0)
            date = line.split(" ")[2]
            date = date.replace(".","-")
            time1 = line.split(" ")[4]
            time1 = time1.replace(".",":")
            # time = (parse(time1) - a).total_seconds()
            level = line.split(" ")[8]
            if level not in levels:
                levels.append(level)
            content = line.split(" ")[7:]
            content = " ".join(content)
            writer.writerow([time1,content])
            i += 1

def gzfile2pandas(inputfile,outputfile):
    file = gzip.GzipFile(inputfile, "r")
    data = pd.read_table(file,header=None,index_col=0)
    data.head(10)

gzfile2pandas(strZipFile,strDstFile)



