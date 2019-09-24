#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let resultList = [];
let i = 0;
const countDict = {};
let key = '';

request(url, function (response, body) {
  resultList = JSON.parse(body.body);
  for (i = 0; i < resultList.length; i++) {
    key = resultList[i].userId;
    if (resultList[i].completed === true) {
      if (!countDict[key]) {
        countDict[key] = 1;
      } else {
        countDict[key] += 1;
      }
    }
  }
  console.log(countDict);
});
