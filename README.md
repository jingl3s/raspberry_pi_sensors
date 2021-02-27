
![#ffa500](https://placehold.it/12/ffa500?text=+) In progress


# raspberry_pi_sensors


Projet personnel avec un Raspberry Pi et des capteurs de temperature et humidite

Ce projet se base sur d'autres projets en fork dans mon dépot

## Dépendances

* Python 3 > 3.7


## Mise en place

* Recuperation des projets dépendant dans le dossier courant

```shell
git clone https://github.com/jingl3s/raspberry_pi_DHT21-AM2301
git clone https://github.com/jingl3s/DHT11_Python


python3 -m venv venv
. venv/bin/activate

cd DHT11_Python
python3 setup.py install
cd -

cd raspberry_pi_DHT21-AM2301/src/am2301
make
cd -
```

## Utilisation


```shell
. venv/bin/activate

cd src
python3 am2301.py
```

## La suite

* Modifier le code C pour retourner les valeurs dans un format simili JSON
  * ~~Temperature~~
  * ~~Humidite~~
  * Success ou echec
  * ~~Nombre d'essais avant d'avoir la valeur~~
* Mise en place d'un script Python pour appeler le script et lire les valeurs
  * ~~Script sans boucle~~
  * Ajouter boucle
* Ajouter le DHT11 similaire au précédent
* Ajouter des DS18B20
* Executer la lecture pour voir les valeurs
* Refactoriser le script pour faire tous les appels en concurrent avec asyncio
* Calibrer les valeurs
 