/* function addingImages(){
    for (var i=1; i<=50; i++){
        image='<img src="http://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/' + i + '.png">';
    }
    $("#imga").html(image);
} */


$(document).ready(function(){
    for (var i = 0; i < 151; i++) {
      $('body').append(`<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/${i}.png">`) 
    }
  })