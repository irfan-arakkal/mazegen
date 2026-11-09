class Config:
    """Holds all values read from the configuration file."""

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        outputfile: str,
        perfect: bool,
        seed: int | None,
    ) -> None:
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit
        self.outputfile = outputfile
        self.perfect = perfect
        self.seed = seed
