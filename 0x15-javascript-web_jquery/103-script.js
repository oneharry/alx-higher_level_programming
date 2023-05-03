const request = require('request');

$(document).ready(() => {
  const translate = () => {
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    request(url, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      const hello = JSON.parse(body).hello;
      $('DIV#hello').text(hello);
    });
  };

  const lang = $('INPUT#language_code').val();
  $('INPUT#btn_translate').click(translate());
  $('INPUT#btn_translate').keypress((e) => {
    if (e.which === 13) {
      translate();
      return false;
    }
  });
});
