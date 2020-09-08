from django.db import models

class Type_de_client(models.Model):
	libelle = models.CharField(max_length=100)
	descriptif = models.CharField(max_length=500)

class Carte(models.Model):
	numero_de_carte = models.CharField(max_length=50)

class Type_d_evenement(models.Model):
	libelle = models.CharField(max_length=100)
	descriptif = models.CharField(max_length=500)

class Type_machine(models.Model):
	libelle = models.CharField(max_length=100)
	descriptif = models.CharField(max_length=500)

class Etat(models.Model):
	libelle = models.CharField(max_length=50)

class Entreprise(models.Model):
	nom = models.CharField(max_length=50)
	adresse_postale = models.CharField(blank=True, null=True, max_length=50)
	adresse_email = models.CharField(blank=True, null=True, max_length=50)
	telephone = models.CharField(blank=True, null=True, max_length=20)
	site_web = models.CharField(blank=True, null=True, max_length=100)

class Abonnement(models.Model):
	libelle = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	prix = models.IntegerField()
	credit_machine = models.IntegerField()
	avantages = models.CharField(max_length=800)
	type_de_client = models.ForeignKey(Type_de_client, on_delete=models.CASCADE)

class Espace(models.Model):
	libelle = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	abonnement_requis = models.ForeignKey(Abonnement, on_delete=models.CASCADE)

class Evenement(models.Model):
	libelle = models.CharField(max_length=100)
	descriptif = models.CharField(max_length=500)
	heure_de_debut = models.TimeField()
	duree = models.IntegerField()
	espace = models.ForeignKey(Espace, on_delete=models.CASCADE)
	type_d_evenement = models.ForeignKey(Type_d_evenement, on_delete=models.CASCADE)

class Qualification(models.Model):
	intitule = models.CharField(max_length=100)
	nomenclature = models.CharField(max_length=50)
	date_de_creation = models.DateField()
	duree_de_validite = models.IntegerField()
	evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)

class Prestation(models.Model):
	libelle = models.CharField(max_length=100)
	descriptif = models.CharField(max_length=500)
	cout_en_euros = models.IntegerField()
	date_de_livraison = models.DateField()
	fichier = models.CharField(max_length=100)

class Machine(models.Model):
	libelle = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	conditions_d_utilisation = models.CharField(max_length=500)
	fabricant = models.CharField(max_length=100)
	date_d_achat = models.DateField()
	fournisseur = models.CharField(max_length=100)
	prix_d_achat = models.IntegerField()
	modele = models.CharField(max_length=100)
	qualification_requise = models.ForeignKey(Qualification, on_delete=models.CASCADE)
	type_machine = models.ForeignKey(Type_machine, on_delete=models.CASCADE)
	prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)

class Client(models.Model):
	nom_de_famille = models.CharField(max_length=100)
	prenom = models.CharField(max_length=30)
	telephone = models.CharField(max_length=20)
	adresse_email = models.CharField(max_length=50)
	identifiant = models.CharField(max_length=50)
	mot_de_passe = models.CharField(max_length=50)
	credit_client_en_temps = models.IntegerField()
	carte = models.ForeignKey(Carte, blank=True, null=True, on_delete=models.CASCADE)
	type_de_client = models.ForeignKey(Type_de_client, blank=True, null=True, on_delete=models.CASCADE)
	abonnement = models.ForeignKey(Abonnement, blank=True, null=True, on_delete=models.CASCADE)
	prestation = models.ForeignKey(Prestation, blank=True, null=True, on_delete=models.CASCADE)

class Panier(models.Model):
	heure_de_pret = models.TimeField()
	heure_de_retour = models.TimeField()
	client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Outil(models.Model):
	libelle = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	fiche_technique = models.CharField(blank=True, null=True, max_length=500)
	machine = models.ForeignKey(Machine, blank=True, null=True, on_delete=models.CASCADE)
	date_de_peremption = models.DateField(blank=True, null=True)
	fabricant = models.CharField(max_length=100)
	fournisseur = models.CharField(max_length=100)

class Article(models.Model):
	code_barre = models.CharField(max_length=100)
	libelle = models.CharField(max_length=100)
	date_d_achat = models.DateField(blank=True, null=True)
	date_de_livraison = models.DateField(blank=True, null=True)
	outil = models.ForeignKey(Outil, on_delete=models.CASCADE)
	panier = models.ForeignKey(Panier, blank=True, null=True, on_delete=models.CASCADE)
	etat = models.ForeignKey(Etat, blank=True, null=True, on_delete=models.CASCADE)

class Possede(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
	date_de_delivrance = models.DateField()
