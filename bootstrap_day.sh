#!/usr/bin/env sh

YEAR="$1"
DAY=$(printf '%02d' "$2")

mkdir -p aoc/years/y${YEAR}/day${DAY}
cp -r aoc/years/y${YEAR}/day01/* aoc/years/y${YEAR}/day${DAY}/
