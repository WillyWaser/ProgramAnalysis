from abc import ABC


class Declaration(ABC):

    def __init__(self, name: str):
        self.name = name