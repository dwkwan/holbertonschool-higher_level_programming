#!/usr/bin/node
const parentSquare = require('./5-square');
module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
