from state import State
import audio
import pygame as pg


class Fight:
    """Holds current gamemode and does the logic on the stances to find out what happens"""
    gamemode: int #TODO - use gamemode to control which danceBattle to use (can we compartmentalize gamemode things?)

    # Gamemode 1: Dance battle
    attacker = 0 #0 or 1 to log which player is currently attacking
    aggressive = True
    DODGES_FOR_ATTACKS= {"nw": "sw",
                          "n": "s",
                          "ne": "se"}
    PARRIES_FOR_ATTACKS = {"nw": "w",
                           "n": "n",
                           "ne": "e"}
    @classmethod
    def danceBattle(cls, inputs: tuple[dict[str: list[str]], dict[str: list[str]]]) -> bool:
        """Takes a list of stances and updates game state. Player history will be a list of attacks."""
        #TODO make this only work in gamemode 1, add comment describing the game mode (maybe a tutorial text file?)
        stances = (inputs[0]["perfect"] + inputs[0]["good"], inputs[1]["perfect"] + inputs[1]["good"]) # Consider only pressed inputs neglecting quality
        print(stances)

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
                if not (cls.PARRIES_FOR_ATTACKS[attack] in parries):
                    parried = False

            if parried: # If attack was parried, lose advantage (also happens if no there was no attack)
                State.players[cls.attacker].history.insertAtFront([])
                cls.attacker = not cls.attacker
                if len(attacks) != 0:
                    audio.ticker.play(audio.parry_sound)
            else: # Otherwise, save last attack
                State.players[cls.attacker].history.insertAtFront(attacks) # Log attack that needs to be blocked
                audio.ticker.play(audio.aggressive_sound)

        else: # For defense beats
            dodges = [] # Create a list of current dodges

            for move in stances[not cls.attacker]: # Add valid dodges chosen
                if move in cls.DODGES_FOR_ATTACKS.values():
                    dodges.append(move)
            
            dodged = True # Check if defender successfully dodged
            if State.players[cls.attacker].history.getHead(): # Do nothing if head is None (start of game)
                for attack in State.players[cls.attacker].history.getHead().getData(): # Check if defender successfully dodged
                    if not (cls.DODGES_FOR_ATTACKS[attack] in dodges): # If any attack undodged, failed to dodge
                        dodged = False
                        audio.ticker.play(audio.hit_sound)
                        return not dodged # If failed to dodge, return True to record a hit
            else:
                #debugging
                print("START OF GAME: player.history.getHead() in fight returned None, this should only happen at start of game")

            #TODO - if dodged: play block noise or something
        
        audio.ticker.play(audio.defensive_sound)
        cls.aggressive = not cls.aggressive # Switch aggressive/defensive beat
        return False # Return False because no hit was recorded
