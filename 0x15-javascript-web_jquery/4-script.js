#!/usr/bin/nodejs

$('DIV#toggle_header').click(function () {
  const $head = $('header');
  if ($head.hasClass('green')) {
    $head.removeClass('green').addClass('red');
  } else {
    $head.removeClass('red').addClass('green');
  }
});
