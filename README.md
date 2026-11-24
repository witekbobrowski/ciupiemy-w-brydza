# Ciupiemy w brydża

Strona i ściągawki krakowskiego klubu brydżowego **Ciupiemy w brydża**.

**Gramy w poniedziałki od 18:00** w Léa Bistro, ul. Juliusza Lea 11b, Kraków.

- Strona: **https://ciupiemy.pl** (po podpięciu domeny; do tego czasu adres `github.io`)
- System licytacji: **/system**
- Karty do druku: **/karty/karty-do-druku.pdf**

## Co jest w repozytorium

```
build/                  generator — tu się wszystko zmienia
  content.py            TREŚĆ KART (system licytacji) — jedyne źródło prawdy
  build.py              buduje karty PNG, PDF i stronę
  components.css        wspólny wygląd paneli i kafelków odzywek
  card.css              rama karty 9:16 + jasny motyw do druku
  site.css              wygląd strony
  templates/            szablony HTML strony głównej i strony systemu
  fonts/                Shantell Sans, Source Sans 3 (licencja SIL OFL), symbole kolorów z DejaVu Sans
docs/                   gotowa strona (GitHub Pages serwuje ten folder)
  index.html            strona główna
  system/index.html     system licytacji (ciupiemy.pl/system)
  karty/                4 karty PNG 1080×1920 + PDF do druku
SYSTEM.md               pełny opis systemu, ustalenia i otwarte pytania
zrodla/                 zdjęcia oryginalnych odręcznych karteczek i poprawek
```

## Jak zmienić system

1. Popraw tekst w `build/content.py` (składnia opisana na górze pliku).
2. Zbuduj:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r build/requirements.txt
   playwright install chromium          # tylko za pierwszym razem
   python build/build.py
   ```

3. Obejrzyj lokalnie: `python -m http.server -d docs 8000` → http://localhost:8000
4. Zatwierdź i wypchnij (`git add -A && git commit -m "..." && git push`). Strona odświeży się sama po minucie lub dwóch.

Karty PNG, PDF i strona zawsze powstają z tej samej treści, więc nie rozjadą się ze sobą.
Gdy jakiś tekst nie zmieści się na karcie, `build.py` wypisze `UWAGA: treść się nie mieści!`.

## Druk

`docs/karty/ciupiemy-sciagawki.zip` — wszystkie karty PNG w jednej paczce (przycisk „Pobierz wszystkie karty”; na telefonie strona proponuje zapis obrazów do galerii).

`docs/karty/karty-do-druku.pdf` — A4 pionowo, 4 karty na jednej stronie, białe tło.
Drukuj w skali 100% („Rzeczywisty rozmiar”), nie „Dopasuj do strony”. Wytnij po przerywanej linii —
karta ma ok. 7,5 × 13,5 cm. Dobrze wygląda zalaminowana.

## Hosting i domena (GitHub Pages)

1. Repozytorium na GitHubie → **Settings → Pages** → Source: *Deploy from a branch*, branch `main`, folder `/docs`.
2. Po zakupie domeny: **Settings → Pages → Custom domain** wpisz `ciupiemy.pl` (plik `docs/CNAME` tworzy się przy budowaniu z `SITE_URL` w `build/content.py`). U rejestratora domeny ustaw DNS:

   | Typ   | Nazwa | Wartość |
   |-------|-------|---------|
   | A     | @     | 185.199.108.153 |
   | A     | @     | 185.199.109.153 |
   | A     | @     | 185.199.110.153 |
   | A     | @     | 185.199.111.153 |
   | CNAME | www   | `witekbobrowski.github.io` |

3. Po propagacji DNS (zwykle do kilku godzin) w **Settings → Pages** zaznacz **Enforce HTTPS**.

Aktualne adresy IP GitHub Pages: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## Podgląd linku

Obrazek `docs/assets/og.png` (1200 × 630) i znaczniki Open Graph powstają przy budowaniu. Adres strony jest w `SITE_URL` w `build/content.py`; po podpięciu domeny trzeba go zmienić i zbudować stronę od nowa.
