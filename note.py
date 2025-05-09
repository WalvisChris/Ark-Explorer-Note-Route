class Note:
    def __init__(self, name: str, position: tuple) -> None:
        self.name = name
        self.position = position

    def __str__(self) -> str:
        return self.name