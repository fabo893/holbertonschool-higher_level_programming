#!/usr/bin/nodejs

const num = process.argv[2];

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + num;
request(url, function (error, response, body) {
  if (error) return console.log(error);
  const d = JSON.parse(body);
  console.log(d.title);
});
