#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:12:30 2017

@author: Maurice
"""
#helper class! -> encapsulates variables

class Student(object):
    def __init__(self,name,idIE,grades,email):
        self.name = name
        self.__idIE = idIE
        self.__grades = {}
        self.email = email
        
    def getname(self):
        return self.name
        
    def getgrade(self):
        return self.__grades
        
    def getemail(self):
        return self.email
        
    def getgrade(self,course):
        return self.__grades[course]

    def getid(self):
        return self.__idIE

    def setgrade(self,course,grade):
        self.__grades[course] = grade

    def setname(self,newname):
        self.name = newname
        
    
    
        
        
create student
get grades

        