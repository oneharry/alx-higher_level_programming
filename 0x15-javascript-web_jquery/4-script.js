const h = $('DIV#toggle_header');
h.click(() => {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  } else {
    $('header').removeClass('red');
    $('header').addClass('green');
  }
});
