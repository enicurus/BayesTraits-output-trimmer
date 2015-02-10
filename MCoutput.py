# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 15:12:53 2015

@author: ryanterrill
"""

# move BayesTraits output into data frame for R manipulation
file=raw_input("enter BayesTraits output file:  ")
openfile=open(file)
file_contents=openfile.read()
out=(file_contents[1858:-1])
outfilename=str(file)+"_MarkovChain.txt"
outfile=open(outfilename,"w")
outfile.write(str(out))
outfile.close




print "Solutions nearly always come from the direction you least expect, which means there’s no point trying to look in that direction because it won’t be coming from there"
