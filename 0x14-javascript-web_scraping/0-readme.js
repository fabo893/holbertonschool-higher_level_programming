#!/usr/bin/nodejs

const args = process.argv[2];
const fs = require('fs');

fs.readFile(args, 'utf8', function (err, data) {
  if (err) return console.log(err);
  console.log(data);
});
