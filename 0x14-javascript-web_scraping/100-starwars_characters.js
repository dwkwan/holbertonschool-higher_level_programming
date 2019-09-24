#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let movieDict = {};
let characterDict = {};
let i = 0;
request(url, function (
  response, body) {
  movieDict = JSON.parse(body.body);
  for (i = 0; i < movieDict.characters.length; i++) {
    request(movieDict.characters[i], function (request, body) {
      characterDict = JSON.parse(body.body);
      console.log(characterDict.name);
    });
  }
});
