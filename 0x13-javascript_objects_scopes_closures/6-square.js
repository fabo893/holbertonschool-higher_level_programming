#!/usr/bin/nodejs
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let idx = 0;
    while (idx < this.width) {
      let idy = 0;
      while (idy < this.height) {
        process.stdout.write(c);
        idy++;
      }
      process.stdout.write('\n');
      idx++;
    }
  }
};
