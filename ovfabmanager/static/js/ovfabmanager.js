$(document).ready(function(){
  $( document ).tooltip();

  $("#premier").click(function(){
        console.log("11111.....");
  });

  $("#second").click(function(){
	$("#deuxieme_modal").dialog({
		height: 800,
		resizable: false,
                width: 650,
		resizable: false,
                modal: true,
                buttons: {
                        "Inscrivez-vous": function(){ console.log("inscrit"); },
			"Réinitialiser": function(){ console.log("réinitialisé"); },
                }
	});
  });

  $("#troisieme").click(function(){
	$("#troisieme_modal").dialog({
		height: 250,
		width: 420,
		resizable: false,
		modal: true,
		buttons: {
			"Connectez-vous": function(){ console.log("Connecté"); },
			"Réinitialiser": function(){
                                document.getElementById("identifiant").value = "";
                                document.getElementById("mot_de_passe").value = "";
                         },
        	}
       });
  });
});
