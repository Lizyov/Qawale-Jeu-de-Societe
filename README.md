# PROJET QAWALE

## Démarrer le projet

Ce projet utilise la technologie Docker ce qui permet son déploiement sur beaucoup d'environnements.

**Il faut bien évidemment avoir Docker ET Docker-compose d'installé sur votre machine, nous conseillons Linux pour plus de facilité (https://docs.docker.com/engine/install/ubuntu/ && https://docs.docker.com/compose/install/linux/)**

Pour lancer le projet, utilisez la commande ```docker-compose down && docker-compose up --build -d --remove-orphans``` (vous devez être dans le repertoire où se situe docker-compose.yml).

Vous pouvez ajouter ```--detach``` ou ```-d``` pour se détacher de la console.

Le projet sera accessible depuis http://[votre-ip]:3669.