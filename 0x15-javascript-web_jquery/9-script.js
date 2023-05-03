const request = require('request');

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    const filmArr = JSON.parse(body).results;
    filmArr.forEach(film => $('UL#list_movies').append(`<li>${film.title}</li>`));
  });
});
