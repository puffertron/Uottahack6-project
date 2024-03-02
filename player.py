from linked_list import LinkedList

class Player():
    """Holds information unique t o each player; in particular, e.g., stance history, audio clips"""
    def __init__(self):
        self.history = LinkedList()