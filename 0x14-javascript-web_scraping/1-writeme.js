#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
})
;
