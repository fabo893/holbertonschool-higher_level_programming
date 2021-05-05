#!/usr/bin/nodejs

const mId = process.argv[2] - 1;
const api = 'https://swapi-api.hbtn.io/api';
const films = api + '/films';

const request = require('request');
request(films, function (error, response, body) {
  if (error || mId < 0) return console.log(error);

  const filmsJson = JSON.parse(body);
  const filmsResults = filmsJson.results[mId];
  const characters = filmsResults.characters;

  for (const character of characters) {
    request(character, function (err, response, body) {
      if (err) return console.log(err);
      const ch = JSON.parse(body);

      console.log(ch.name);
    });
  }
});
