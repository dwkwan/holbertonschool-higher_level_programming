$(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/?lang=' + code, function (resp) {
      $('#hello').html(resp.hello);
    });
  });
  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  }
  );
});
