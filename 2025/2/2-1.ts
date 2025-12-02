import fs from "fs";

function numberDuplicate(num: number, repeats = 2) {
  return Number(num.toString().repeat(repeats));
}

const file = fs.readFileSync("2.txt", "utf-8");
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

let invalidIdSum = 0;

for (const range of ranges) {
  // odd length product ids are always valid
  if (range[0].length % 2 == 1) continue;

  // e.g. '161112' - '224439'
  //      161 112     224 439
  // becomes
  //      161 161
  // then 162 162, 163 163, etc

  const midLength = range[0].length / 2;

  const startFirst = Number(range[0].substring(0, midLength));
  const startSecond = Number(range[0].substring(midLength));
  const endFirst = Number(range[1].substring(0, midLength));
  const endSecond = Number(range[1].substring(midLength));

  let duplicateVal = startFirst;

  if (startSecond > startFirst) {
    duplicateVal += 1;
  }

  while (
    duplicateVal <= endFirst &&
    (duplicateVal < endFirst || duplicateVal <= endSecond)
  ) {
    invalidIdSum += numberDuplicate(duplicateVal);
    duplicateVal += 1;
  }
}

console.log(invalidIdSum);

console.log();

export {};
