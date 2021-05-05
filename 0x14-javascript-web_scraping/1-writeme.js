#!/usr/bin/nodejs

const path = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(path, str, 'utf8', err => {
  if (err) return console.log(err);
});
