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
        seed: int | None = None,
    ) -> None:
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit
        self.outputfile = outputfile
        self.perfect = perfect
        self.seed = seed


class ConfigError(Exception):
    """Raised when the configuration file is invalid."""


def read_config_file(path: str) -> dict[str, str]:
    """Read the config file and return KEY -> VALUE text pairs."""
    values: dict[str, str] = {}

    try:
        with open(path) as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise ConfigError(f"File not found: {path}") from None
    except PermissionError:
        raise ConfigError(f"Cannot read file: {path}") from None

    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        if "=" not in line:
            raise ConfigError(f"Invalid line (missing '='): {line}")

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if key == "":
            raise ConfigError(f"Invalid line (empty key): {line}")
        if key in values:
            raise ConfigError(f"Duplicate key: {key}")
        values[key] = value

    return values
