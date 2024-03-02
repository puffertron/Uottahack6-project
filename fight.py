from state import State
import audio
import pygame as pg


class Fight:
    """Holds current gamemode and does the logic on the stances to find out what happens"""
    gamemode: int

    # Gamemode 1: Dance battle
    attacker = 0
    aggressive = True
    waiting = True
    DODGES_FOR_ATTACKS= {"nw": "sw",
                          "n": "s",
                          "ne": "se"}
    PARRIES_FOR_ATTACKS = {"nw": "w",
                           "n": "n",
                           "ne": "e"}
    @classmethod
    def danceBattle(cls, inputs: tuple[dict[str: list[str]], dict[str: list[str]]]):
        """Takes a list of stances and updates game state. Player history will be a list of attacks."""
        stances = (inputs[0]["perfect"] + inputs[0]["good"], inputs[1]["perfect"] + inputs[1]["good"]) # Consider only pressed inputs neglecting quality
        print(stances)
        attacks = [] # Create a list of current attacks
        parries = [] # Create a list of current parries
        dodges = [] # Create a list of current dodges

        for move in stances[cls.attacker]: # Add valid attacks chosen
            if move in cls.DODGES_FOR_ATTACKS.keys():
                attacks.append(move)
        for move in stances[not cls.attacker]:
            if move in cls.PARRIES_FOR_ATTACKS.values():
                parries.append(move)
        for move in stances[not cls.attacker]: # Add valid dodges chosen
            if move in cls.DODGES_FOR_ATTACKS.values():
                dodges.append(move)

        if cls.waiting:
            if len(attacks) == 0:
                return
            else:
                cls.waiting = False
                #TODO - can add music change here

        if cls.aggressive: # For aggressive beats
            print("attacking beat. Attacks:",attacks,"Parries:",parries)

            parried = True
            for attack in attacks: # Check if defender successfully parried
                if not (cls.PARRIES_FOR_ATTACKS[attack] in parries):
                    parried = False

            if parried: # If attack was parried, lose advantage
                State.players[cls.attacker].history.insertAtFront([])
                cls.attacker = not cls.attacker
                if not len(attacks) == 0:
                    audio.ticker.play(audio.parry_sound)
            else: #otherwise, save last attack
                State.players[cls.attacker].history.insertAtFront(attacks)
                audio.ticker.play(audio.aggressive_sound)

        else: # For defense beats
            print("defending beat. Dodges:",dodges)

            dodged = True
            if State.players[cls.attacker].history.getHead():
                for attack in State.players[cls.attacker].history.getHead().getData(): # Check if defender successfully dodged
                    print(attack)
                    if not (cls.DODGES_FOR_ATTACKS[attack] in dodges):
                        dodged = False
                        audio.ticker.play(audio.hit_sound)
                        cls.attacker = not cls.attacker
                        cls.waiting = True
                        return # If failed to dodge

        audio.ticker.play(audio.defensive_sound)
        cls.aggressive = not cls.aggressive # Switch aggressive/defensive beat
        return False # Return False because no hit should be recorded
