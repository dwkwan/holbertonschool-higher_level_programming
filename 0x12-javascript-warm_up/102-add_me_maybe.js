#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  x = x + 1;
  theFunction(x);
};
