const h = $('DIV#add_item');
h.click(() => {
  $('UL.my_list').append('<li>Item</li>');
});
