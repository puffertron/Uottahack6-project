from State import State.players as players

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
    def danceBattle(cls, stances: list[list[str]]) -> bool:
        """Takes a list of stances and updates game state"""
        if aggressive: # For aggressive beats
            attacks = [] # Create a list of current attacks
            parries = [] # Create a list of current parries

            for move in stances[attacker]: # Add valid attacks chosen
                if move in DODGES_FOR_ATTACKS.keys():
                    attacks.append(move)
            for move in stances[not attacker]
                if move in PARRIES_FOR_ATTACKS.values()
                    parries.append(move)
            
            parried = True
            for attack in attacks: # Check if defender successfully parried
                if not (parries contains PARRIES_FOR_ATTACKS[attack]):
                    parried = False

            if parried: # If attack was parried, lose advantage
                players[attacker].history.insertAtFront([])
                attacker = not attacker
            else: #otherwise, save last attack
                players[attacker].history.insertAtFront(attacks)

        else: # For defense beats
            dodges = [] # Create a list of current dodges

            for move in stances[not attacker]: # Add valid dodges chosen
                if move in DODGES_FOR_ATTACKS.values():
                    dodges.append(move)
            
            dodged = True
            for attack in players[attacker].history.getHead().getData(): # Check if defender successfully dodged
                if not (dodges contains DODGES_FOR_ATTACKS[attack]):
                    dodged = False
                    return not dodged # If failed to dodge, return True to record a hit

        cls.aggressive = not cls.aggressive # Switch aggressive/defensive beat
        return False # Return False because no hit should be recorded
