from state import State
import audio
import pygame as pg


class Fight:
    """Holds current gamemode and does the logic on the stances to find out what happens"""
    gamemode: int #TODO - use gamemode to control which danceBattle to use (can we compartmentalize gamemode things?)

    # Gamemode 1: Dance battle
    attacker = 0 #0 or 1 to log which player is currently attacking
    aggressive = True
    waiting = True
    DODGES_FOR_ATTACKS= {"nw": "se",
                          "n": "s",
                          "ne": "sw"}
    PARRIES_FOR_ATTACKS = {"nw": "e",
                           "n": "n",
                           "ne": "w"}
    @classmethod
    def metronome(cls):
        audio.

    @classmethod
    def danceBattle(cls, inputs: tuple[dict[str: list[str]], dict[str: list[str]]]):
        """Takes a list of stances and updates game state. Player history will be a list of attacks."""
        #TODO make this only work in gamemode 1, add comment describing the game mode (maybe a tutorial text file?)
        stances = (inputs[0]["perfect"] + inputs[0]["good"], inputs[1]["perfect"] + inputs[1]["good"]) # Consider only pressed inputs neglecting quality
        print("attacker: " + str(int(cls.attacker)))
        print(stances)
        attacks = [] # Create a list of current attacks
        parries = [] # Create a list of current parries
        dodges = [] # Create a list of current dodges

        for move in stances[cls.attacker]: # Add valid attacks chosen
            if move in cls.DODGES_FOR_ATTACKS.keys(): # It's a valid attack
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
            for attack in attacks: # Assume successful parry, check each attack, if ANY of them is unparried then set parried to false
                if not (cls.PARRIES_FOR_ATTACKS[attack] in parries):
                    parried = False

            if parried: # If attack was parried, lose advantage (also happens if no there was no attack)
                State.players[cls.attacker].history.insertAtFront([])
                if len(attacks) == 0:
                    audio.ticker.play(audio.fumble_sound)
                else:
                    audio.ticker.play(audio.parry_sound)
                cls.attacker = not cls.attacker
                cls.aggressive = True
                return
            else: # Otherwise, save last attack
                State.players[cls.attacker].history.insertAtFront(attacks) # Log attack that needs to be blocked
                audio.ticker.play(audio.attack_sound)

        else: # For defense beats
            print("defending beat. Dodges:",dodges)

            dodged = True
            if State.players[cls.attacker].history.getHead():
                for attack in State.players[cls.attacker].history.getHead().getData(): # Check if defender successfully dodged
                    print(attack)
                    if not (cls.DODGES_FOR_ATTACKS[attack] in dodges):
                        print("Player " + str(int(not cls.attacker)) + " got hit. Waiting for them to start.")
                        dodged = False
                        audio.ticker.play(audio.hit_sound)
                        cls.attacker = not cls.attacker
                        cls.aggressive = True
                        cls.waiting = True
                        return # If failed to dodge

        audio.ticker.play(audio.dodge_sound)
        cls.aggressive = not cls.aggressive # Switch aggressive/defensive beat
        return # Return False because no hit was recorded
