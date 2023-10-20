
total_facture = 0
nombre_articles = int(input("Saisir le nombre des articles "))
for i in range(nombre_articles):
    print(f"\nArticle {i + 1}")
    nom_article = input("Nom de l'article : ")
    prix_article = float(input("Prix de l'article : "))
    quantite_article = int(input("Quantité de l'article : "))
    montant_ht = prix_article * quantite_article
    montant_ttc = montant_ht + (montant_ht * 0.2)
    print(f"Montant total de l'article {nom_article}: {montant_ttc} dhs")
    total_facture += montant_ttc
print(f"\nMontant total de la facture : {total_facture} dhs")
