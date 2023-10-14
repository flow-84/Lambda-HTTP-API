# AWS Lambda und S3 Bucket Beispiel

## CloudFormation
Die Vorlage befindet sich in der Datei `CF-Lambda.yaml`.

## Architektur
![Architektur Diagramm](./CF-Lambda-designer.png)


Dieses Repository enthält zwei AWS Lambda-Funktionen (`lambda-get` und `lambda-post`), die über ein API-Gateway erreichbar sind, und einen S3-Bucket zum Speichern von Textdateien.

## Architektur

- **API-Gateway**: Zwei Endpunkte (`GET` und `POST`)
- **Lambda-Funktionen**: `lambda-get` und `lambda-post`
- **S3-Bucket**: Zum Speichern der Textdateien

## Erweiterungen

1. `lambda-post` speichert die Datei unter einem zufälligen Namen.
2. `lambda-post` gibt die URL für den `GET`-Aufruf zurück.
3. `lambda-get` löscht die gelesene Datei nach dem Abrufen.

## Erläuterungen

### Lambda-POST-Funktion

In der `POST`-Funktion wird die Nachricht aus dem `body` des `event`-Objekts extrahiert und in einer Datei im S3-Bucket gespeichert. Die Datei erhält einen zufälligen Namen durch `uuid.uuid4()`. Die genaue URL für den `GET`-Aufruf wird in der Antwort zurückgegeben.

### Lambda-GET-Funktion

In der `GET`-Funktion wird die Datei, die im S3-Bucket gespeichert ist, gelesen und danach gelöscht.
