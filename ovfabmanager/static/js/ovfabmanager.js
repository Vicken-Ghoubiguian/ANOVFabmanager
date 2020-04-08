$(document).ready(function(){

  $( document ).tooltip();

  $("#personne_morale").click(function(){
	if($("#personne_morale").prop(":checked")){
		$("#personne_morale"). prop(":checked", false);
		alert("Check box in Unchecked");
	} else {
		$("#personne_morale"). prop(":checked", true);
		alert("Check box is Checked");
	}
  });

  $(".customized_checkbox").checkboxradio();

  $(".common").click(function(){ document.location.href = "http://127.0.0.1:8000/"; });

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
		show: {
			effect: "size",
			duration: 1000
		},
		hide: {
			effect: "size",
			duration: 1000
		},
		close: function(event, ui){
			$("#nom").val("");
			$("#prenom").val("");
			$("#iscidt").val("");
			$("#adresse_email").val("");
			$("#mot_de_passe").val("");
			$("#resaisir_mot_de_passe").val("");
			$("#naissance").val("");
			$("#telephone").val("");
		},
                buttons: {
                        "Inscrivez-vous": function(){ console.log("inscrit"); },
			"Réinitialiser": function()
			{
				$("#nom").val("");
				$("#prenom").val("");
				$("#iscidt").val("");
				$("#adresse_email").val("");
				$("#mot_de_passe").val("");
				$("#resaisir_mot_de_passe").val("");
				$("#naissance").val("");
				$("#telephone").val("");
			},
                }
	});
  });

  $("#troisieme").click(function(){
	$("#troisieme_modal").dialog({
		height: 250,
		width: 420,
		resizable: false,
		modal: true,
		show: {
			effect: "size",
			duration: 1000
		},
		hide: {
			effect: "size",
			duration: 1000
		},
		close: function(event, ui){ $("#idt").val(""); $("#mdp").val(""); },
		buttons: {
                        "Connectez-vous": function(){ $("#connexion_form").submit(); },
			"Réinitialiser": function(){ $("#idt").val(""); $("#mdp").val(""); },
                }
       });
  });
});
