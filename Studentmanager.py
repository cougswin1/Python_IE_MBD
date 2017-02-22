#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:23:42 2017

@author: Maurice
"""

import OOpStudentFile as st #student class file

class StudentManager:
    def __init__(self,filename):
        self.filename = filename
        self.students = {}

    def loadStudent(self,idIE,student):
        self.students[idIE]= student

    def makeStudent(self,infoStr):
        name,idIE,email = infoStr.split("*")
        return st.Student(name,idIE,email)
        
    def getStudent(self,idIE):
        return(self.students[idIE])
        
    def loadStudent(self):
        infile = open(self.filename,"r")
        for line in infile:
            tokens = line.split("*")
            if(len(tokens)>2):
                s = self.makeStudent(line)
                self.loadStudent(s.idIE,s)
            else:
                s.setGrade(tokens[0],tokens[1])
                
        infile.close()
        
    def getStudents(self):
        return self.students
    