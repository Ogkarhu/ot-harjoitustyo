**Ohjelmistotekniikka, harjoitustyö**

harjoitustyön aihe on budjettisovellus



## Dokumentaatio

- Määrittelydokumentti https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md

- Työaikakirjanpito https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md

- Release https://github.com/Ogkarhu/ot-harjoitustyo/releases/tag/viikko5
<<<<<<< HEAD

- Käyttöohje https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md

- Testausdokumentti https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md

=======

- Käyttöohje https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md

- Testidokumentaatio https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md
>>>>>>> 80fbab5a95c517b8f5d173eaf73e7af28d40e19c

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
