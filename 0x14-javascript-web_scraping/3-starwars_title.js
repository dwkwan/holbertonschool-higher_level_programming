#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let resultDict = {};
request(url, function (response, body) {
  resultDict = JSON.parse(body.body);
  console.log(resultDict["title"]);
});
