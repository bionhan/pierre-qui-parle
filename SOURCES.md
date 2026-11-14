# Sources, références et points à valider

## Données et services tiers

| Source | Usage | Licence / conditions |
|---|---|---|
| BRGM — carte lithologique simplifiée et carte géologique au 1/1 000 000 (services WFS) | Roche, âge et contexte au point choisi | © BRGM |
| BRGM — BD Charm-50 (édition 2019), cartes géologiques harmonisées au 1/50 000 | Dossier `geol50k/` : géométries simplifiées (tolérance 20 m) et légendes | Licence Ouverte (Etalab) — source : BRGM |
| IGN — Plan IGN v2 (Géoplateforme) | Fond de carte | © IGN |
| GPlates Web Service, modèle de Merdith et al. (2021) | Carte du monde à l'époque de la roche | CC BY 4.0 |
| Wikimedia Commons | Photos des roches (chaque photo renvoie à sa page : auteur et licence) | Licences libres, variables selon la photo |
| Leaflet 1.9.4 | Affichage de la carte | BSD 2-Clause |

Les fichiers de `geol50k/` sont une œuvre dérivée de la BD Charm-50 : ils restent sous Licence Ouverte, avec mention de la source BRGM.

## Références scientifiques

- **Streckeisen** : Streckeisen A. (1976), *Earth-Science Reviews* 12 — classification QAPF de l'IUGS.
- **TAS** : Le Bas M.J. et al. (1986), *Journal of Petrology* 27 ; limite alcalin / subalcalin d'après Irvine et Baragar (1971).
- **AFM** : Irvine T.N. et Baragar W.R.A. (1971), *Canadian Journal of Earth Sciences* 8.
- **Fusion de la péridotite** : Katz R.F., Spiegelman M. et Langmuir C.H. (2003), *Geochemistry, Geophysics, Geosystems* 4 — solidus et liquidus secs.
- **Silicates d'alumine** : Holdaway M.J. (1971), *American Journal of Science* 271.
- **Hjulström** : Hjulström F. (1935), *Bulletin of the Geological Institution of the University of Upsala* 25.
- **Forme et tri des grains** : Powers M.C. (1953), *Journal of Sedimentary Petrology* 23 ; Folk R.L. (1951) et Folk R.L. et Ward W.C. (1957) ; morphoscopie de Cailleux.
- **Dunham** : Dunham R.J. (1962), *AAPG Memoir* 1 ; Embry A.F. et Klovan J.E. (1971).
- **QFL** : Dickinson W.R. et al. (1983), *GSA Bulletin* 94.
- **Paléogéographie** : Merdith A.S. et al. (2021), *Earth-Science Reviews* 214.

La **clé de détermination** repose sur les critères classiques de la pétrographie macroscopique (structure, texture, minéraux visibles, dureté, réaction à l'acide). Sa formulation et ses illustrations schématiques sont propres à l'application.

## Points à valider

Ces éléments sont schématiques, simplifiés ou saisis de mémoire. Ils sont à vérifier en priorité.

**Partie 1 — Les roches selon un lieu**
- Table des étages (`STAGES`), dont les noms régionaux et anciens, et leurs âges en Ma.
- Lecture automatique des légendes de la BD Charm-50 : l'âge est reconnu pour environ 69 % des polygones, la roche pour environ 89 %.
- Textes décrivant le milieu de formation de chaque roche.
- Carte du monde : tables des chaînes de montagnes (`OROGENS`), des continents (`LANDS`) et des océans (`SEAS`) avec leurs périodes ; les continents sont dessinés avec leurs contours actuels.

**Partie 3 — Les roches dans un diagramme**
- Pression – température : limites de faciès schématiques ; conditions associées aux minéraux repères (ordres de grandeur).
- QFL : coordonnées des champs de Dickinson saisies de mémoire.
- AFM : points de la limite d'Irvine et Baragar saisis de mémoire ; compositions types arrondies.
- Hjulström : courbes redessinées à partir d'une douzaine de points de contrôle.
- Géotherme et solidus : solidus hydraté schématique ; géotherme très simplifié ; taux de fusion non calculé.
- Diagramme ternaire de phases : schématique (champ du spinelle omis).
- Forme et tri des grains : le découpage en milieux de dépôt est une interprétation, pas une référence publiée.
- Dunham : textes d'interprétation des milieux.
