$(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/?lang=' + code, function (resp) {
      $('#hello').text(resp.hello);
    });
  });
});
