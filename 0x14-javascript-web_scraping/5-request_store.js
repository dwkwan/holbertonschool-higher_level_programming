#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
let text;
request(url, function (response, body) {
  text = body.body;
  fs.writeFile(process.argv[3], text, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
