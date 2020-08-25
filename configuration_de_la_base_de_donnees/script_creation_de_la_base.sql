-- CREATION DE L'UTILISATEUR ovfablab_admin --
CREATE USER 'ovfablab_admin'@'localhost' IDENTIFIED BY 'mot_de_passe_de_l_admin_du_fablab';

-- ACCORD DE TOUS LES PRIVILEGES A L'UTILISATEUR ovfablab_admin SUR LA BASE ovfablab_database --
GRANT ALL PRIVILEGES ON ovfablab_database.* TO 'ovfablab_admin'@'localhost';

-- CREATION DE TOUTES LES TABLES DU MODELE --

-- TABLE Type_de_client --
CREATE TABLE IF NOT EXISTS Type_de_client (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	PRIMARY KEY(id)
);

-- TABLE Type_d_evenement --
CREATE TABLE IF NOT EXISTS Type_d_evenement (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	PRIMARY KEY(id)
);

-- TABLE Type_machine --
CREATE TABLE IF NOT EXISTS Type_machine (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	PRIMARY KEY(id)
);

-- TABLE Entreprise --
CREATE TABLE IF NOT EXISTS Entreprise (

	id INTEGER NOT NULL AUTO_INCREMENT,
	nom VARCHAR(50) NOT NULL,
	adresse_postale VARCHAR(50) NOT NULL,
	adresse_email VARCHAR(50) NOT NULL,
	PRIMARY KEY(id)
);

-- TABLE Type_d_outil --
CREATE TABLE IF NOT EXISTS Type_d_outil (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	fabricant INTEGER NOT NULL,
	date_d_achat DATE NOT NULL,
	fournisseur INTEGER NOT NULL,
	date_de_peremption DATE NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (fabricant) REFERENCES Entreprise(id),
	FOREIGN KEY (fournisseur) REFERENCES Entreprise(id)
);

-- TABLE Abonnement --
CREATE TABLE IF NOT EXISTS Abonnement (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	prix INTEGER NOT NULL,
	credit_machine INTEGER NOT NULL,
	avantages VARCHAR(800) NOT NULL,
	type_de_client INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (type_de_client) REFERENCES Type_de_client(id)
);

-- TABLE Espace --
CREATE TABLE IF NOT EXISTS Espace (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	abonnement_requis INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (abonnement_requis) REFERENCES Abonnement(id)
);

-- TABLE Evenement --
CREATE TABLE IF NOT EXISTS Evenement (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	heure_de_debut TIME NOT NULL,
	duree INTEGER NOT NULL,
	espace INTEGER NOT NULL,
	type_d_evenement INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (espace) REFERENCES Espace(id),
	FOREIGN KEY (type_d_evenement) REFERENCES Type_d_evenement(id)
);

-- TABLE Qualification --
CREATE TABLE IF NOT EXISTS Qualification (

	id INTEGER NOT NULL AUTO_INCREMENT,
	Intitule VARCHAR(100) NOT NULL,
	nomenclature VARCHAR(50) NOT NULL,
	date_de_creation DATE NOT NULL,
	duree_de_validite INTEGER NOT NULL,
	evenement INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (evenement) REFERENCES Evenement(id)
);

-- TABLE Prestation --
CREATE TABLE IF NOT EXISTS Prestation (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	descriptif VARCHAR(500) NOT NULL,
	cout_en_euros INTEGER NOT NULL,
	date_de_livraison DATE NOT NULL,
	fichier VARCHAR(100) NOT NULL,
	PRIMARY KEY(id)
);

-- TABLE Machine --
CREATE TABLE IF NOT EXISTS Machine (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	conditions_d_utilisation VARCHAR(500) NOT NULL,
	fabricant VARCHAR(100) NOT NULL,
	date_d_achat DATE NOT NULL,
	fournisseur VARCHAR(100) NOT NULL,
	prix_d_achat INTEGER NOT NULL,
	modele VARCHAR(100) NOT NULL,
	qualification_requise INTEGER NOT NULL,
	type_machine INTEGER NOT NULL,
	prestation INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (qualification_requise) REFERENCES Qualification(id),
	FOREIGN KEY (type_machine) REFERENCES Type_machine(id),
	FOREIGN KEY (prestation) REFERENCES Prestation(id)
);

-- TABLE Client --
CREATE TABLE IF NOT EXISTS Client (

	id INTEGER NOT NULL AUTO_INCREMENT,
	nom_de_famille VARCHAR(100) NOT NULL,
	prenom VARCHAR(30) NOT NULL,
	telephone VARCHAR(20) NOT NULL,
	adresse_email VARCHAR(50) NOT NULL,
	identifiant VARCHAR(50) NOT NULL,
	mot_de_passe VARCHAR(50) NOT NULL,
	credit_client_en_temps INTEGER NOT NULL,
	type_de_client INTEGER NOT NULL,
	abonnement INTEGER NOT NULL,
	prestation INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (type_de_client) REFERENCES Type_de_client(id),
	FOREIGN KEY (abonnement) REFERENCES Abonnement(id),
	FOREIGN KEY (prestation) REFERENCES Prestation(id)
);

-- TABLE  Panier --
CREATE TABLE IF NOT EXISTS Panier (

	id INTEGER NOT NULL AUTO_INCREMENT,
	heure_de_pret TIME NOT NULL,
	heure_de_retour TIME NOT NULL,
	client INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (client) REFERENCES Client(id)
);

-- TABLE Outil --
CREATE TABLE IF NOT EXISTS Outil (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	description VARCHAR(500) NOT NULL,
	fiche_technique VARCHAR(500) NOT NULL,
	machine INTEGER NOT NULL,
	Type_d_outil INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (machine) REFERENCES Machine(id),
        FOREIGN KEY (type_d_outil) REFERENCES Type_d_outil(id)
);

-- TABLE Article --
CREATE TABLE IF NOT EXISTS Article (

	id INTEGER NOT NULL AUTO_INCREMENT,
	libelle VARCHAR(100) NOT NULL,
	outil INTEGER NOT NULL,
	panier INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (outil) REFERENCES Outil(id),
	FOREIGN KEY (panier) REFERENCES Panier(id)
);

-- TABLE Possede --
CREATE TABLE IF NOT EXISTS Possede (

	client INTEGER NOT NULL,
	qualification INTEGER NOT NULL,
	date_de_delivrance DATE NOT NULL,
	FOREIGN KEY (client) REFERENCES Client(id),
	FOREIGN KEY (qualification) REFERENCES Qualification(id)
);
