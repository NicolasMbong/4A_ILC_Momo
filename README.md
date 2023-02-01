# Momo

## groupe 
M'BONG Nicolas
DESCHAMPS-FRILLEY Benjamin

## Sujet du projet
Nous avons choisi de réaliser le sujet guidé. 
Car nous possèdions très peut de connaissance sur les différentes démarche d'un projet CI/CD.

## Language
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Github Actions
- [Build API](https://github.com/NicolasMbong/4A_ILC_Momo/blob/main/.github/workflows/BuildAPI.yml)
  Une déclenchée à chaque changement pour builder l’application.
- [Dockfile](https://github.com/NicolasMbong/4A_ILC_Momo/blob/main/.github/workflows/DockerFile.yml) 
  Une déclenchée manuellement pour utiliser le fichier Dockerfile pour créer une image.
- [Docker Push GRC](https://github.com/NicolasMbong/4A_ILC_Momo/blob/main/.github/workflows/D%C3%A9ploiement_continue.yml)
  Une déclenchée pour chaque tag semver pour utiliser le fichier Dockerfile pour créer et
pousser l’image de l’API avec en tag la version semver spécifiée.

[Status actions](https://github.com/Naereen/badges)
