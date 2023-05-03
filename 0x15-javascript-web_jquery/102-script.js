const request = require('request');

$(document).ready(() => {
  const lang = $('INPUT#language_code').val();
  $('INPUT#btn_translate').click(() => {
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    request(url, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      const hello = JSON.parse(body).hello;
      $('DIV#hello').text(hello);
    });
  });
});
