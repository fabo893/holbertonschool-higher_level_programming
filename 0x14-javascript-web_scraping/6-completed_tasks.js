#!/usr/bin/nodejs

const url = process.argv[2];

const request = require('request');
request(url, function (error, response, body) {
  if (error) return console.log(error);
  const d = JSON.parse(body);
  const completed = {};
  let uid;

  for (const x of d) {
    uid = x.userId;
    if (x.completed === true) {
      completed[uid] = (completed[uid] || 0) + 1;
    }
  }

  console.log(completed);
});
