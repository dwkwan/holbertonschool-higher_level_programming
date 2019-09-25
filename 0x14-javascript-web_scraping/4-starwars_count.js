#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let resultDict = {};
let count = 0;
let i = 0;
let j = 0;
request(url, function (
  error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resultDict = JSON.parse(body);
    for (i = 0; i < resultDict.results.length; i++) {
      for (j = 0; j < resultDict.results[i].characters.length; j++) {
        if (resultDict.results[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
