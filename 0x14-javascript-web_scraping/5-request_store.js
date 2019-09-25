#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
let text;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    text = body;
    fs.writeFile(process.argv[3], text, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
