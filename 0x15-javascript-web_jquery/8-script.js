#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const filmArr = JSON.parse(body).results;
  filmArr.forEach(film => $('UL#list_movies').append(`<li>${film.title}</li>`));
});
