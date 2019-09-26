$.getJSON('https://swapi.co/api/people/5/?format=json', function (resp) {
  $('#character').text(resp.name);
});
