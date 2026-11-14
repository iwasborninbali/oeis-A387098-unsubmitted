#!/usr/bin/env python3
"""Independent exact enumeration for selected A387098(n,k) values.

No external packages. Run: python3 verify_kings.py > output.log
The program does not use OEIS algorithms or any lab verification code.
"""

from functools import lru_cache
from time import perf_counter, process_time
import platform


def kings(n: int, k: int) -> tuple[int, int]:
    """Return exact count and number of cached subproblems.

    A row mask has k non-neighboring set bits. Two consecutive row masks
    must have no kings in the same or neighboring columns. For each prefix
    remember the previous row and the per-column occupancy in base k+1.
    """
    if k == 0:
        return 1, 0
    if k > n:
        return 0, 0

    full = (1 << n) - 1
    rows = [m for m in range(1 << n)
            if m.bit_count() == k and not (m & (m << 1))]
    follows = {
        a: tuple(b for b in rows
                 if not (b & ((a | (a << 1) | (a >> 1)) & full)))
        for a in rows
    }
    powers = [(k + 1) ** j for j in range(n)]
    desired = k * sum(powers)
    positions = {m: tuple(j for j in range(n) if (m >> j) & 1)
                 for m in rows}

    @lru_cache(maxsize=None)
    def visit(depth: int, previous: int, occupancies: int) -> int:
        if depth == n:
            return int(occupancies == desired)
        total = 0
        for row in (rows if depth == 0 else follows[previous]):
            if any((occupancies // powers[j]) % (k + 1) == k
                   for j in positions[row]):
                continue
            new_occupancies = occupancies + sum(powers[j] for j in positions[row])
            total += visit(depth + 1, row, new_occupancies)
        return total

    value = visit(0, 0, 0)
    return value, visit.cache_info().currsize


# OEIS display, read 2026-11-15; zero cases extend the displayed triangle.
expected_k1 = (1, 0, 0, 2, 14, 90, 646, 5242, 47622, 479306,
               5296790, 63779034, 831283558, 11661506218,
               175203184374, 2806878055610)
checks = {(n, 0): 1 for n in range(1, 17)}
checks.update({(n, 1): v for n, v in enumerate(expected_k1, start=1)})
checks.update({(7, 2): 0, (8, 2): 2, (9, 2): 664,
               (10, 2): 146510, (11, 2): 31197434})
checks.update({(11, 3): 0, (12, 3): 2, (13, 3): 42732})
checks.update({(15, 4): 0, (16, 4): 2})


def main() -> None:
    cpu_start, wall_start = process_time(), perf_counter()
    print('A387098 independent row-mask / column-count DP')
    print('Python:', platform.python_version())
    print('Range: k=0,1 at n=1..16; k=2 at n=7..11;'
          ' k=3 at n=11..13; k=4 at n=15..16')
    all_ok = True
    for (n, k), expected in sorted(checks.items()):
        actual, states = kings(n, k)
        ok = (actual == expected)
        all_ok &= ok
        print(f'n={n:2d} k={k} T={actual} expected={expected}'
              f' states={states} {"PASS" if ok else "FAIL"}')
    print('Cases:', len(checks))
    print('All matched:', all_ok)
    print(f'CPU seconds: {process_time() - cpu_start:.3f}')
    print(f'Wall seconds: {perf_counter() - wall_start:.3f}')
    if not all_ok:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
