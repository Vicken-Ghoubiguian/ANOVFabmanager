$(document).ready(function(){
  $( document ).tooltip();

  $("#premier").click(function(){
        console.log("11111.....");
  });

  $("#second").click(function(){
	$("#deuxieme_modal").dialog({
		height: 400,
                width: 350,
                modal: true,
                buttons: {
                        "Inscrivez-vous": function(){ console.log("inscrit"); },
                }
	});
  });

  $("#troisieme").click(function(){
	$("#troisieme_modal").dialog({
		height: 400,
		width: 350,
		modal: true,
		buttons: {
			"Connectez-vous": function(){ console.log("Connecté"); },
        	}
       });
  });
});
