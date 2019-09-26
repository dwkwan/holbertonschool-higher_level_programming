$.get('https://swapi.co/api/films/?format=json', function (resp) {
  for (var i = 0; i < resp.results.length; i++) {
    $('#list_movies').append(`<li>${resp.results[i].title}</li>`);
  }
});
