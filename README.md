# OpengraphParser
REST service to extract OpenGraph data from page with given URL.

## Run
`python server.py`

## Request example
Make `POST` request to `/` with data:
```
{
  "url": "https://ya.ru/"
}
```

Response should be something like that:
```
{
  "description": "Найдётся всё", 
  "image": "//yastatic.net/s3/home/logos/share/share-logo_ru.png", 
  "locale": "ru_RU", 
  "site_name": "Яндекс", 
  "title": "Яндекс", 
  "type": "website"
}
```
