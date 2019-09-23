#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  for (i = 0; i < list.length / 2; i++, j--) {
    [list[i], list[j]] = [list[j], list[i]];
  }
  return list;
};
