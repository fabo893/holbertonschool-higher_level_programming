#!/usr/bin/nodejs
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  let idx = 0;
  while (idx < list.length) {
    if (list[idx] === searchElement) {
      num += 1;
    }
    idx++;
  }
  return num;
};
