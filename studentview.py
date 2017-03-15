#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:40:50 2017

@author: Maurice
"""

import Studentcontroller as st

class view:
    
    def __init__(self,controller):
        self.controller = controller
        
    def mainloop(self):
        while choice != "0":
            print(
                  """
                  Welcome to student manager
                  
                  0-Quit
                  1-Average grade for one student
                  2-Average of the average grade of all students
                  3-Average grade for one course
                  """
                  )
            choice = input("Input command: ")
            print()
            
            if choice == "0":
                print("Bye bye!")
                break
            if choice == "1"
                s = input("Who's grades do you want to know?")
                print("Your Average Grade is")+st.averageStudent[s]
            
            