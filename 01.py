from __future__ import annotations

import sys

def is_leap_year(year: int) -> bool:
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def days_in_month(year: int, month: int) -> int:
	if month == 2:
		return 29 if is_leap_year(year) else 28
	if month in (1, 3, 5, 7, 8, 10, 12):
		return 31
	return 30

def days_since_1_1_1(year: int, month: int, day: int) -> int:
	if year < 1 or not (1 <= month <= 12):
		raise ValueError("Invalid year or month")
	dim = days_in_month(year, month)
	if day < 1 or day > dim:
		raise ValueError("Invalid day")

	days = 0
	for y in range(1, year):
		days += 366 if is_leap_year(y) else 365
	for m in range(1, month):
		days += days_in_month(year, m)
	days += day - 1
	return days


def date_from_days(days: int) -> tuple[int, int, int]:
	if days < 0:
		raise ValueError("days must be non-negative")

	year = 1
	while True:
		year_days = 366 if is_leap_year(year) else 365
		if days < year_days:
			break
		days -= year_days
		year += 1

	month = 1
	while True:
		dim = days_in_month(year, month)
		if days < dim:
			break
		days -= dim
		month += 1

	day = days + 1
	return year, month, day


def add_days(year: int, month: int, day: int, n: int) -> tuple[int, int, int]:
	if n < 0:
		raise ValueError("n must be non-negative")
	base = days_since_1_1_1(year, month, day)
	return date_from_days(base + n)


def parse_args(argv: list[str]) -> tuple[int, int, int, int]:
	if len(argv) != 5:
		raise ValueError("Usage: python 01.py yyyy mm dd n")
	return int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4])


def main() -> None:
	try:
		y, m, d, n = parse_args(sys.argv)
	except ValueError:
		# Fallback to stdin: yyyy mm dd n
		parts = sys.stdin.read().strip().split()
		if len(parts) != 4:
			raise SystemExit("Provide: yyyy mm dd n")
		y, m, d, n = map(int, parts)

	y2, m2, d2 = add_days(y, m, d, n)
	print(f"{y2} {m2} {d2}")


if __name__ == "__main__":
	main()