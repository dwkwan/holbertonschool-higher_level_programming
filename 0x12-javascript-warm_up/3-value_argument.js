#!/usr/bin/node
if (process.argv[3] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
