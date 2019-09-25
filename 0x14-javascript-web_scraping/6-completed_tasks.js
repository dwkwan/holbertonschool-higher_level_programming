#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let resultList = [];
let i = 0;
const countDict = {};
let key = '';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resultList = JSON.parse(body);
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
  }
});
