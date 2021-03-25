#!/usr/bin/nodejs
exports.converter = function (base) {
  return function converter (num) {
    return num.toString(base);
  };
};
