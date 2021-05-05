#!/usr/bin/nodejs

let get = process.argv[2];

const request = require('request');
get = 'https://swapi-api.hbtn.io/api/people/18/';
request(get, function (error, response, body) {
  if (error) return console.log(error);
  const d = JSON.parse(body);
  const films = d.films;
  console.log(films.length);
});
