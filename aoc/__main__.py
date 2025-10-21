from typing import override

from tap import Tap

from aoc import solver


class Args(Tap):
    year: int  # pyright: ignore[reportUninitializedInstanceVariable]
    day: int  # pyright: ignore[reportUninitializedInstanceVariable]
    part: int  # pyright: ignore[reportUninitializedInstanceVariable]

    @override
    def configure(self):
        self.add_argument("year")  # pyright: ignore[reportUnknownMemberType]
        self.add_argument("day")  # pyright: ignore[reportUnknownMemberType]
        self.add_argument("part")  # pyright: ignore[reportUnknownMemberType]


def main() -> None:
    args = Args().parse_args()
    result = solver.run(args.year, args.day, args.part)
    print(f"Ran {args.year} Day {args.day:02} Part {args.part}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
