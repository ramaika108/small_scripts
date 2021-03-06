#!/usr/bin/python3
import os, sys, time

"""
    -f    Find all open ".pdf" and ".djvu" files and save list to file
    -r    Reopen all ".pdf" and ".djvu" files that were saved in zathura
          and Atril document viewer
"""

def determine_reader(line:str):
    if line.lower()[-5:-1] == ".pdf":
        return "zathura"

def find_files():   #find all pdf files open (probably zathura instances)
    open_windows = os.popen("wmctrl -l").read()
    open_windows = open_windows.splitlines()
    pdf_list = []

    for i in open_windows:
        if i.lower().endswith(".pdf"):  #find docs files
            pdf_list.append(i[12]+i[27:] + "\n")  #gets pat to docs

    with open ("open_docs.txt", "w") as file:   #save found docs to file
        for i in pdf_list:
            file.write(i)
        file.close()

def reopen_files(): #opens files that were saved to "open_docs.txt"
    with open ("open_docs.txt", "r") as file:
        for i in file:
            os.popen("wmctrl -s %s" % i[0]) #move to needed workspace
            reader = determine_reader(i)
            os.popen("%s \"%s\"" % (reader, i[1:-1]))
            time.sleep(1)

if len(sys.argv) == 1:
    exit()
elif sys.argv[1] == "-f":
    find_files()
elif sys.argv[1] == "-r":
    reopen_files()

#requires wmctrl and zathura
