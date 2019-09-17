#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const part = process.argv.slice(2);
  let i;
  let position;
  let second;
  let max = part[0];
  for (i = 0; i < part.length; i++) {
    if (part[i] > max) {
      max = part[i];
      position = i;
    }
  }
  second = part[0];
  for (i = 0; i < part.length; i++) {
    if (part[i] > second & i !== position) {
      console.log(part[i]);
      second = part[i];
    }
  }
  console.log(second);
}
