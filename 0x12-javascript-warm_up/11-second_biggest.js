#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const mod = process.argv.slice(2);
  mod.sort((a, b) => b - a);
  console.log(mod[1]);
}
