#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let movieDict = {};
const count = 0;
let i = 0;
const j = 0;
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
