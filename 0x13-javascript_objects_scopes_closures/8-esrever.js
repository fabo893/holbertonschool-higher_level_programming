#!/usr/bin/nodejs
exports.esrever = function (list) {
  const ar = [];
  let idx = list.length - 1;
  while (idx >= 0) {
    ar.push(list[idx]);
    idx--;
  }
  return ar;
};
