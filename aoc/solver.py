import importlib
from types import ModuleType
from typing import Callable, Protocol

from aoc import util


def run(year: int, day: int, part: int) -> str:
    # Allow short form (17 instead of 2017).
    # First AoC year is 2015 so no need to support 1900s.
    if year < 2000:
        year += 2000
    solver = load(year, day)
    match part:
        case 1:
            input = util.load_input(year, day)
            return solver.part_one(input)
        case 2:
            input = util.load_input(year, day)
            return solver.part_two(input)
        case _:
            raise SystemExit(f"part must be 1 or 2, was {part}.")


class SolverModule(Protocol):
    part_one: Callable[[str], str]
    part_two: Callable[[str], str]


def load(year: int, day: int) -> SolverModule:
    module_path = f"years.y{year}.day{day:02}.solver"
    try:
        module: ModuleType = importlib.import_module(module_path)
    except ModuleNotFoundError as e:
        raise SystemExit(f"Couldn't import solver '{module_path}'. {e}") from e

    for fn in ("part_one", "part_two"):
        if not hasattr(module, fn) or not callable(getattr(module, fn)):  # pyright: ignore[reportAny]
            raise SystemExit(f"Solver '{module_path}' is missing a callable '{fn}()'.")

    return module  # pyright: ignore[reportReturnType]
