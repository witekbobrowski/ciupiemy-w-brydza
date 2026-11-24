# Jak pomóc

Błąd w systemie, literówka, pomysł na stronę? Każda poprawka jest mile widziana.

## Najprościej: zgłoszenie

Otwórz [zgłoszenie (issue)](https://github.com/witekbobrowski/ciupiemy-w-brydza/issues) i napisz, co jest nie tak
i gdzie (karta, sekcja, odzywka). Nie musisz umieć programować.

## Poprawka w kodzie albo treści

1. Zrób fork i gałąź.
2. Zmieniaj tylko źródła w `build/`:
   - treść kart i systemu: `build/content.py` (składnia opisana na górze pliku),
   - teksty strony: `build/templates/`,
   - wygląd: `build/components.css`, `build/card.css`, `build/site.css`.
3. Zbuduj: `python build/build.py` (instalacja w [README](README.md#jak-zbudować)).
4. Sprawdź stronę lokalnie na szerokim i wąskim ekranie oraz karty w `docs/karty/`.
5. Zatwierdź źródła razem z wygenerowanym `docs/` i otwórz pull request.

## Zasady

- Nie edytuj ręcznie plików w `docs/`. Powstają z `build/` i następne budowanie je nadpisze.
- `UWAGA: treść się nie mieści!` przy budowaniu oznacza błąd. Skróć tekst, nie zmniejszaj układu.
- Treść jest po polsku. Zmiany w samym systemie licytacji (co znaczy odzywka) najpierw uzgadniamy
  w zgłoszeniu, bo muszą być zgodne z tym, jak gramy przy stole. Otwarte pytania są w `SYSTEM.md`.
- Bez śledzenia użytkowników i bez zewnętrznych skryptów. Strona ma działać jako zwykłe pliki statyczne.
