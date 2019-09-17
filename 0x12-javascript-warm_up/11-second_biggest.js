#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const mod = process.argv.slice(2);
  let i;
  let first = Number.MIN_VALUE;
  let second = Number.MIN_VALUE;
  for (i = 0; i < mod.length; i++) {
    if (mod[i] > first) {
      second = first;
      first = mod[i];
    }
    if (first > mod[i] > second) {
      second = mod[i];
    }
  }
  console.log(second);
}
