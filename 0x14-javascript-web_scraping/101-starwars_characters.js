#!/usr/bin/nodejs

const request = require('request');

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        const ch = JSON.parse(body);
        resolve(ch.name);
      } else {
        reject(error);
      }
    });
  });
}

async function main (film) {
  const characters = film.characters;

  for (const characterApi of characters) {
    const res = await doRequest(characterApi);
    console.log(res);
  }
}

const filmApi = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(filmApi, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const film = JSON.parse(body);

  main(film);
});
