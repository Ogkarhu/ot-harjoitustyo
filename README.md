**Ohjelmistotekniikka, harjoitustyö**

harjoitustyön aihe on budjettisovellus



## Dokumentaatio

- Määrittelydokumentti https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md

- Työaikakirjanpito https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md

- Release https://github.com/Ogkarhu/ot-harjoitustyo/releases/tag/viikko5

- Käyttöohje https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md

- Testidokumentaatio https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md

## Asennus

1. Riippuvuuksien asennus:
```bash
poetry install
```
2. Alustus:
```bash
poetry run invoke build
```
3. Käynnistä sovellus:
```bash
poetry run invoke start
```

## Testaus

Testiraportti luodaan komennolla:
```bash
poetry run invoke coverage-report
```
raportit löytyvät muodostuneesta htmlcov-kansiosta
