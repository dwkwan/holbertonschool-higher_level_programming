#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let resultDict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resultDict = JSON.parse(body);
    console.log(resultDict.title);
  }
});
