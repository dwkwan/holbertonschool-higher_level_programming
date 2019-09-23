#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
let key;
for (key in dict) {
  if (dict[key] in newDict) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
