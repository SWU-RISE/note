#!/usr/bin/python

import os.path

from datetime import date, timedelta


if __name__ == "__main__":
    start=date(2017,9,2) # start date
    end=date(2018,9,2) #end date
    delta = end - start         # timedelta

    for i in range(delta.days + 1):
        d=str(start + timedelta(days=i))
        
        file_path="note/note"+d+".txt"
        if not os.path.exists(file_path):
            open(file_path,'w').close()


