"""
TREŚĆ KART — tu edytujesz system.

Po zmianie uruchom:  python build/build.py
Powstaną: karty PNG (telefon), PDF do druku i strona w docs/.

Mini-składnia w tekstach:
  **pogrubienie**      -> pogrubiony tekst
  {13–20 PC}           -> wyróżniony zakres punktów (zielony)
  ♠ ♥ ♦ ♣              -> kolory; ♥ i ♦ same robią się czerwone

Row(odzywka, opis, dopisek)   — jeden wiersz; dopisek (szary, mniejszy) jest opcjonalny.
  Odzywka może być listą: ["1♥", "1♠"] -> jeden kafelek "1♥ ♠".
  Prefiks "po " -> "po 2♣" pokazuje małe "po" przed kafelkiem.
Panel(nagłówek, wiersze, tag=..., callout=...) — sekcja; tag to zielona plakietka z progiem punktów.
Note(tekst) — ciemna notka na dole karty.
"""
from dataclasses import dataclass, field


@dataclass
class Row:
    bid: object          # str albo lista str
    text: str
    sub: str = ""


@dataclass
class Panel:
    label: str
    rows: list
    tag: str = ""
    callout: str = ""    # duży wyróżniony tekst nad wierszami (pierwsza linia = tytuł)


@dataclass
class Note:
    text: str


@dataclass
class Card:
    no: int
    slug: str
    title: str
    sub: str
    blocks: list = field(default_factory=list)


CLUB = "Ciupiemy w brydża"
# Publiczny adres strony (z ukośnikiem na końcu). Potrzebny do podglądu linku; zmień po podpięciu domeny.
SITE_URL = "https://witekbobrowski.github.io/ciupiemy-w-brydza/"
CITY_YEAR = "Kraków 2026"

CARDS = [
    Card(1, "otwarcia", "Otwarcia", "Siła i długość koloru", [
        Panel("Otwarcia na poziomie 1", tag="od 13 PC", rows=[
            Row("1♣", "{13–20 PC}, min. 3♣ (krótki trefl) lub 5+♣", "z 15–17 PC bez singla otwieraj 1BA"),
            Row("1♦", "{13–20 PC}, min. 3♦"),
            Row(["1♥", "1♠"], "{13–20 PC}, 5+ kart w kolorze starszym"),
            Row("1BA", "{15–17 PC}, ręka zrównoważona, **bez singla**"),
        ]),
        Panel("Silne otwarcia", tag="od 20 PC", rows=[
            Row("2♣", "{22+ PC} lub 4 szybkie lewy z góry", "jedyne otwarcie forsujące, zaproszenie do wysokiej gry"),
            Row("2BA", "{20–21 PC}, ręka zrównoważona", "dalej licytacja jak po 1BA"),
        ]),
        Panel("Otwarcia blokujące", tag="5–10 PC", rows=[
            Row(["2♦", "2♥", "2♠"], "6-karta, {ok. 10 PC}"),
            Row(["3♣", "3♦", "3♥", "3♠"], "7-karta, {5–10 PC}"),
        ]),
        Note("**Bez piątki w starszym** otwierasz młodszy: 1♣ (3+) lub 1♦ (3+). "
             "Zrównoważone 15–17 zawsze idą przez 1BA."),
    ]),

    Card(2, "odpowiedzi", "Odpowiedzi", "Po otwarciu partnera", [
        Panel("Po otwarciu 1 w kolor", tag="od 6 PC", rows=[
            Row("nowy", "nowy kolor na 1 — **pokazuje 5 kart**"),
            Row("+1", "podniesienie koloru partnera o 1 — **fit**"),
            Row("1BA", "{6–10 PC}, bez gwarancji zatrzymania w kolorze przeciwnika"),
        ]),
        Panel("Po otwarciu 1BA partnera", tag="transfer: bez minimum", rows=[
            Row("2♣", "**Stayman** — pytanie o czwórkę ♠ lub ♥", "od 7–9 PC, bez górnej granicy"),
            Row("2♦", "transfer — 5+♥", "dowolna siła, także poniżej 7 PC"),
            Row("2♥", "transfer — 5+♠", "dowolna siła, także poniżej 7 PC"),
            Row("2♠", "**zgłoszenie młodszych:** 5+♣ / 5+♦ lub 4-4 ♣+♦",
                "partner musi odpowiedzieć 3♣ (przymusowy przekaz)"),
        ]),
        Panel("1BA w dalszej licytacji", tag="6–10 / 12–14 PC", rows=[
            Row("1BA", "**po własnym pasie:** {6–10 PC}", "brak zatrzymania w kolorze przeciwnika"),
            Row("1BA", "**rebid otwierającego** po nowym kolorze partnera: {12–14 PC}", "niezgodność"),
        ]),
        Panel("Po silnym 2♣ partnera", tag="negat 0–8 PC", rows=[
            Row("2♦", "**negat** — {0–8 PC}, bez piątki"),
        ]),
    ]),

    Card(3, "obrona", "Obrona", "Kontra wywoławcza · Cappelletti", [
        Panel("Kontra po otwarciu przeciwnika", tag="od 13 PC",
              callout="Kontra = min. 13 PC\nPartner **musi** odpowiedzieć!",
              rows=[
                  Row("2BA", "po kontrze przeciwnika — **poparcie** w kolor partnera"),
              ]),
        Panel("Cappelletti po 1BA przeciwnika", tag="od ok. 14 PC", rows=[
            Row("2♣", "jednokolorówka — dowolny kolor"),
            Row("2♦", "dwukolorówka: **oba starsze** ♥ + ♠"),
            Row("2♥", "dwukolorówka: ♥ + kolor młodszy"),
            Row("2♠", "dwukolorówka: ♠ + kolor młodszy"),
            Row("2BA", "oba młodsze ♣ + ♦"),
        ]),
        Panel("Odpowiedzi partnera", rows=[
            Row("po 2♣", "**2♦** — pytanie o kolor", "wpisujący pasuje, jeśli jego kolorem są ♦"),
            Row("po 2♦", "kolor starszy — naturalnie, do gry", "kolor młodszy — forsing · 2BA — negat"),
            Row("po 2♥/♠", "kolor młodszy — naturalnie"),
        ]),
    ]),

    Card(4, "asy", "Pytanie o asy", "Gerber · Roman Key Card Blackwood", [
        Panel("Gerber — 4♣", tag="bez uzgodnionego atu", rows=[
            Row("4♦", "**0 lub 4** asy"),
            Row("4♥", "**1** as"),
            Row("4♠", "**2** asy"),
            Row("4BA", "**3** asy"),
        ]),
        Panel("RKCB — 4BA", tag="atu ustalone", rows=[
            Row("5♣", "**1 lub 4** klucze"),
            Row("5♦", "**0 lub 3** klucze"),
            Row("5♥", "**2 lub 5** kluczy, **bez** damy atu"),
            Row("5♠", "**2 lub 5** kluczy, **z** damą atu"),
        ]),
        Note("**Klucze = 4 asy + król atutowy.** Wariant 1430 — jeden as „na niższą”: "
             "5♣ to 1/4, 5♦ to 0/3. Liczbę rozpoznajesz z kontekstu.\n"
             "**Szlemik ≈ 33 PC** na linii · **szlem ≈ 37 PC**."),
    ]),
]


# Konwencje — lista na stronie systemu. (nazwa, opis, slug karty ze szczegółami)
CONVENTIONS = [
    ("Krótki trefl", "Otwarcie 1♣ już od 3 kart, gdy nie masz piątki w kolorze starszym.", "otwarcia"),
    ("Słabe dwójki", "Otwarcia 2♦, 2♥ i 2♠ z 6-kartą i ok. 10 PC. Blokują przeciwników.", "otwarcia"),
    ("Silne 2♣", "Jedyne otwarcie forsujące: 22+ PC lub 4 szybkie lewy z góry. Odpowiedź 2♦ to negat, 0–8 PC.", "otwarcia"),
    ("Stayman", "2♣ po 1BA partnera: pytanie o czwórkę ♠ lub ♥. Od 7–9 PC.", "odpowiedzi"),
    ("Transfery", "Po 1BA partnera 2♦ pokazuje 5+♥, a 2♥ pokazuje 5+♠. Dowolna siła.", "odpowiedzi"),
    ("2♠ na młodsze", "Po 1BA partnera: 5+♣, 5+♦ lub 4-4 w młodszych. Partner musi odpowiedzieć 3♣.", "odpowiedzi"),
    ("Kontra wywoławcza", "Kontra po otwarciu przeciwnika, od 13 PC. Partner musi odpowiedzieć.", "obrona"),
    ("2BA po kontrze", "Gdy przeciwnik skontruje otwarcie partnera, 2BA pokazuje poparcie jego koloru.", "obrona"),
    ("Cappelletti", "Wejście po 1BA przeciwnika: 2♣ jeden kolor, 2♦ oba starsze, "
                    "2♥ lub 2♠ starszy z młodszym, 2BA oba młodsze.", "obrona"),
    ("Gerber", "4♣ pyta o asy, gdy nie ma uzgodnionego atu.", "asy"),
    ("RKCB 1430", "4BA pyta o pięć kluczy (4 asy i król atutowy), gdy atu jest ustalone.", "asy"),
]
