#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
let movieDict = {};
let characterDict = {};
let i = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    movieDict = JSON.parse(body);
    for (i = 0; i < movieDict.characters.length; i++) {
      request(movieDict.characters[i], function (error, request, body) {
        if (error) {
          console.log(error);
        } else {
          characterDict = JSON.parse(body);
          console.log(characterDict.name);
        }
      });
    }
  }
});
