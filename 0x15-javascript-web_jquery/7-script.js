#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const name = JSON.parse(body).name;
  $('DIV#character').html(name);
});
