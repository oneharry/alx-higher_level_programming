#!/usr/bin/node
const request = require('request');
const arg = process.argv;
let num;
let films;
let cha;
if (arg.length > 1) {
  const url = arg[2];
  request(url, (err, res, body) => {
    if (err) {
      return;
    }
    films = JSON.parse(body).results;
    num = films.filter(film => {
      cha = film.characters;
      return cha.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(num.length);
  });
}
