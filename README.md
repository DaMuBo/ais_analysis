# AIS - Analysis
Zentrales Projekt für die explorative Analyse udn Entwicklung für AIS Anomalie Erkennung
Das Projekt ist in verschiedene Experimente unterteilt. 
Außerdem sollen die Ergebnisse in einer APp zusammengefasst und visualisiert werden.
Dies ermöglicht die interaktive Untersuchung der Daten.

## Contents
* backup_load.py
* experiments
  * k_means_clustering
  * time_series
  * anomaly_detection
* functions
  * utils.py
* connection.yml
* connection_example.yml
* README.md
* requirements.txt
* .gitignore

## Usage
Zuerst die Daten von dem Remote Server aus dem Projekt für das Streaming über backup_load.py reinladen.

connections.yml "path/to/backup/file"

Wenn dies erfolgreich ist, dann sind die connection.yml richtig konfiguriert. Ansonsten die Daten abgleichen mit den Credentials für die Datenbank.
Wenn das eingerichtet ist können die Experimente durchgeführt werden oder die App ausgeführt werden.


## Contacts
* Author: Daniel Müller
* E-Mail: daniel.mueller@damu-analytics.com
* Website: damu-analytics.de
* University: FOM - Hochschule für Oekonomie und Management