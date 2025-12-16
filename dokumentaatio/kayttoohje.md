Sovellus käynnistyy suorittamalla

```bash
poetry run invoke start
```

## Aloitusnäkymä

![Aloitusnäkymä](https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sov_etusivu.png)

Aloitusnäkymässä käyttäjä näkee koosteen budjetistaan.

Painamalla "Add expense" tai "Add income" aukeaa uusi valikko

![Lisäys](https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sov_lisays.png)

"Amount:" -kohtaan lisätään valinnasta riippuen kulu tai tulo
"Name:" -kohtaan lisätään nimitunniste kululle tai tulolle
"Date" -kohtaan lisätään päivämäärä
"Recurring?" -kohtaan laitetaan ruksi jos tapahtuma toistuu kuukausittain

## Syötenäkymä

Yksittäiset syötteet näkyvät painamalla "Show all entries"

![Syötteet](https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sov_syotteet.png)

Syötteen voi poistaa painamalla "Delete entry"

Tästä aukeaa ikkuna johon voi syöttää poistettavan syötteen ID:n (ensimmäinen kenttä syötenäytössä)

![Poisto](https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sov_poisto.png)

Syöte poistuu sovelluksesta

![Poistettu](https://github.com/Ogkarhu/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sov_poistettu.png)
