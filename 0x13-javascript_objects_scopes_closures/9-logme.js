#!/usr/bin/node
exports.logMe = (function (item) {
  let counter = -1;
  return function (item) { counter += 1; console.log(counter + ': ' + item); };
})();
