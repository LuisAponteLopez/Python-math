# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:22:12 2019

@author: Juan
"""



def decimal(passCourse):
    return passCourse/100

def sumNote(note,number,amountNote):
    while number<3:
        notes = int(input("Enter the note number "+str(number)+" "))
        note+=notes/100
        number+=1
    note = note/amountNote    
    return note
        
def missingNote(amountNote,youEvaluations):
    missing = amountNote - youEvaluations
    return missing

def percentExam(note,missing,decimalPassCourse,amountNote):
    need = round(((decimalPassCourse - note)*amountNote)/missing,2)
    if missing == 1:
        print("You need to take out "+ str(need*100) +"% in the next exam.")
    else:
        print("You need to take out "+ str(need*100) +"% in the next",missing,"exam.")
    
    
def main():
    
    
    amountNote = int(input("Enter the total note of course: "))
    
    passCourse = int(input("With how much class passes? "))
    decimalPassCourse = decimal(passCourse)
    
    youEvaluations = int(input("How many evaluations do you have? "))
    
    note = 0
    number = 1
    
    note = sumNote(note,number,amountNote)
    missing = missingNote(amountNote,youEvaluations)
    percentExam(note,missing,decimalPassCourse,amountNote)
    
main()