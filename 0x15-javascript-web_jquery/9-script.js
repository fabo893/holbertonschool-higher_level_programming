#!/usr/bin/nodejs

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (hello) {
      $('DIV#hello').text(hello.hello);
    }
  });
});
