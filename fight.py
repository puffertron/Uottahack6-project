from state import State
import audio
import pygame as pg


class Fight:
    """Holds current gamemode and does the logic on the stances to find out what happens"""
    gamemode: int #TODO - use gamemode to control which danceBattle to use (can we compartmentalize gamemode things?)

    # Gamemode 1: Dance battle
    attacker = 0 #0 or 1 to log which player is currently attacking
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
        #TODO make this only work in gamemode 1, add comment describing the game mode (maybe a tutorial text file?)
        stances = (inputs[0]["perfect"] + inputs[0]["good"], inputs[1]["perfect"] + inputs[1]["good"]) # Consider only pressed inputs neglecting quality

        if cls.aggressive: # For aggressive beats
            attacks = [] # Create a list of current attacks
            parries = [] # Create a list of current parries

            for move in stances[cls.attacker]: # Add valid attacker attacks chosen
                if move in cls.DODGES_FOR_ATTACKS.keys(): # It's a valid attack
                    attacks.append(move)
            for move in stances[not cls.attacker]: # Add valid defender parries chosen
                if move in cls.PARRIES_FOR_ATTACKS.values():
                    parries.append(move)
            
            parried = True # Check if defender successfully parried
            for attack in attacks: # Assume successful parry, check each attack, if ANY of them is unparried then set parried to false
                if not (parries in cls.PARRIES_FOR_ATTACKS[attack]):
                    parried = False

            if parried: # If attack was parried, lose advantage (also happens if no there was no attack)
                State.players[cls.attacker].history.insertAtFront([])
                cls.attacker = not cls.attacker
                if len(attacks) != 0:
                    audio.parry.play()
            else: # Otherwise, save last attack
                State.players[cls.attacker].history.insertAtFront(attacks) # Log attack that needs to be blocked
                audio.aggressive_sound.play()

        else: # For defense beats
            dodges = [] # Create a list of current dodges

            for move in stances[not cls.attacker]: # Add valid dodges chosen
                if move in cls.DODGES_FOR_ATTACKS.values():
                    dodges.append(move)
            
            dodged = True # Check if defender successfully dodged
            if State.players[cls.attacker].history.getHead(): # Get attack from last beat
                for attack in State.players[cls.attacker].history.getHead().getData(): # Check if defender successfully dodged
                    if not (dodges in cls.DODGES_FOR_ATTACKS[attack]):
                        dodged = False
                        audio.hit.play()
                        return not dodged # If failed to dodge, return True to record a hit
        
        audio.defensive_sound.play()
        cls.aggressive = not cls.aggressive # Switch aggressive/defensive beat
        return False # Return False because no hit should be recorded
