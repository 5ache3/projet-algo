#set page(paper: "a4", margin: 1in)
#set text(font: "New Computer Modern", size: 11pt, lang: "fr")

 

#align(center, {
  text("Comparaison des Algorithmes de Tri",size: 17pt,weight: 700)
})
\

#v(1em)
#line(length: 100%)
#v(3em)

Analyse comparative entre le *Tri par Sélection* (utilisé dans la classe `File`) et le *Tri Fusion* (utilisé dans la classe `Pile`).

= 1. Complexité Temporelle (Time Complexity)

== Tri par Sélection (Selection Sort)
Le tri par sélection parcourt la liste non triée à chaque itération pour trouver l'élément minimum (ou maximum) et le mettre à sa position finale.

- *Complexité*: *$O(n^2)$* .

- *Explication*: Pour une liste de taille *$n$*, il effectue *$n$* itérations. À chaque itération *$i$*, il fait *$n - 1 - i$* comparaisons.
 le nombre des iteration devient exprime par la somme:
$
  sum_(i=0)^(n-1) (n - 1 - i) $ $ = 
  sum_(i=0)^(n-1) (n - 1) - sum_(i=0)^(n-1) i $ $ = 
  (n - 1)n - n(n - 1)/2  $ $ =
  n(n - 1)/2  $ $ =
  (1/2)n^2 - (1/2)n
$
Ce qui donne une complexité de l'ordre de *$O(n^2)$*

== Tri Fusion (Merge Sort)
Le tri fusion est un algorithme "Diviser pour Régner" qui divise la liste en deux moitiés récursivement 
jusqu'à ce que chaque sous-liste ne contienne qu'un seul élément, puis fusionne les moitiés triées.


- *Complexité*: *$O(n log n)$*
- *Explication*: La division de la liste prend un temps logarithmique (*$log n$* niveaux de récursion), et la fusion des sous-listes prend un temps linéaire (*$n$*) à chaque niveau car en chaque niveau, tous les éléments doivent être comparés et fusionnés.

#pagebreak()
= 2. Complexité Spatiale (Space Complexity)


== Tri par Sélection
- *Complexité*: $O(1)$
- *Explication*: Cet algorithme n'utilise qu'un nombre constant d'espaces supplémentaires pour les variables temporaires, indépendamment de la taille de la liste à trier.

== Tri Fusion
- *Complexité*: $O(n)$
- *Explication*: L'étape de fusion nécessite de créer des petites tableaux temporaires pour stocker les éléments triés avant de les recopier dans le tableau original.

= 3. Tableau de Comparaison

#figure(
  table(
    columns: (auto, auto, auto),
    inset: 10pt,
    align: horizon,
    [], [*Tri par Sélection*], [*Tri Fusion*],
    [Complexité Temporelle], [$O(n^2)$], [$O(n log n)$],
    [Complexité Spatiale], [$O(1)$], [$O(n)$],
    [Efficacité sur grandes listes], [Faible], [Élevée],
  ),
  caption: [Comparaison Selection Sort vs Merge Sort]
)

= 4. Comparaison Pratique
#figure(
  image("image.jpeg", width: 400pt),
  caption: [Performance des Algorithmes de Tri en Fonction de la Taille des Données]
)