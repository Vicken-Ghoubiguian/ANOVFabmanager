CREATE TABLE IF NOT EXISTS ovfabmanager_etat (
	
	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_carte (

	id INT PRIMARY KEY NOT NULL,
	numero_de_carte VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_prestation (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	cout_en_euros INT NOT NULL,
	date_de_livraison DATE NOT NULL,
	fichier VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_type_de_client (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_abonnement (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	prix INT NOT NULL,
	credit_machine INT NOT NULL,
	avantages VARCHAR(800) NOT NULL,
	type_de_client_id INT NOT NULL,
	FOREIGN KEY (type_de_client_id) REFERENCES ovfabmanager_type_de_client(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_type_d_evenement (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_type_machine (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_entreprise (

	id INT PRIMARY KEY NOT NULL,
	nom VARCHAR(50) NOT NULL,
	adresse_postale VARCHAR(50) NOT NULL,
	adresse_email VARCHAR(50) NOT NULL,
	telephone VARCHAR(20) NOT NULL,
	site_web VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS ovfabmanager_espace (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	abonnement_requis_id INT NOT NULL,
	FOREIGN KEY (abonnement_requis_id) REFERENCES ovfabmanager_abonnement(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_evenement (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	heure_de_debut TIME NOT NULL,
	duree INT NOT NULL,
	espace_id INT NOT NULL,
	FOREIGN KEY (espace_id) REFERENCES ovfabmanager_espace(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_qualification (

	id INT PRIMARY KEY NOT NULL,
	intitule VARCHAR(100) NOT NULL,
	nomenclature VARCHAR(50) NOT NULL,
	date_de_creation DATE NOT NULL,
	duree_de_validite INT NOT NULL,
	evenement_id INT NOT NULL,
	FOREIGN KEY (evenement_id) REFERENCES ovfabmanager_evenement(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_machine (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	conditions_d_utilisation VARCHAR(500) NOT NULL,
	fabricant VARCHAR(100) NOT NULL,
	date_d_achat DATE NOT NULL,
	fournisseur VARCHAR(100) NOT NULL,
	prix_d_achat INT NOT NULL,
	modele VARCHAR(100) NOT NULL,
	prestation_id INT NOT NULL,
	type_machine_id INT NOT NULL,
	qualification_requise_id INT NOT NULL,
	FOREIGN KEY (prestation_id) REFERENCES ovfabmanager_prestation(id),
	FOREIGN KEY (type_machine_id) REFERENCES ovfabmanager_type_machine(id),
	FOREIGN KEY (qualification_requise_id) REFERENCES ovfabmanager_qualification(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_outil (

	id INT PRIMARY KEY NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	fiche_technique VARCHAR(500) NOT NULL,
	date_de_peremption DATE NOT NULL,
	fabricant VARCHAR(100) NOT NULL,
	fournisseur VARCHAR(100) NOT NULL,
	machine_id INT NOT NULL,
	FOREIGN KEY (machine_id) REFERENCES ovfabmanager_machine(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_client (

	id INT PRIMARY KEY NOT NULL,
	nom_de_famille VARCHAR(100) NOT NULL,
	prenom VARCHAR(30) NOT NULL,
	telephone VARCHAR(20) NOT NULL,
	adresse_email VARCHAR(50) NOT NULL,
	identifiant VARCHAR(50) NOT NULL,
	mot_de_passe VARCHAR(50) NOT NULL,
	credit_client_en_temps INT NOT NULL,
	abonnement_id INT NOT NULL,
	carte_id INT,
	prestation_id INT NOT NULL,
	type_de_client_id INT NOT NULL,
	FOREIGN KEY (abonnement_id) REFERENCES ovfabmanager_abonnement(id),
	FOREIGN KEY (carte_id) REFERENCES ovfabmanager_carte(id),
	FOREIGN KEY (prestation_id) REFERENCES ovfabmanager_prestation(id),
	FOREIGN KEY (type_de_client_id) REFERENCES ovfabmanager_type_de_client(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_possede (

	id INT PRIMARY KEY NOT NULL,
	date_de_delivrance DATE NOT NULL,
	client_id INT NOT NULL,
	qualification_id INT NOT NULL,
	FOREIGN KEY (client_id) REFERENCES ovfabmanager_client(id),
	FOREIGN KEY (qualification_id) REFERENCES ovfabmanager_qualification(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_panier (

	id INT PRIMARY KEY NOT NULL,
	heure_de_pret TIME NOT NULL,
	heure_de_retour TIME NOT NULL,
	client_id INT NOT NULL,
	FOREIGN KEY (client_id) REFERENCES ovfabmanager_client(id)
);

CREATE TABLE IF NOT EXISTS ovfabmanager_article (

	id INT PRIMARY KEY NOT NULL,
	code_barre VARCHAR(100) NOT NULL,
	libelle VARCHAR(100) NOT NULL,
	date_d_achat DATE NOT NULL,
	date_de_livraison DATE NOT NULL,
	etat_id INT NOT NULL,
	outil_id INT NOT NULL,
	panier_id INT NOT NULL,
	FOREIGN KEY (etat_id) REFERENCES ovfabmanager_etat(id),
	FOREIGN KEY (outil_id) REFERENCES ovfabmanager_outil(id),
	FOREIGN KEY (panier_id) REFERENCES ovfabmanager_panier(id)
);
