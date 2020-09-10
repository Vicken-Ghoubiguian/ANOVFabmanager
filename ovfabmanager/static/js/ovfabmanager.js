$(document).ready(function(){

  $( document ).tooltip();

  $(".bouton_au_pied").button();

  $("input[type=submit]").button();

  $("input[type=reset]").button();

  $("#enregistrement_creation_panier_validation").click(function(){

	var verif_var = true;

	$(":input.required-field-enregistrement-panier").css("border-color","#ccc");

	$(":input.required-field-enregistrement-panier").each(function(){

		var input_value = $(this).val();
		var field_name = "";

		if(document.getElementById("client_pret").selectedIndex === 0)
		{

			$("#client_pret").css("border-color", "#f8009b");

			$("#inside_pret_enregistrement_error").text("Erreur: veuillez sélectionner le client");

			$("#pret_enregistrement_error").removeClass("hidden_div");

			verif_var = false;

			return false;
		}

		if(input_value === "")
                {

                        $(this).css("border-color", "#f8009b");
                        $(this).css("::placeholder", "#f8009b");

                        field_name = $(this).attr("placeholder");

						field_name = field_name.charAt(0).toLowerCase() + field_name.slice(1);

						$("#inside_pret_enregistrement_error").text("Erreur: " + field_name.slice(0,-1) + " invalide");

                        $("#pret_enregistrement_error").removeClass("hidden_div");

                        verif_var = false;

                        return false;
                }
	});

	if(verif_var)
        {
                $("#pret_enregistrement_error").addClass("hidden_div");

                $(":input.required-field-enregistrement-panier").css("border-color","#ccc");

                $("#formulaire_enregistrement_paniers").submit();
        }
  });

  $("#enregistrement_retour_panier_validation").click(function(){

	var verif_var = true;

	$(":input.required-field-retour-panier").css("border-color","#ccc");

        $(":input.required-field-retour-panier").each(function(){

                var input_value = $(this).val();
                var field_name = "";

                if(input_value === "")
                {

                        $(this).css("border-color", "#f8009b");
                        $(this).css("::placeholder", "#f8009b");

                        field_name = $(this).attr("placeholder");

						field_name = field_name.charAt(0).toLowerCase() + field_name.slice(1);

						$("#inside_retour_pret_error").text("Erreur: " + field_name.slice(0,-1) + " invalide");

                        $("#retour_pret_error").removeClass("hidden_div");

                        verif_var = false;

                        return false;
                }
        });

        if(verif_var)
        {
                $("#retour_pret_error").addClass("hidden_div");

                $(":input.required-field-retour-panier").css("border-color","#ccc");

                $("#formulaire_de_retour_panier").submit();
        }
  });

  $("#reinitialisation_creation_panier").click(function(){

	$("#pret_enregistrement_error").addClass("hidden_div");

	$(":input.required-field-enregistrement-panier").css("border-color","#ccc");

	$("#client_pret").css("border-color","#ccc");

	document.getElementById("client_pret").selectedIndex = 0

	$("#date_de_retour_du_pret").val("");

        $("#liste_des_articles_a_preter").val("");
  });

  $("#reinitialisation_retour_panier").click(function(){

	$("#retour_pret_error").addClass("hidden_div");

	$(":input.required-field-retour-panier").css("border-color","#ccc");

	$("#client_retour").val(0);

	$("#liste_des_articles_a_retourner").val("");
  });

  $("#enregistrement_produit_validation").click(function(){

	var verif_var_1 = true;
	var verif_var_2 = true;

	$(":input.required-field-enregistrement_produit").each(function(){

		$(this).css("border-color", "#CCCCCC");
		$(this).css("::placeholder", "#CCCCCC");

	});

	$(":input.required-field-enregistrement_produit").each(function(){

		var input_value = $(this).val();
		var field_name = "";

		if(input_value === "")
		{

			$(this).css("border-color", "#f8009b");
			$(this).css("::placeholder", "#f8009b");

			field_name = $(this).attr("placeholder");

			field_name = field_name.charAt(0).toLowerCase() + field_name.slice(1);

			$("#inside_product_error_div").text("Erreur: " + field_name.slice(0,-1) + " invalide");

			$("#product_error_div").removeClass("hidden_div");

			verif_var_1 = false;

			return false;
		}
	});

	if(verif_var_1)
	{
		if(document.getElementById("nouveau_produit").checked === false && document.getElementById("type_d_objet").value === "")
		{

			$("#type_d_objet").css("border-color", "#f8009b");
			$("#type_d_objet").css("::placeholder", "#f8009b");

			field_name = $("#type_d_objet").attr("placeholder");

			field_name = field_name.charAt(0).toLowerCase() + field_name.slice(1);

			$("#inside_product_error_div").text("Erreur: " + field_name.slice(0,-1) + " invalide");

			$("#product_error_div").removeClass("hidden_div");

			verif_var_2 = false;

			return false;
		}

		if(verif_var_2)
		{
			$("#product_error_div").addClass("hidden_div");

			$(":input.required-field-enregistrement_produit").css("border-color","#ccc");

			$("#formulaire_enregistrement_stock").submit();
		}
	}
  });

  $("#reinitialisation_enregistrement_produit").click(function(){

	$("#product_error_div").addClass("hidden_div");

	$(":input.required-field-enregistrement_produit").css("border-color","#ccc");

	$("#codebarre").val("");

	$("#date_d_achat").val("");

	$("#date_de_livraison").val("");

	$("#type_d_objet").val(0);

	document.getElementById("nouveau_produit").checked = false;

	$("#outil").val("");

	$("#description_outil").val("");

	$("#fabricant").val("");

        $("#adresse_email_fabricant").val("");

        $("#adresse_postale_fabricant").val("");

        $("#numero_telephone_fabricant").val("");

        $("#site_web_fabricant").val("");

	$("#fournisseur").val("");

	$("#adresse_email_fournisseur").val("");

	$("#adresse_postale_fournisseur").val("");

	$("#numero_telephone_fournisseur").val("");

	$("#site_web_fournisseur").val("");
  });

  $("#nouveau_produit").change(function(){

	if(document.getElementById("nouveau_produit").checked == true)
	{

		$("#outil").addClass("required-field-enregistrement_produit");

		$("#description_outil").addClass("required-field-enregistrement_produit");

		$("#fabricant").addClass("required-field-enregistrement_produit");

                $("#fournisseur").addClass("required-field-enregistrement_produit");

		$("#type_d_objet").removeClass("required-field-enregistrement_produit");

		$("#type_d_objet").addClass("disabled_element");

		$("#icone_type_d_objet").addClass("disabled_element");

		document.getElementById("type_d_objet").disabled = true;

		$("#enregistrer_nouveau_produit").fadeIn("slow");
	}
	else
	{

		$("#outil").removeClass("required-field-enregistrement_produit");

		$("#description_outil").removeClass("required-field-enregistrement_produit");

		$("#fabricant").removeClass("required-field-enregistrement_produit");

		$("#fournisseur").removeClass("required-field-enregistrement_produit");

		$("#type_d_objet").addClass("required-field-enregistrement_produit");

		$("#type_d_objet").removeClass("disabled_element");

		$("#icone_type_d_objet").removeClass("disabled_element");

		document.getElementById("type_d_objet").disabled = false;

		$("#enregistrer_nouveau_produit").fadeOut("slow");
	}
  });

  $(".asDatatable").DataTable({
	"language": {
		"url": "//cdn.datatables.net/plug-ins/1.10.21/i18n/French.json"
	}
  });

  $.datepicker.regional['fr'] = {
		
		prevText: '&#x3c;Préc',
		
		nextText: 'Suiv&#x3e;',
		
		monthNames: ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre'],
		
		monthNamesShort: ['Jan','Fev','Mar','Avr','Mai','Jun','Jul','Aou','Sep','Oct','Nov','Dec'],
		
		dayNames: ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'],
		
		dayNamesShort: ['Dim','Lun','Mar','Mer','Jeu','Ven','Sam'],
		
		dayNamesMin: ['Di','Lu','Ma','Me','Je','Ve','Sa'],
		
		weekHeader: 'Sm',
		
		dateFormat: 'dd/mm/yy',
		
		firstDay: 1,
		
		isRTL: false,
		
		showMonthAfterYear: false,
		
		yearSuffix: '',
		
		numberOfMonths: 1,
		
		showButtonPanel: false
  };
  
  $.datepicker.setDefaults($.datepicker.regional['fr']);

  $(".datepicker_amical").datepicker( $.datepicker.regional["fr"] );

  $(".jqTabs").tabs({show: {effect: "clip", duration: "slow"}});

  $(":input.required-field-enregistrement_produit").focus(function(){

	$(this).css("border-color", "#c5007b");

  });

  $(":input.required-field-enregistrement_produit").focusout(function(){

	$(this).css("border-color", "#ccc");

  });

  $(":input.required-field-connexion").focus(function(){

	$(this).css("border-color", "#c5007b");

  });

  $(":input.required-field-connexion").focusout(function(){

	$(this).css("border-color", "#ccc");

  });

  $(":input.required-field-inscription").focus(function(){

	$(this).css("border-color", "#c5007b");

  });

  $(":input.required-field-inscription").focusout(function(){

	$(this).css("border-color", "#ccc");

  });

  function activerPersonneMorale(commande){

	if(commande == true)
	{

		$("#personne_morale_nom").addClass("required-field-inscription");

		$("#enregistrer_personne_morale").fadeIn("slow");
	}
	else
	{

		$("#personne_morale_nom").removeClass("required-field-inscription");

		$("#enregistrer_personne_morale").fadeOut("slow");
	}
  }

  $("#personne_morale").change(function(){

	if(document.getElementById("personne_morale").checked == true)
	{
		activerPersonneMorale(true);
	}
	else
	{
		activerPersonneMorale(false);
	}
  });

  $("#autorisation_communication").click(function(){

        if($("#autorisation_communication").prop(":checked")){

                $("#autorisation_communication"). prop(":checked", false);

        } else {

                $("#autorisation_communication"). prop(":checked", true);

        }
  });

  $("#autorisation_informations_depuis_fablab").click(function(){

        if($("#autorisation_informations_depuis_fablab").prop(":checked")){

                $("#autorisation_informations_depuis_fablab"). prop(":checked", false);

        } else {

                $("#autorisation_informations_depuis_fablab"). prop(":checked", true);

        }
  });

  $("#acceptation_des_conditions").click(function(){

        if($("#acceptation_des_conditions").prop(":checked")){

                $("#acceptation_des_conditions"). prop(":checked", false);

        } else {

                $("#acceptation_des_conditions"). prop(":checked", true);

        }
  });

  $(".common").click(function(){ document.location.href = "http://127.0.0.1:8000/"; });

  $("#client_pret_carte").click(function(){
	$("#identification_client_par_carte").dialog({
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
                        $("#client_card").val("");
                },
                buttons: {
                        "Valider": function()
			{

				$("#client_pret").val($("#client_card").val());

				$(this).dialog("close");
			},
                        "Réinitialiser": function()
                        {
                                $("#client_card").val("");
                        },
                }
        });
  });

  $("#client_retour_carte").click(function(){
	$("#identification_client_par_carte").dialog({
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
			$("#client_card").val("");
		},
		buttons: {
			"Valider": function()
			{
				$("#client_retour").val($("#client_card").val());

				$(this).dialog("close");
			},
			"Réinitialiser": function()
			{
				$("#client_card").val("");
			},
		}
	});
  });

  $("#code_barre_de_l_article_pour_emprunt").click(function(){
        $("#identification_code_barre_article").dialog({
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
                        $("#code_barre_de_l_article").val("");
                },
                buttons: {
                        "Valider": function()
                        {
				console.log(allSerializedArticles);

                                $(this).dialog("close");
                        },
                        "Réinitialiser": function()
                        {
                                $("#code_barre_de_l_article").val("");
                        },
                }
        });
  });

  $("#code_barre_de_l_article_pour_retour").click(function(){
        $("#identification_code_barre_article").dialog({
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
                        $("#code_barre_de_l_article").val("");
                },
                buttons: {
                        "Valider": function()
                        {
                                console.log(allSerializedArticles);

                                $(this).dialog("close");
                        },
                        "Réinitialiser": function()
                        {
                                $("#code_barre_de_l_article").val("");
                        },
                }
        });
  });

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
		close: function(event, ui)
		{
			$("#nom").val("");
			$("#prenom").val("");
			$("#iscidt").val("");
			$("#adresse_email").val("");
			$("#mot_de_passe").val("");
			$("#resaisir_mot_de_passe").val("");
			$("#naissance").val("");
			$("#telephone").val("");

                        $("#personne_morale_nom").val("");

			//document.getElementById("abonnement").selectedIndex = 0;

			document.getElementById("personne_morale").checked = false
			activerPersonneMorale(false)

			document.getElementById("autorisation_communication").checked = false
			document.getElementById("autorisation_informations_depuis_fablab").checked = false
			document.getElementById("acceptation_des_conditions").checked = false

			$(":input.required-field-inscription").css("border-color", "#ccc");

			$("#inscription_error_div").addClass("hidden_div");
		},
                buttons: {
                        "Inscrivez-vous": function()
			{
				var verif_var = true;
				var field_name = "";

				$(":input.required-field-inscription").each(function(){

					var input_value = $(this).val();
					var field_name = "";

					//Si le champ est vide...
					if(input_value === "")
					{
						$(this).css("border-color", "#f8009b");
						$(this).css("::placeholder", "#f8009b");

						field_name = $(this).attr("placeholder");

						field_name = field_name.charAt(0).toLowerCase() + field_name.slice(1);

                        $("#inside_inscription_error_div").text("Erreur: " + field_name.slice(0,-1) + " invalide");

						$("#inscription_error_div").removeClass("hidden_div");

						verif_var = false;

						return false;
					}
				});

				if($("#mot_de_passe").val() != $("#resaisir_mot_de_passe").val())
				{
					$("#inside_inscription_error_div").text("Erreur: votre mot de passe et votre ressaisie ne correspondent pas");

					$("#inscription_error_div").removeClass("hidden_div");

					return false;
				}

				/*if(document.getElementById("abonnement").selectedIndex === 0)
				{
					$("#abonnement").css("border-color", "#f8009b");
					$("#abonnement").css("::placeholder", "#f8009b");

					$("#inside_inscription_error_div").text("Erreur: veuillez sélectionner un abonnement");

					$("#inscription_error_div").removeClass("hidden_div");

					return false;
				}*/

				if(verif_var && document.getElementById("acceptation_des_conditions").checked == false)
				{
					$("#inside_inscription_error_div").text("Erreur: veuillez accepter les conditions d'utilisation");

					$("#inscription_error_div").removeClass("hidden_div");

					verif_var = false;

					return false;
				}

				if(verif_var)
				{

					$("#inscription_form").submit();
				}
			},
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
                        	$("#personne_morale_nom").val("");

				//document.getElementById("abonnement").selectedIndex = 0;

				document.getElementById("autorisation_communication").checked = false;
				document.getElementById("autorisation_informations_depuis_fablab").checked = false;
				document.getElementById("acceptation_des_conditions").checked = false;

				$(":input.required-field-inscription").css("border-color", "#ccc");

				$("#inscription_error_div").addClass("hidden_div");
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
		close: function(event, ui)
		{
			$("#idt").val("");
			$("#mdp").val("");

			$(":input.required-field-connexion").css("border-color", "#ccc");

			$("#connexion_error_div").addClass("hidden_div");
		},
		buttons: {
                        "Connectez-vous": function()
			{
				var verif_var = true;

				$(":input.required-field-connexion").each(function(){
					var input_value = $(this).val();
					var field_name = "";

					//Si le champs est vide....
					if(input_value === "")
                    {
                        $(this).css("border-color", "#f8009b");
                        $(this).css("::placeholder", "#f8009b");

                       	var field_name = $(this).attr("placeholder");

                       	field_name = field_name.charAt(0).toLowerCase() + field_name.slice(1);

                        $("#inside_connexion_error_div").text("Erreur: " + field_name.slice(0,-1) + " invalide")

						$("#connexion_error_div").removeClass("hidden_div");

						verif_var = false;

						return false;
                    }
				});

				if(verif_var)
				{
					$("#connexion_form").submit();
				}
			},
			"Réinitialiser": function()
			{
				$("#idt").val("");
				$("#mdp").val("");

				$(":input.required-field-connexion").css("border-color", "#ccc");

				$("#connexion_error_div").addClass("hidden_div");
			},
                }
       });
  });
});
