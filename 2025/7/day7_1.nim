import strutils

let filename = "7.txt"
let lines = filename.readFile.strip.splitLines

type GridColumn = int16
type Indices = set[GridColumn]

proc stringIndices(s: string, target: char): Indices =
    for i, c in s:
        if c == target:
            result.incl i.GridColumn

proc shift(ixs: Indices, delta: int16): Indices =
    for ix in ixs:
        result.incl ix + delta


let start = lines[0].find('S').GridColumn

var beams: Indices = {start}
var splits = 0
for line in lines:
    # if line n has beam positions {10, 15, 101}
    # and there's a splitter at {15}
    # new beams are {10, 14, 16, 101}

    let splitters = stringIndices(line, '^')
    let split = beams * splitters

    splits += len(split)

    let left = shift(split, -1)
    let right = shift(split, 1)

    beams = beams - split + left + right

echo splits


