#!/usr/bin/nodejs

const url = process.argv[2];

const request = require('request');
request(url, function (error, response, body) {
  if (error) return console.log(error);
  const d = JSON.parse(body);
  const js = d.results;
  let res = 0;
  for (const md of js) {
    for (const cht of md.characters) {
      if (cht.slice(-4) === '/18/') {
        res += 1;
      }
    }
  }
  console.log(res);
});
