#!/usr/bin/python
# -*- coding: utf-8 -*
from convertdate import french_republican
from convertdate import islamic

MoisHejFr = {1:"Mouharram",2:"Safar",3:"Rabi' Awwal",4:"Rabi' Thani",5:"Joumada Awwal",6:"Joumada Thani",7:"Rajab",8:"Cha'ban",9:"Ramadan",10:"Chawwal",11:"Dhoul Qa'da",12:"Dhoul Hijja"}
def convertdate(year, month, day):
    A = year
    M = month
    J = day
    dt = []
    dt = islamic.from_gregorian(A, M , J)
    #print islamic.from_gregorian(A, M , J)
    AnH = dt[0]
    Moh1 = dt[1]
    Moh = MoisHejFr.get(Moh1)
    Joh = dt[2]

    return AnH, Moh, Joh