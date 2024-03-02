from linked_list import LinkedList
# Player holds info about the player like its audio clips and last few stances

class Player():
    history = LinkedList()
    #example of insert
    history.insertAtFront(['a','b'])
    #get the head object
    obj = history.getHead()
    #get the next pointer
    history.getNext(obj)

    def __init__(self) -> None:
        pass
