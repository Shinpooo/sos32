

class StateVariable:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.optimal_position = None
        self.isStored = False