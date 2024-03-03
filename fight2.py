from state import State
import audio
import pygame as pg

class fight2:
    #To be moved to fight.py file
    #Gamemode 2: combo fight (placeholder)
    combo = 0 #aka health. Positive for p1 negative for p2
    SEQUENCES = {["ne", "nw", "ne", "nw", "n"]: "Guardbreak",[]:"",[]:""}

    def comboFight(cls, inputs: tuple[dict[str: list[str]], dict[str: list[str]]]):
        stances = (inputs[0]["perfect"] + inputs[0]["good"], inputs[1]["perfect"] + inputs[1]["good"])

        p1_attack = ""
        p2_attack = ""
        
        #Add player's current stance to front of history list
        State.player0.history.insertAtFront(stances[0])
        State.player1.history.insertAtFront(stances[1])

        #Get latest item in player's history
        p1_iterator = State.player0.history.getHead()
        p2_iterator = State.player1.history.getHead()

        #Build the current sequence the player is doing
        p1_sequence = []
        p2_sequence = []
        
        while True:
            p1_sequence.insert(0, p1_iterator.getData())
            p2_sequence.insert(0, p2_iterator.getData())

            if p1_sequence in cls.SEQUENCES:
                while p1_sequence in cls.SEQUENCES:
                    p1_attack == cls.SEQUENCES.get(p1_sequence)
                    p1_sequence.insert(0, p1_iterator.getData())
                    p1_iterator = p1_iterator.getNext()

            if p2_sequence in cls.SEQUENCES:
                while p2_sequence in cls.SEQUENCES:
                    p2_attack == cls.SEQUENCES.get(p2_sequence)
                    p2_sequence.insert(0, p2_iterator.getData())
                    p2_iterator = p2_iterator.getNext()
            
            p1_iterator = p1_iterator.getNext()
            p2_iterator = p2_iterator.getNext()

            if p1_iterator == None or p2_iterator == None or p1_attack != "" or p2_attack != "":
                break

        #match p1_attack:
            #case "Guardbreak":
                #do something to p2
                #break

        #match p2_attack:
            #case "Guardbreak":
                #do something to p1
                #break
        




