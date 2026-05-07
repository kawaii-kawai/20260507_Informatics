from __future__ import annotations

import sys
import datetime

def main() -> None:
    if len(sys.argv) != 5:
        print("Usage: python 01.py yyyy mm dd n")
        return
    try:
        y, m, d, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        date = datetime.date(y, m, d)
        new_date = date + datetime.timedelta(days=n)
        print(new_date.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()