"""A-Maze-ing: generate a maze from a configuration file."""

import sys

from parsing.config import ConfigError, parse_config


def main() -> None:
    """Run the maze program with the config file given as argument."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)

    try:
        config = parse_config(sys.argv[1])
    except ConfigError as error:
        print(f"Error: {error}")
        sys.exit(1)

    print("Config loaded:")
    print(f"  size:    {config.width} x {config.height}")
    print(f"  entry:   {config.entry}")
    print(f"  exit:    {config.exit}")
    print(f"  output:  {config.outputfile}")
    print(f"  perfect: {config.perfect}")
    print(f"  seed:    {config.seed}")


if __name__ == "__main__":
    main()
