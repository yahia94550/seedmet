#!/usr/bin/python
# -*- coding: utf-8 -*
from func_convert import *

#AnG = input("Entrez votre année de naissance : ")
#MoG = input("Entrez votre mois de naissance : ")
#JoG = input("Entrez votre jour de naissance : ")
#AnG = A =  1969
#MoG = M =  2
#JoG = J = 20
Entdtnaiss = raw_input("Entrez la date a convertir : (format : dd/mm/YYYY)\n")
liNaiss = Entdtnaiss.split("/")
AnG = A = int(liNaiss[2])
MoG = M = int(liNaiss[1])
JoG = J = int(liNaiss[0])
print "La date saisie est : %d/%d/%d " % (J, M, A)
NewH = []
NewH = convertdate(A, M, J)
Anh = NewH[0]
Moh = NewH[1]
Joh = NewH[2]
print "La date du : %d/%d/%d  , Correspond a : %d %s %d  " % (J, M, A, Joh,Moh , Anh)