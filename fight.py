from state import State
import audio
import pygame as pg


class Fight:
    """Holds current gamemode and does the logic on the stances to find out what happens"""
    gamemode: int

    # Gamemode 1: Dance battle
    attacker = 0
    aggressive = True
    DODGES_FOR_ATTACKS= {"NW": "SW",
                          "N": "S",
                          "NE": "SE"}
    PARRIES_FOR_ATTACKS = {"NW": "W",
                           "N": "N",
                           "NE": "E"}
    @classmethod
    def danceBattle(cls, inputs: tuple[dict[str: list[str]], dict[str: list[str]]]) -> bool:
        """Takes a list of stances and updates game state. Player history will be a list of attacks."""
        stances = (inputs[0]["perfect"] + inputs[0]["good"], inputs[1]["perfect"] + inputs[1]["good"]) # Consider only pressed inputs neglecting quality

        if cls.aggressive: # For aggressive beats
            attacks = [] # Create a list of current attacks
            parries = [] # Create a list of current parries

            for move in stances[cls.attacker]: # Add valid attacks chosen
                if move in cls.DODGES_FOR_ATTACKS.keys():
                    attacks.append(move)
            for move in stances[not cls.attacker]:
                if move in cls.PARRIES_FOR_ATTACKS.values():
                    parries.append(move)
            
            parried = True
            for attack in attacks: # Check if defender successfully parried
                if not (parries in cls.PARRIES_FOR_ATTACKS[attack]):
                    parried = False

            if parried: # If attack was parried, lose advantage
                State.players[cls.attacker].history.insertAtFront([])
                cls.attacker = not cls.attacker
                if not len(attacks) == 0:
                    audio.parry.play()
            else: #otherwise, save last attack
                State.players[cls.attacker].history.insertAtFront(attacks)
                audio.aggressive_sound.play()

        else: # For defense beats
            dodges = [] # Create a list of current dodges

            for move in stances[not cls.attacker]: # Add valid dodges chosen
                if move in cls.DODGES_FOR_ATTACKS.values():
                    dodges.append(move)
            
            dodged = True
            if State.players[cls.attacker].history.getHead():
                for attack in State.players[cls.attacker].history.getHead().getData(): # Check if defender successfully dodged
                    if not (dodges in cls.DODGES_FOR_ATTACKS[attack]):
                        dodged = False
                        audio.hit.play()
                        return not dodged # If failed to dodge, return True to record a hit
        
        audio.defensive_sound.play()
        cls.aggressive = not cls.aggressive # Switch aggressive/defensive beat
        return False # Return False because no hit should be recorded
