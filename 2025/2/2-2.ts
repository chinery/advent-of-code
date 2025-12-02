import fs from "fs";

const filename = "2.txt";

function numberDuplicate(num: number, repeats = 2) {
  return Number(num.toString().repeat(repeats));
}

function chunkString(str: string, chunkSize: number) {
  const arr = [];
  for (let i = 0; i < str.length; i += chunkSize) {
    arr.push(str.substring(i, i + chunkSize));
  }
  return arr;
}

function* divisors(num: number) {
  const half = num / 2;
  let x = 1;
  yield x;
  while (++x <= half) {
    if (num % x == 0) yield x;
  }
}

function* duplicateNumberGeneratorLength(
  start: number,
  end: number,
  repeats: number
) {
  for (let x = start; x <= end; x++) {
    yield numberDuplicate(x, repeats);
  }
}

function* invalidIdGenerator(start: string, end: string) {
  // idea: 161112 - 224439
  // take string length, find divisors
  //  6 = 3, 2, 1
  // for each divisor, split, then generate all values between start and end

  // properly speaking should add duplicate prevention in here
  // but I've already got it at the global level in case any ranges overlap

  for (const divisor of divisors(start.length)) {
    const startChunks = chunkString(start, divisor).map((s) => Number(s));
    const endChunks = chunkString(end, divisor).map((s) => Number(s));

    // annoying acrobatics to find starting number
    // e.g. 16 11 19 starts on 16 16 16 (because 16 > 11)
    //      16 18 10 starts on 17 17 17 (because 16 < 18)
    //      16 16 19 starts on 17 17 17 (because 16 = 16, 16 < 19)
    //      16 16 16 starts on 16 16 16
    let startDupe = startChunks[0];
    let ptr = 1;
    while (ptr < startChunks.length) {
      if (startDupe > startChunks[ptr]) break;
      if (startDupe < startChunks[ptr]) {
        startDupe++;
        break;
      }
      ptr++;
    }

    // similarly for end but reversed
    // e.g. 22 44 39 ends on 22 22 22
    //      22 10 39 ends on 21 21 21
    let endDupe = endChunks[0];
    ptr = 1;
    while (ptr < endChunks.length) {
      if (endDupe < endChunks[ptr]) break;
      if (endDupe > endChunks[ptr]) {
        endDupe--;
        break;
      }
      ptr++;
    }

    const quotient = start.length / divisor;
    yield* duplicateNumberGeneratorLength(startDupe, endDupe, quotient);
  }
}

const file = fs.readFileSync(filename, "utf-8");
const ranges = file
  .trim()
  .split(",")
  .map((range: string) => range.split("-"));

// convert ranges to ensure same string length for sanity
// e.g. 1-20 becomes 1-9 and 10-20
//      9827-16119 becomes 9827-9999 and 10000-16119
for (let i = 0; i < ranges.length; i++) {
  const range = ranges[i];
  if (range[0].length != range[1].length) {
    const newRange = [`1${"0".repeat(range[0].length)}`, range[1]];
    range[1] = "9".repeat(range[0].length);
    ranges.splice(i + 1, 0, newRange);
    i++;
  }
}

// to prevent duplicates (within one range and across ranges if that exists)
const invalidIds = new Set<number>();

for (const range of ranges) {
  if (range[0].length == 1) continue;

  for (const invalidId of invalidIdGenerator(range[0], range[1])) {
    invalidIds.add(invalidId);
  }
}

let invalidIdSum = 0;
invalidIds.forEach((id) => (invalidIdSum += id));

console.log(invalidIdSum);

export {};
