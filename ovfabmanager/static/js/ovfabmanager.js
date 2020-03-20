$(document).ready(function(){
  $( document ).tooltip();

  $("#premier").click(function(){
        console.log("11111.....");
  });

  $("#second").click(function(){
	$("#deuxieme_modal").dialog();
  });

  $("#troisieme").click(function(){
	$("#troisieme_modal").dialog();
  });
});
