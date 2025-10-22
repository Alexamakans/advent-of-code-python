#!/usr/bin/env sh

YEAR="$1"
DAY=$(printf '%02d' "$2")

cp aoc/years/y${YEAR}/day01/* aoc/years/y${YEAR}/day${DAY}/
