# Questions aux experts — Pierre qui parle

Ce document rassemble les choix scientifiques faits dans l'application qui méritent l'avis d'un géologue : valeurs saisies de mémoire, tracés schématiques, rattachements discutables, textes d'interprétation.

**Comment l'utiliser**

- Chaque question porte un identifiant (`LIEU-03`, `DIAG-TAS-02`…) pour pouvoir y renvoyer dans un courriel ou un ticket GitHub.
- La case `[ ]` devient `[x]` quand la question est tranchée ; la réponse se note sous « Réponse ».
- Les nouvelles questions s'ajoutent dans la bonne section, et une ligne dans le **journal** en fin de document.
- Priorité : 🔴 risque d'erreur visible par tous les utilisateurs · 🟠 approximation assumée à confirmer · ⚪ question de vocabulaire ou de présentation.

---

## 1. Les roches selon un lieu

### 1.1 Âges lus dans les légendes de la carte au 1/50 000

- [ ] **LIEU-01** 🔴 — **Table des étages et des périodes**
  - *Ce que fait l'application* : elle cherche dans le texte des légendes du BRGM des noms d'étages ou de périodes et leur attribue des bornes en millions d'années (charte internationale ICS 2023 pour les étages officiels).
  - *Question* : les bornes des étages officiels sont-elles correctes ? Faut-il une autre référence que l'ICS 2023 ?
  - *Réponse* :

- [ ] **LIEU-02** 🔴 — **Étages anciens ou régionaux, bornes approchées**
  - *Ce que fait l'application* : bornes choisies de mémoire pour des termes hors charte officielle :

    | Terme | Bornes retenues (Ma) | | Terme | Bornes retenues (Ma) |
    |---|---|---|---|---|
    | Villafranchien | 3,5 – 1,0 | | Urgonien | 126 – 113 |
    | Vindobonien | 16 – 7,2 | | Bédoulien / Gargasien / Clansayésien | 121,4 – 118 / 118 – 115 / 115 – 113 |
    | Helvétien | 16 – 11,6 | | Purbeckien | 145 – 139,8 |
    | Sannoisien | 33,9 – 32 | | Séquanien / Rauracien / Argovien | 157 – 152 / 159 – 157 / 161,5 – 157 |
    | Ludien, Auversien, Marinésien | 37,7 – 33,9 / 41,2 – 37,7 | | Lotharingien | 196 – 192,9 |
    | Ilerdien, Cuisien, Sparnacien | 56 – 52 / 52 – 47,8 / 56 – 54 | | Briovérien | 650 – 540 |
    | Vitrollien, Rognacien | 66 – 59 / 72,1 – 66 | | Cadomien | 620 – 540 |
    | Bégudien, Fuvélien | 83,6 – 72,1 | | Icartien | 2 100 – 1 800 |
    | Garumnien | 72,1 – 56 | | Varisque, hercynien | 380 – 290 |
    | Würm, Riss, Mindel | 0,115 – 0,012 / 0,3 – 0,13 / 0,48 – 0,42 | | Tardiglaciaire | 0,018 – 0,012 |

  - *Question* : ces bornes sont-elles acceptables ? Y a-t-il des termes fréquents sur les cartes françaises qui manquent ?
  - *Réponse* :

- [ ] **LIEU-03** 🔴 — **Subdivisions « inférieur / moyen / supérieur »**
  - *Ce que fait l'application* : depuis le 22 novembre 2026, « Pliocène supérieur », « Pléistocène inférieur », etc. reçoivent leurs propres bornes (avant, seule la série entière était lue : 6 % des légendes avaient un âge trop large). Les bornes suivent l'ICS 2023, **y compris le rattachement du Gélasien au Pléistocène (2009)**.
  - *Question* : les cartes antérieures à 2009 placent le Gélasien (2,58 – 1,8 Ma) dans le Pliocène supérieur. Faut-il appliquer l'ancienne convention selon la date de la feuille, ou garder la convention actuelle partout ?
  - *Réponse* :

- [ ] **LIEU-04** 🟠 — **« Moyen » pour les séries qui n'ont que deux subdivisions officielles**
  - *Ce que fait l'application* : bornes choisies d'après l'usage français ancien :

    | Terme | Bornes retenues (Ma) |
    |---|---|
    | Crétacé moyen | 113 – 93,9 (Albien – Cénomanien) |
    | Oligocène moyen | 32 – 27,8 |
    | Pliocène moyen | 3,6 – 3,0 |
    | Carbonifère moyen | 331 – 307 (Namurien – Westphalien) |
    | Dogger moyen | 170,9 – 165,3 |
    | Malm moyen | 157 – 152 |

  - *Question* : ces équivalences sont-elles celles qu'emploient les cartes du BRGM ?
  - *Réponse* :

- [ ] **LIEU-05** 🟠 — **Termes informels « basal », « terminal », « sommital »**
  - *Ce que fait l'application* : « basal » reçoit les bornes de la subdivision inférieure, « terminal » et « sommital » celles de la subdivision supérieure. C'est trop large (ex. : Miocène terminal = 11,6 – 5,3 Ma au lieu du seul Messinien).
  - *Question* : faut-il restreindre au dernier ou au premier étage (Messinien, Priabonien, Maastrichtien, Rhétien…) ?
  - *Réponse* :

- [ ] **LIEU-06** ⚪ — **Âge affiché pour une légende « X à Y »**
  - *Ce que fait l'application* : elle réunit les intervalles (début du plus ancien → fin du plus récent) et prend le milieu comme âge de la carte du monde.
  - *Question* : le milieu est-il un bon choix pour une formation longue (ex. volcanisme de 3,6 Ma à 774 000 ans), ou vaut-il mieux le début de la formation ?
  - *Réponse* :

- [ ] **LIEU-07** 🟠 — **Âge de la carte au 1/1 000 000 réutilisé**
  - *Ce que fait l'application* : quand la légende au 1/50 000 ne donne pas d'âge, elle reprend celui de la carte au millionième, seulement si les deux cartes décrivent la même famille de roche.
  - *Question* : cette règle est-elle trop permissive ou trop stricte ?
  - *Réponse* :

### 1.2 Roches lues dans les légendes

- [ ] **LIEU-08** 🔴 — **Rattachement de termes locaux ou anciens à une roche de référence**
  - *Ce que fait l'application* :

    | Terme de la légende | Roche affichée |
    |---|---|
    | latite, mugéarite, benmoréite, doréite, trachylabradorite | trachyandésite |
    | labradorite (Massif central), leucobasalte, hawaïte, ankaramite, spilite, trachybasalte | basalte |
    | picrite, teschénite, ophite | dolérite |
    | monzonite, syénite, lamprophyres (kersantite, vaugnérite) | « roche magmatique » générique |
    | pegmatite, aplite, alaskite | granite |
    | trondhjémite | tonalite |
    | leptynite, kinzigite | gneiss |
    | métapélite | schiste |
    | métabasite | amphibolite |
    | métatexite, diatexite, anatexite | migmatite |
    | granulite (sauf si la légende parle de granite) | roche métamorphique |
    | mylonite, ultramylonite, blastomylonite | roche métamorphique |
    | phtanite | chert |
    | ampélite | argilite |
    | arènes, altérites, isaltérites | altérites (roche décomposée) |

  - *Question* : ces rattachements sont-ils acceptables ? Lesquels mériteraient une roche à part entière (avec photo et texte) ?
  - *Réponse* :

- [ ] **LIEU-09** 🟠 — **Termes ambigus**
  - *Ce que fait l'application* : « minette » n'est **pas** compté comme lamprophyre (en Lorraine, c'est le minerai de fer oolithique) ; « granulite » n'est compté comme roche métamorphique que si la légende ne cite pas de granite (ancien sens : granite à deux micas).
  - *Question* : d'autres termes des cartes françaises ont-ils un double sens de ce genre ?
  - *Réponse* :

- [ ] **LIEU-10** ⚪ — **Légendes sans roche reconnue**
  - *État* : 1 574 légendes sur 16 864 (9 %) n'affichent que « Formation géologique », faute de nom de roche dans le texte (« unité indéterminée », « formation ferrifère »…).
  - *Question* : faut-il un affichage plus utile dans ce cas (famille déduite de l'âge ou de la notation, par exemple) ?
  - *Réponse* :

### 1.3 Textes « milieu de formation »

- [ ] **LIEU-11** 🔴 — **Texte d'environnement de chaque roche**
  - *Ce que fait l'application* : chaque roche a une phrase sur le milieu de formation, rédigée par l'auteur de l'application (Claude). À relire en priorité : trachyandésite (volcan continental de rift ou de point chaud), bauxite (Les Baux-de-Provence, Crétacé, climat tropical), altérites, andésite (« typiquement au-dessus d'une zone de subduction »), flysch, molasse.
  - *Question* : ces textes sont-ils justes et suffisamment nuancés pour la France ?
  - *Réponse* :

### 1.4 Le monde à l'époque

- [ ] **LIEU-12** 🟠 — **Reconstitutions paléogéographiques**
  - *Ce que fait l'application* : modèle GPlates de Merdith et al. (2021) ; les terres sont dessinées avec les contours des côtes actuelles reconstruites.
  - *Question* : ce modèle est-il le bon choix pour l'Europe de l'Ouest ? L'usage des côtes actuelles est-il trompeur ?
  - *Réponse* :

- [ ] **LIEU-13** 🔴 — **Noms des continents, océans et chaînes de montagnes par époque**
  - *Ce que fait l'application* : tables rédigées de mémoire (périodes d'existence et position des noms) : Pangée, Gondwana, Laurussia, Avalonia, Armorica, Téthys, Rhéique, chaîne varisque, calédonienne, alpine, pyrénéenne, etc.
  - *Question* : les périodes et positions sont-elles correctes ?
  - *Réponse* :

### 1.5 Confronter l'observation à la carte

- [ ] **LIEU-14** ⚪ — **Verdicts « accord / désaccord »**
  - *Ce que fait l'application* : à la fin de la clé, elle compare la roche identifiée à celle de la carte, selon que l'échantillon était en place ou isolé, et propose des explications (galet de rivière, bloc erratique, éboulis, remblai ; simplification de la carte, limite de formation).
  - *Question* : les explications proposées sont-elles les bonnes, et dans le bon ordre de fréquence ?
  - *Réponse* :

### 1.6 Profil géologique

- [ ] **LIEU-15** 🟠 — **Lecture automatique du profil**
  - *Ce que fait l'application* : elle signale la formation du point culminant, les formations aux pentes moyennes les plus raides et les plus douces (« les roches résistantes arment souvent les reliefs… mais la pente dépend aussi des rivières et des glaciers »), et l'écart d'âge entre les roches traversées.
  - *Question* : cette lecture est-elle pertinente, ou risque-t-elle d'induire des conclusions fausses ?
  - *Réponse* :

- [ ] **LIEU-16** ⚪ — **Coupe en profondeur (étape future)**
  - *Projet* : prolonger les contacts en profondeur à partir des pendages et des failles de la BD Charm-50, d'abord dans les bassins sédimentaires.
  - *Question* : est-ce raisonnable ? Dans quels contextes faut-il s'en abstenir ?
  - *Réponse* :

---

## 2. Identifier une roche

- [ ] **CLE-01** 🔴 — **Structure de la clé**
  - *Ce que fait l'application* : clé de 24 questions construite à partir de critères classiques de pétrographie macroscopique (structure, texture, minéraux visibles, dureté, réaction à l'acide).
  - *Question* : les critères sont-ils justes et dans le bon ordre ? Des roches courantes en France manquent-elles ?
  - *Réponse* :

- [ ] **CLE-02** 🟠 — **Schémas illustrant chaque choix**
  - *Question* : les illustrations schématiques (textures, cristaux, foliation…) sont-elles fidèles et lisibles ?
  - *Réponse* :

- [ ] **CLE-03** 🟠 — **Photos d'exemple à côté des schémas**
  - *Ce que fait l'application* : une photo libre (Wikimedia Commons) par choix ; quand le choix mène à une autre question, la photo montre une roche typique de la branche (« ex. : granite »).
  - *Points faibles connus* : « pas d'effervescence » illustré par une ardoise ; craie illustrée par une falaise ; granodiorite au grain fin ; « goût amer » (sylvite) sans photo.
  - *Question* : quelles photos remplacer, et par quoi ?
  - *Réponse* :

- [ ] **CLE-04** ⚪ — **Degré de confiance des critères**
  - *Idée* : indiquer pour chaque critère s'il est robuste (effervescence) ou trompeur (couleur), et ce qu'il faudrait pour trancher entre deux roches proches.
  - *Question* : utile ? Quels critères qualifier de fragiles ?
  - *Réponse* :

---

## 3. Faire parler la roche (diagrammes)

### Rattachement des roches aux diagrammes

- [ ] **DIAG-00** 🟠 — **Positions « à la louche » des roches**
  - *Ce que fait l'application* : chaque roche ouvre ses diagrammes avec une position type (ex. trachyandésite : SiO₂ 59 %, alcalins 8,8 % dans le TAS ; scénario « point chaud » pour la naissance du magma).
  - *Question* : ces positions types sont-elles représentatives des roches françaises ?
  - *Réponse* :

### De quoi était fait le magma — Streckeisen

- [ ] **DIAG-QAPF-01** 🟠 — Coordonnées des champs (IUGS, Streckeisen 1976) et compositions types. *Question* : à vérifier.
  - *Réponse* :

### D'où vient cette lave — TAS (alcalins totaux – silice)

- [ ] **DIAG-TAS-01** 🟠 — Champs de Le Bas et al. (1986) et limite alcalin / subalcalin d'Irvine et Baragar (1971). *Question* : coordonnées et textes de lecture à vérifier.
  - *Réponse* :

### Dorsale ou subduction — AFM (alcalins – fer – magnésium)

- [ ] **DIAG-AFM-01** 🔴 — Points de la limite tholéiitique / calco-alcaline d'Irvine et Baragar **saisis de mémoire** ; six compositions types arrondies. *Question* : à vérifier.
  - *Réponse* :

### Pourquoi un magma est né — géotherme et solidus de la péridotite

- [ ] **DIAG-MELT-01** 🟠 — Solidus et liquidus secs d'après Katz et al. (2003) ; conversion 1 GPa ≈ 32 km. *Question* : paramétrisation adaptée ?
  - *Réponse* :
- [ ] **DIAG-MELT-02** 🔴 — **Solidus hydraté schématique**, géotherme simplifié (conduction puis adiabatique 0,4 °C/km), quatre scénarios (dorsale 1 350 °C / 8 km ; point chaud 1 550 °C / 90 km ; subduction 1 300 °C / 70 km + eau ; craton 1 350 °C / 180 km). *Question* : valeurs et textes acceptables ?
  - *Réponse* :

### L'ordre d'apparition des cristaux — diagrammes de phases

- [ ] **DIAG-PH-01** 🟠 — Eutectique diopside – anorthite, boucle des plagioclases (solution idéale), ternaire **schématique (champ du spinelle omis)**. *Question* : simplifications acceptables pour ce public ?
  - *Réponse* :

### La profondeur et la chaleur subies — pression – température

- [ ] **DIAG-PT-01** 🔴 — **Limites de faciès schématiques.** *Question* : à vérifier.
  - *Réponse* :
- [ ] **DIAG-PT-02** 🟠 — Minéraux repères (zones de Barrow) et conditions associées : chlorite 380 °C / 0,4 GPa, biotite 450 / 0,5, grenat 520 / 0,6, staurotide 580 / 0,65, disthène 620 / 0,75, sillimanite 700 / 0,7, andalousite 550 / 0,25, cordiérite 600 / 0,2. Silicates d'alumine d'après Holdaway (1971), point triple ≈ 500 °C / 0,38 GPa. *Question* : valeurs acceptables ?
  - *Réponse* :

### La force du courant — Hjulström

- [ ] **DIAG-HJ-01** 🟠 — Courbes redessinées à partir d'une douzaine de points de contrôle. *Question* : fidélité suffisante ?
  - *Réponse* :

### La durée et le mode de transport — forme et tri des grains

- [ ] **DIAG-MORPH-01** 🔴 — **Le découpage de la grille émoussé × tri en milieux** (éboulis, rivières, plages, vent, grains hérités) est une interprétation de l'auteur, pas une référence publiée. *Question* : acceptable ? Une référence existe-t-elle ?
  - *Réponse* :

### L'énergie de la mer dans un calcaire — Dunham

- [ ] **DIAG-DUN-01** 🟠 — Textes d'interprétation des six textures et des quatre types de grains. *Question* : à relire.
  - *Réponse* :

### Le relief disparu — QFL (quartz – feldspaths – fragments de roches)

- [ ] **DIAG-QFL-01** 🔴 — Coordonnées des champs de Dickinson et al. (1983) **saisies de mémoire**. *Question* : à vérifier.
  - *Réponse* :

---

## 4. Données et sources

- [ ] **SRC-01** 🔴 — **Licence de la BD Charm-50.** `SOURCES.md` indique « Licence Ouverte (Etalab) » de mémoire ; la fiche data.gouv.fr indique « License Not Specified ». *Question* : quelle licence exacte, et quelle mention de source ?
  - *Réponse* :
- [ ] **SRC-02** 🟠 — **Références bibliographiques** de `SOURCES.md` (auteurs, années, revues) écrites de mémoire. *Question* : à vérifier.
  - *Réponse* :
- [ ] **SRC-03** ⚪ — **Simplification des polygones** au 1/50 000 (tolérance 20 m). *Question* : acceptable pour l'usage pédagogique ?
  - *Réponse* :

---

## Journal des mises à jour

| Date | Modification |
|---|---|
| 22/11/2026 | Création du document : synthèse des questions accumulées depuis le début du projet. |
