REQUIRED_KEYS = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]


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
    """Convert text into an int, raising ConfigError if it is not one."""
    try:
        return int(text)
    except ValueError:
        raise ConfigError(
            f"{key} must be a whole number, got '{text}'"
        ) from None


def parse_coor(key: str, text: str) -> tuple[int, int]:
    """Convert 'x,y' text into an (x, y) tuple of ints."""
    parts = text.split(",")

    if len(parts) != 2:
        raise ConfigError(f"{key} must look like x,y, got '{text}'")
    x = parse_int(key, parts[0])
    y = parse_int(key, parts[1])

    return (x, y)


def check_inside(
    key: str, position: tuple[int, int], width: int, height: int
) -> None:
    """Raise ConfigError if position is outside a width x height maze."""
    x, y = position
    if x < 0 or x >= width or y < 0 or y >= height:
        raise ConfigError(
            f"{key} {x},{y} is outside the maze "
            f"(x must be 0-{width - 1}, y must be 0-{height - 1})"
        )


def parse_config(path: str) -> Config:
    """Read and validate the config file, returning a Config object."""
    values = read_config_file(path)

    for key in REQUIRED_KEYS:
        if key not in values:
            raise ConfigError(f"Missing mandatory key: {key}")
        if values[key] == "":
            raise ConfigError(f"{key} has no value")

    width = parse_int("WIDTH", values["WIDTH"])
    height = parse_int("HEIGHT", values["HEIGHT"])
    if width <= 0 or height <= 0:
        raise ConfigError("WIDTH and HEIGHT must be greater than 0")

    entry_pos = parse_coor("ENTRY", values["ENTRY"])
    exit_pos = parse_coor("EXIT", values["EXIT"])
    check_inside("ENTRY", entry_pos, width, height)
    check_inside("EXIT", exit_pos, width, height)
    if entry_pos == exit_pos:
        raise ConfigError("ENTRY and EXIT must be different")

    outputfile = values["OUTPUT_FILE"]
    perfect = parse_bool("PERFECT", values["PERFECT"])

    seed: int | None = None
    if "SEED" in values:
        seed = parse_int("SEED", values["SEED"])

    return Config(
        width, height, entry_pos, exit_pos, outputfile, perfect, seed
    )
