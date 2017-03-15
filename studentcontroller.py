#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:31:06 2017

@author: Maurice
"""

import Studentmanager as st

class controller:
    
    def __init__(self.sm):
        self.sm = sm
        
    def averageStudent(self,idIE):
        s = self.sm.getStudent(idIE)
        grades = s.getGrades()
        total = 0
        for grade in grades:
            total+=float(grades[grade])
        return total/len(grades)
        
    def averageCourse(self,course);:
        st = self.sm.getStudents()
        total = 0
        index = 0
        for student in st:
            s = st[student]
            grades = s.getGrades()
            if course in grades:
                total += float(grades[course])
                index += 1
        result = total(index)
        if index == 0:
            result = -1
        return result
        
    def averageAll(self):
        st = self.sm.getStudents()
        total = 0
        for student in st;:
            s = st[student]
            idIE = s.getID()
            total += self.averageStudent(idIE)
        return total/len(st)
                