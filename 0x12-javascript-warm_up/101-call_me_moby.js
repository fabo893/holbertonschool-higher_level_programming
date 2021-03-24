#!/usr/bin/nodejs
exports.callMeMoby = function (x, theFunction) {
  let idx = 0;
  while (idx < x) {
    theFunction();
    idx++;
  }
};
