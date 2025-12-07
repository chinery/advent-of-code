import strutils

let filename = "7.txt"
let lines = filename.readFile.strip.splitLines

type GridColumn = int16
type Indices = set[GridColumn]
type BeamCount = seq[int]

proc stringIndices(s: string, target: char): Indices =
    for i, c in s:
        if c == target:
            result.incl i.GridColumn

proc shift(ixs: Indices, delta: int16): Indices =
    for ix in ixs:
        result.incl ix + delta

proc splitBeams(counts: BeamCount, ixs: Indices): BeamCount =
    result = counts
    for i in ixs:
        result[i-1] += counts[i]
        result[i+1] += counts[i]
        result[i] = 0

let start = lines[0].find('S').GridColumn
var beams: Indices = {start}

# seems like a shame you can't write 
#    lines[0].len.newSeq[int]
# unless I'm missing something!
var beamCount: BeamCount = newSeq[int](len(lines[0]))
beamCount[start] += 1

var universes = 1
for line in lines:
    # each splitter adds one universe for each beam (universe) on its column
    # counts on line n are summed into line n+1, shifted ±1 space
    # e.g. 
    #   ...2.1..
    #   ...^.^..
    #   ..2.3.1.
    # where 1,2,3... mean that many | on that column

    let splitters = stringIndices(line, '^')
    let splits = beams * splitters

    for split in splits:
        universes += beamCount[split]

    let left = shift(splits, -1)
    let right = shift(splits, 1)

    beamCount = splitBeams(beamCount, splits)

    beams = beams - splits + left + right

echo universes


