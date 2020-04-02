$(document).ready(function(){

  $( document ).tooltip();

  $(".radiobutton_group").controlgroup();

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
				console.log("(" + $("input[name='genre']:checked").val() + ")");
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
		buttons: {
                        "Connectez-vous": function(){
				$.ajax({
					url: "{% url 'calendrier'  %}",
					type: "POST",
					data: { form_name: "connexion_form" },
					success: function(response){ console.log("YESSSS !!!!" + response); },
					error: function(response){ console.log("NNNOOOO !!!!" + response); }
				});

				$("#idt").val("");
				$("#mdp").val("");
				$( this ).dialog( "close" );
			 },
			"Réinitialiser": function(){ $("#idt").val(""); $("#mdp").val(""); },
                }
       });
  });
});
