#!/usr/bin/node
const request = require('request');
const arg = process.argv;
if (arg.length > 1) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + arg[2];
  request(url, (err, res, body) => {
    if (err) {
      return;
    }
    const charas = JSON.parse(body).characters;

    charas.forEach(ch => {
      request(ch, (err, res, body) => {
        if (err) {
          console.log(err);
          return;
        }
        const char = JSON.parse(body).name;
        console.log(char);
      });
    });
  });
}
