#!/usr/bin/nodejs
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const wid = this.width;
    const hei = this.height;
    let idx = 0;
    while (idx < hei) {
      let idy = 0;
      while (idy < wid) {
        process.stdout.write('X');
        idy++;
      }
      process.stdout.write('\n');
      idx++;
    }
  }
};
