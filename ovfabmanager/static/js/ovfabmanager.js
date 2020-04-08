$(document).ready(function(){

  $( document ).tooltip();

  $("#personne_morale").click(function(){
	if($("#personne_morale").prop(":checked")){
		$("#personne_morale"). prop(":checked", false);

		$(".personne_moral_field").removeClass("input-container");
		$(".personne_moral_field").addClass("hidden_div");

		$(".personne_morale_input").removeAttr("required");

		$("#personne_morale_adresse_physique").val("");
		$("#personne_morale_nom").val("");

	} else {
		$("#personne_morale"). prop(":checked", true);

		$(".personne_moral_field").removeClass("hidden_div");
                $(".personne_moral_field").addClass("input-container");

		$(".personne_morale_input").attr("required","required");
	}
  });

  $("#autorisation_communication").click(function(){
        if($("#autorisation_communication").prop(":checked")){
                $("#autorisation_communication"). prop(":checked", false);
                alert("Autorisation communication is Unchecked");
        } else {
                $("#autorisation_communication"). prop(":checked", true);
                alert("Autorisation communication is Checked");
        }
  });

  $("#autorisation_informations_depuis_fablab").click(function(){
        if($("#autorisation_informations_depuis_fablab").prop(":checked")){
                $("#autorisation_informations_depuis_fablab"). prop(":checked", false);
                alert("Autorisation informations depuis fablab is Unchecked");
        } else {
                $("#autorisation_informations_depuis_fablab"). prop(":checked", true);
                alert("Autorisation informations depuis fablab is Checked");
        }
  });

  $("#acceptation_des_conditions").click(function(){
        if($("#acceptation_des_conditions").prop(":checked")){
                $("#acceptation_des_conditions"). prop(":checked", false);
                alert("Acceptation des conditions is Unchecked");
        } else {
                $("#acceptation_des_conditions"). prop(":checked", true);
                alert("Acceptation des conditions is Checked");
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
			$("#personne_morale_adresse_physique").val("");
			$("#personne_morale_nom").val("");
		},
                buttons: {
                        "Inscrivez-vous": function(){ console.log("inscrit."); },
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
				$("#personne_morale_adresse_physique").val("");
                        	$("#personne_morale_nom").val("");
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
