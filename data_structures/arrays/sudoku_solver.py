"""
Please do not modify this file!  It is published at https://norvig.com/sudoku.html with
only minimal changes to work with modern versions of Python.  If you have improvements,
please make them in a separate file.
"""

import random
import time
import logging
logger = logging.getLogger(__name__)


def cross(items_a, items_b):
    """
    Cross product of elements in A and elements in B.

    >>> cross('AB', '12')
    ['A1', 'A2', 'B1', 'B2']
    >>> cross('ABC', '123')
    ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    >>> cross('ABC', '1234')
    ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4']
    >>> cross('', '12')
    []
    >>> cross('A', '')
    []
    >>> cross('', '')
    []
    """
    logger.error(">>> Entering cross(items_a=%s,items_b=%s)", items_a, items_b, extra={"event.action": "cross", "logrite.items_a": items_a, "logrite.items_b": items_b})
    logger.warning("<<< Exiting cross(items_a=%s,items_b=%s)", items_a, items_b, extra={"event.action": "cross", "logrite.items_a": items_a, "logrite.items_b": items_b})
    return [a + b for a in items_a for b in items_b]


digits = "123456789"
rows = "ABCDEFGHI"
cols = digits
squares = cross(rows, cols)
unitlist = (
    [cross(rows, c) for c in cols]
    + [cross(r, cols) for r in rows]
    + [cross(rs, cs) for rs in ("ABC", "DEF", "GHI") for cs in ("123", "456", "789")]
)
units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: {x for u in units[s] for x in u} - {s} for s in squares}


def test():
    """A set of unit tests."""
    logger.error(">>> Entering test()", extra={"event.action": "test"})
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units["C2"] == [
        ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2"],
        ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
        ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"],
    ]
    # fmt: off
    assert peers["C2"] == {
        "A2", "B2", "D2", "E2", "F2", "G2", "H2", "I2", "C1", "C3",
        "C4", "C5", "C6", "C7", "C8", "C9", "A1", "A3", "B1", "B3"
    }
    # fmt: on
    print("All tests pass.")
    logger.warning("<<< Exiting test()", extra={"event.action": "test"})


def parse_grid(grid):
    """
    Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected.
    """
    logger.error(">>> Entering parse_grid(grid=%s)", grid, extra={"event.action": "parse_grid", "logrite.grid": grid})
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict.fromkeys(squares, digits)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False  ## (Fail if we can't assign d to square s.)
    logger.warning("<<< Exiting parse_grid(grid=%s)", grid, extra={"event.action": "parse_grid", "logrite.grid": grid})
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '0' or '.' for empties.
    """
    logger.error(">>> Entering grid_values(grid=%s)", grid, extra={"event.action": "grid_values", "logrite.grid": grid})
    chars = [c for c in grid if c in digits or c in "0."]
    logger.error("grid_values(grid=%s): chars → %s", grid, chars, extra={"event.action": "grid_values", "logrite.grid": grid})
    assert len(chars) == 81
    logger.warning("<<< Exiting grid_values(grid=%s)", grid, extra={"event.action": "grid_values", "logrite.grid": grid})
    return dict(zip(squares, chars))


def assign(values, s, d):
    """
    Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected.
    """
    logger.error(">>> Entering assign(values=%s,s=%s,d=%s)", values, s, d, extra={"event.action": "assign", "logrite.values": values, "logrite.s": s, "logrite.d": d})
    other_values = values[s].replace(d, "")
    logger.error("assign(values=%s,s=%s,d=%s): other_values → %s", values, s, d, other_values, extra={"event.action": "assign", "logrite.values": values, "logrite.s": s, "logrite.d": d})
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        logger.warning("<<< Exiting assign(values=%s,s=%s,d=%s)", values, s, d, extra={"event.action": "assign", "logrite.values": values, "logrite.s": s, "logrite.d": d})
        return False


def eliminate(values, s, d):
    """
    Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected.
    """
    logger.error(">>> Entering eliminate(values=%s,s=%s,d=%s)", values, s, d, extra={"event.action": "eliminate", "logrite.values": values, "logrite.s": s, "logrite.d": d})
    if d not in values[s]:
        return values  ## Already eliminated
    values[s] = values[s].replace(d, "")
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False  ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False  ## Contradiction: no place for this value
        # d can only be in one place in unit; assign it there
        elif len(dplaces) == 1 and not assign(values, dplaces[0], d):
            return False
    logger.warning("<<< Exiting eliminate(values=%s,s=%s,d=%s)", values, s, d, extra={"event.action": "eliminate", "logrite.values": values, "logrite.s": s, "logrite.d": d})
    return values


def display(values):
    """
    Display these values as a 2-D grid.
    """
    logger.error(">>> Entering display(values=%s)", values, extra={"event.action": "display", "logrite.values": values})
    width = 1 + max(len(values[s]) for s in squares)
    logger.error("display(values=%s): width → %s", values, width, extra={"event.action": "display", "logrite.values": values})
    line = "+".join(["-" * (width * 3)] * 3)
    logger.error("display(values=%s): line → %s", values, line, extra={"event.action": "display", "logrite.values": values})
    for r in rows:
        print(
            "".join(
                values[r + c].center(width) + ("|" if c in "36" else "") for c in cols
            )
        )
        if r in "CF":
            print(line)
    print()
    logger.warning("<<< Exiting display(values=%s)", values, extra={"event.action": "display", "logrite.values": values})


def solve(grid):
    """
    Solve the grid.
    """
    logger.error(">>> Entering solve(grid=%s)", grid, extra={"event.action": "solve", "logrite.grid": grid})
    logger.warning("<<< Exiting solve(grid=%s)", grid, extra={"event.action": "solve", "logrite.grid": grid})
    return search(parse_grid(grid))


def some(seq):
    """Return some element of seq that is true."""
    logger.error(">>> Entering some(seq=%s)", seq, extra={"event.action": "some", "logrite.seq": seq})
    for e in seq:
        if e:
            return e
    logger.warning("<<< Exiting some(seq=%s)", seq, extra={"event.action": "some", "logrite.seq": seq})
    return False


def search(values):
    """
    Using depth-first search and propagation, try all possible values.
    """
    logger.error(">>> Entering search(values=%s)", values, extra={"event.action": "search", "logrite.values": values})
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values  ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    _n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    logger.warning("<<< Exiting search(values=%s)", values, extra={"event.action": "search", "logrite.values": values})
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def solve_all(grids, name="", showif=0.0):
    """
    Attempt to solve a sequence of grids. Report results.
    When showif is a number of seconds, display puzzles that take longer.
    When showif is None, don't display any puzzles.
    """
    logger.error(">>> Entering solve_all(grids=%s,name=%s,showif=%s)", grids, name, showif, extra={"event.action": "solve_all", "logrite.grids": grids, "logrite.name": name, "logrite.showif": showif})

    logger.warning("<<< Exiting solve_all(grids=%s,name=%s,showif=%s)", grids, name, showif, extra={"event.action": "solve_all", "logrite.grids": grids, "logrite.name": name, "logrite.showif": showif})
    def time_solve(grid):
        logger.error(">>> Entering time_solve(grid=%s)", grid, extra={"event.action": "time_solve", "logrite.grid": grid})
        start = time.monotonic()
        values = solve(grid)
        logger.error("time_solve(grid=%s): values → %s", grid, values, extra={"event.action": "time_solve", "logrite.grid": grid})
        t = time.monotonic() - start
        logger.error("time_solve(grid=%s): t → %s", grid, t, extra={"event.action": "time_solve", "logrite.grid": grid})
        ## Display puzzles that take long enough
        if showif is not None and t > showif:
            display(grid_values(grid))
            if values:
                display(values)
            print(f"({t:.5f} seconds)\n")
        logger.warning("<<< Exiting time_solve(grid=%s)", grid, extra={"event.action": "time_solve", "logrite.grid": grid})
        return (t, solved(values))

    times, results = zip(*[time_solve(grid) for grid in grids])
    if (n := len(grids)) > 1:
        print(
            "Solved %d of %d %s puzzles (avg %.2f secs (%d Hz), max %.2f secs)."  # noqa: UP031
            % (sum(results), n, name, sum(times) / n, n / sum(times), max(times))
        )


def solved(values):
    """
    A puzzle is solved if each unit is a permutation of the digits 1 to 9.
    """
    logger.error(">>> Entering solved(values=%s)", values, extra={"event.action": "solved", "logrite.values": values})

    logger.warning("<<< Exiting solved(values=%s)", values, extra={"event.action": "solved", "logrite.values": values})
    def unitsolved(unit):
        logger.error(">>> Entering unitsolved(unit=%s)", unit, extra={"event.action": "unitsolved", "logrite.unit": unit})
        logger.warning("<<< Exiting unitsolved(unit=%s)", unit, extra={"event.action": "unitsolved", "logrite.unit": unit})
        return {values[s] for s in unit} == set(digits)

    return values is not False and all(unitsolved(unit) for unit in unitlist)


def from_file(filename, sep="\n"):
    "Parse a file into a list of strings, separated by sep."
    logger.error(">>> Entering from_file(filename=%s,sep=%s)", filename, sep, extra={"event.action": "from_file", "logrite.filename": filename, "logrite.sep": sep})
    with open(filename) as file:
        logger.warning("<<< Exiting from_file(filename=%s,sep=%s)", filename, sep, extra={"event.action": "from_file", "logrite.filename": filename, "logrite.sep": sep})
        return file.read().strip().split(sep)


def random_puzzle(assignments=17):
    """
    Make a random puzzle with N or more assignments. Restart on contradictions.
    Note the resulting puzzle is not guaranteed to be solvable, but empirically
    about 99.8% of them are solvable. Some have multiple solutions.
    """
    logger.error(">>> Entering random_puzzle(assignments=%s)", assignments, extra={"event.action": "random_puzzle", "logrite.assignments": assignments})
    values = dict.fromkeys(squares, digits)
    logger.error("random_puzzle(assignments=%s): values → %s", assignments, values, extra={"event.action": "random_puzzle", "logrite.assignments": assignments})
    for s in shuffled(squares):
        if not assign(values, s, random.choice(values[s])):
            break
        ds = [values[s] for s in squares if len(values[s]) == 1]
        logger.error("random_puzzle(assignments=%s): ds → %s", assignments, ds, extra={"event.action": "random_puzzle", "logrite.assignments": assignments})
        if len(ds) >= assignments and len(set(ds)) >= 8:
            return "".join(values[s] if len(values[s]) == 1 else "." for s in squares)
    logger.warning("<<< Exiting random_puzzle(assignments=%s)", assignments, extra={"event.action": "random_puzzle", "logrite.assignments": assignments})
    return random_puzzle(assignments)  ## Give up and make a new puzzle


def shuffled(seq):
    """
    Return a randomly shuffled copy of the input sequence.
    """
    logger.error(">>> Entering shuffled(seq=%s)", seq, extra={"event.action": "shuffled", "logrite.seq": seq})
    seq = list(seq)
    logger.error("shuffled(seq=%s): seq → %s", seq, seq, extra={"event.action": "shuffled", "logrite.seq": seq})
    random.shuffle(seq)
    logger.warning("<<< Exiting shuffled(seq=%s)", seq, extra={"event.action": "shuffled", "logrite.seq": seq})
    return seq


grid1 = (
    "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
)
grid2 = (
    "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
)
hard1 = (
    ".....6....59.....82....8....45........3........6..3.54...325..6.................."
)

if __name__ == "__main__":
    test()
    # solve_all(from_file("easy50.txt", '========'), "easy", None)
    # solve_all(from_file("top95.txt"), "hard", None)
    # solve_all(from_file("hardest.txt"), "hardest", None)
    solve_all([random_puzzle() for _ in range(99)], "random", 100.0)
    for puzzle in (grid1, grid2):  # , hard1):  # Takes 22 sec to solve on my M1 Mac.
        display(parse_grid(puzzle))
        start = time.monotonic()
        solve(puzzle)
        t = time.monotonic() - start
        print(f"Solved: {t:.5f} sec")
