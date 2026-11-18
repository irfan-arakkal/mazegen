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


def parse_bool(key: str, text: str) -> bool:
    """Convert 'True' or 'False' text into a bool."""
    if text == "True":
        return True
    if text == "False":
        return False
    raise ConfigError(f"{key} must be True or False, got '{text}'")


def parse_int(key: str, text: str) -> int:

    try:
        return int(text)
    except ValueError:
        raise ConfigError(
            f"{key} must be  whole numbers , got '{text}'"
        ) from None


def parse_coor(key: str, text: str) -> tuple[int, int]:

    parts = text.split(",")

    if len(parts) != 2:
        raise ConfigError(f"{key} must look like x,y, got '{text}'")
    x = parse_int(key, parts[0])
    y = parse_int(key, parts[1])

    return (x, y)
