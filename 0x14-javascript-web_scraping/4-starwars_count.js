#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let resultDict = {};
let count = 0;
let i = 0;
request(url, function (
  response, body) {
  resultDict = JSON.parse(body.body);
  for (i = 0; i < resultDict.results.length; i++) {
    if (resultDict.results[i].characters.includes('https://swapi.co/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
