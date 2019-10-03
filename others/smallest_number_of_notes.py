#!/usr/bin/env python3
available_notes = [100, 50, 10, 5, 2, 1]
notes = list()
no_of_each_note = list()
for i in range(int(input())) :
    amount = int(input())
    #print("amount: ", amount)
    small = 0
    for note in available_notes :
        small = amount // note
        #print("No of", note, "notes:", small)
        amount -= small * note
        #print("amount:",amount)
        no_of_each_note.append(small)
        if amount == 0 :
            break
    notes.append(sum(no_of_each_note))
    no_of_each_note = list()
for note in notes :
    print(note)
