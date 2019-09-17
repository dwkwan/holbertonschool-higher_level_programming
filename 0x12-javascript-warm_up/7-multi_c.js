#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of occurences');
} else {
  let i;
  for (i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
