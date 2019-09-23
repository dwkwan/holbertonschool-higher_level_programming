#!/usr/bin/node
exports.logMe = (function (item) {
  let counter = 0;
  return function (item) { console.log(item + ': ' + counter); counter += 1; };
})();
