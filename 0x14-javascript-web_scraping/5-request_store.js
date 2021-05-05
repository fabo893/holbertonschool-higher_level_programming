#!/usr/bin/nodejs

const path = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');
request(path, function (error, response, body) {
  if (error) return console.log(error);
  fs.writeFile(file, body, err => {
    if (err) return console.log(err);
  });
});
