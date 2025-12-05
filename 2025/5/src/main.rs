use std::fs::File;
use std::io;
use std::io::prelude::*;
use std::collections::HashSet;

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
    let mut ranges_to_ignore= HashSet::new();

    for i in 0..ranges.len() {
        if ranges_to_ignore.contains(&i) {continue;}

        let range = ranges[i];
        let start = range.start;
        let mut end = range.end;

        // check if this range overlaps any subsequent ones
        for j in i+1..ranges.len() {
            let next_range = ranges[j];
            if end < next_range.start {break;}
            else if end < next_range.end {
                // if partial overlap - truncate this range
                end = next_range.start-1;
                break;
            } else {
                // if full overlap - ignore the subsumed range
                ranges_to_ignore.insert(j);
            }
        }
        
        fresh_count += end - start + 1;
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
