# Pierre qui parle

*Ce que racontent les roches de France*

**Une roche est à la fois un acteur et un témoin de l'histoire de la Terre. Elle permet de comprendre le mouvement dans l'immobile.**

« Pierre qui parle » est une application web de géologie pour la France métropolitaine. Elle relie trois approches pour donner du sens à l'identification d'une roche :

1. **Les roches selon un lieu** — à partir d'une position, la roche attendue sous vos pieds, son âge, le milieu dans lequel elle s'est formée et une carte du monde à cette époque.
2. **Identifier une roche** — une clé de détermination illustrée, qui se termine sur ce que la roche raconte.
3. **Les roches dans un diagramme** — dix diagrammes où l'on place une roche « à la louche » ou précisément, chacun répondant à une question sur son passé (Streckeisen, TAS, AFM, géotherme et solidus de la péridotite, diagrammes de phases, pression – température, Hjulström, forme et tri des grains, Dunham, QFL).

Public visé : de l'adulte curieux au géologue averti.

## Statut : version soumise à relecture

Cette version est un prototype proposé à la **relecture de la communauté**. Plusieurs tables et tracés sont schématiques ou simplifiés ; ils sont listés dans [SOURCES.md](SOURCES.md), section « Points à valider ». Corrections et critiques sont bienvenues : ouvrez un ticket (*Issues*) ou proposez une modification (*Pull request*).

## Utilisation

- **En ligne** : via GitHub Pages, à l'adresse du dépôt (voir la rubrique *About*).
- **En local** : téléchargez le dépôt et ouvrez `index.html` dans un navigateur. Pour le mode détaillé au 1/50 000 en local, importez le dossier `geol50k` depuis la rubrique « Cartes détaillées » de l'application, ou servez le dossier avec `python -m http.server`.

Une connexion internet est nécessaire (fond de carte, services du BRGM, reconstitutions paléogéographiques, photos).

## Contenu du dépôt

| Élément | Rôle |
|---|---|
| `index.html` | L'application complète, en un seul fichier (HTML, CSS, JavaScript) |
| `geol50k/` | Cartes géologiques au 1/50 000 par département, dérivées de la BD Charm-50 du BRGM |
| `outils/` | Scripts Python de conversion de la BD Charm-50 (shapefile → JSON allégé) |
| `SOURCES.md` | Données, références scientifiques et points à valider |

## Licence

Code, textes et schémas de l'application : **CC BY-NC-SA 4.0** (voir [LICENSE](LICENSE)).
Les données et services tiers gardent leurs propres licences (voir [SOURCES.md](SOURCES.md)).

## Auteur

[Nhan LE] — application développée avec l'assistance de Claude (Anthropic).
