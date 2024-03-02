from State import State.player0 as player0, State.player1 as player1

class Fight:
    """Holds current gamemode and does the logic on the stances to find out what happens"""
    gamemode: int

    # Gamemode 1: Dance battle
    attacker = 0
    attack_beat = True
    @classmethod
    def danceBattle(cls, stance0: list[str], stance1: list[str]):
        player0.addStance(stance0) # TODO rename to actual
        player1.addStance(stance1) # TODO rename to actual

        # TODO add the logic

        cls.attack_beat = not cls.attack_beat
