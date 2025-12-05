use std::fs::File;
use std::{cmp, io};
use std::io::prelude::*;

#[derive(Debug, Clone, Copy)]
struct Range {
    start: i64,
    end: i64
}

impl Range {
    fn new(start: &str, end: &str) -> Range {
        Range {
            start: start.parse::<i64>().expect("invalid int"),
            end: end.parse::<i64>().expect("invalid int")
        }
    }
}

fn read_input(filename: &str) -> io::Result<(Vec<Range>, Vec<i64>)> {
    let mut ranges = Vec::new();
    let mut ingredients = Vec::new();

    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);
    
    let mut reading_ranges = true;

    for line in reader.lines() {
        let line = line?;
        if reading_ranges && line.is_empty() {
            reading_ranges = false;
            continue;
        } else if reading_ranges {
            let range = line.split_once("-").expect("range line without -");
            ranges.push(Range::new(range.0, range.1));
        } else {
            ingredients.push(line.parse::<i64>().expect("invalid int"))
        }
    }
    Ok((ranges, ingredients))
}

fn part_one(filename: &str) {
    let (mut ranges, ingredients) = read_input(filename).expect("error loading data");
    ranges.sort_by_key(|a| a.start);

    let mut fresh_count: i32 = 0;

    for ingredient in ingredients {
        for range in &ranges {
            if ingredient < range.start {
                // ranges sorted, so this is not in any range
                break
            }
            if range.start <= ingredient && ingredient <= range.end {
                fresh_count += 1;
                break;
            }
        }
    }

    println!("Part one fresh: {}", fresh_count);
}

fn part_two(filename: &str) {
    let (mut ranges, _) = read_input(filename).expect("error loading data");
    ranges.sort_by_key(|a| a.start);

    let mut fresh_count: i64 = 0;
    let Range {start: mut running_start, end: mut running_end} = ranges[0];

    for i in 1..ranges.len() {
        let Range {start: next_start, end: next_end} = ranges[i];
        if next_start > running_end {
            fresh_count += running_end - running_start + 1;
            (running_start, running_end) = (next_start, next_end);
        }
        else {
            running_end = cmp::max(running_end, next_end);
        }
    }

    println!("Part two fresh: {}", fresh_count);
}

fn main() {
    let filename = "5.txt";

    let start = std::time::Instant::now();
    part_one(filename);
    println!("\telapsed: {:?}", start.elapsed());

    let start = std::time::Instant::now();
    part_two(filename);
    println!("\telapsed: {:?}", start.elapsed());
}
