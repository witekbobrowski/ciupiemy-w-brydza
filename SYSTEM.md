# System licytacji klubu Ciupiemy w brydża

Naturalny system z pięciokartowymi starszymi i krótkim treflem. Najbliżej mu do amerykańskiego
**SAYC** (Standard American Yellow Card). Źródłem są odręczne karteczki klubowe (`zrodla/karteczki/`)
oraz poprawki naniesione na wydruki (`zrodla/poprawki/`).

Treść kart i strony generuje się z `build/content.py`. Ten plik jest opisem i uzasadnieniem.

---

## 1. Otwarcia

| Odzywka | Znaczenie |
|---|---|
| **1♣** | 13–20 PC, min. 3♣ (krótki trefl) lub 5+♣. Ręka zrównoważona 15–17 bez singla idzie przez 1BA, nie przez 1♣. |
| **1♦** | 13–20 PC, min. 3♦. |
| **1♥ / 1♠** | 13–20 PC, 5+ kart w kolorze. |
| **1BA** | 15–17 PC, ręka zrównoważona, bez singla. |
| **2♣** | 22+ PC lub 4 szybkie lewy z góry. Jedyne otwarcie forsujące, zaproszenie do wysokiej gry. |
| **2BA** | 20–21 PC, ręka zrównoważona; dalej licytacja jak po 1BA. |
| **2♦ / 2♥ / 2♠** | Blok: 6-karta, ok. 10 PC. |
| **3 w kolor** | Blok: 7-karta, 5–10 PC. |

Bez piątki w starszym otwiera się młodszy: 1♣ (3+) lub 1♦ (3+).

## 2. Odpowiedzi

### Po otwarciu 1 w kolor (od 6 PC)
- **Nowy kolor na 1** — pokazuje 5 kart.
- **Podniesienie koloru partnera o 1** — fit.
- **1BA** — 6–10 PC, bez gwarancji zatrzymania w kolorze przeciwnika.

### Po otwarciu 1BA partnera
| Odzywka | Znaczenie |
|---|---|
| **2♣** | Stayman — pytanie o czwórkę ♥ lub ♠. Od 7–9 PC, bez górnej granicy. |
| **2♦** | Transfer — 5+♥. Dowolna siła, także poniżej 7 PC. |
| **2♥** | Transfer — 5+♠. Dowolna siła, także poniżej 7 PC. |
| **2♠** | Zgłoszenie młodszych: 5+♣, 5+♦ albo 4-4 w ♣ i ♦. Otwierający musi odpowiedzieć 3♣ (przymusowy przekaz — 3♣ nic nie mówi o jego ręce). |

### 1BA w dalszej licytacji
- **Po własnym pasie** — 6–10 PC, brak zatrzymania w kolorze przeciwnika.
- **Rebid otwierającego** po otwarciu w kolor i nowym kolorze partnera — 12–14 PC, niezgodność.

### Po silnym 2♣ partnera
- **2♦ = negat** — 0–8 PC, brak piątki.

## 3. Obrona

### Kontra wywoławcza
- Kontra po otwarciu przeciwnika = **min. 13 PC**. Partner **musi** odpowiedzieć.
- Po kontrze przeciwnika: **2BA = poparcie** w kolor partnera.

### Cappelletti po 1BA przeciwnika (od ok. 14 PC)
| Odzywka | Znaczenie |
|---|---|
| **2♣** | Jednokolorówka w dowolnym kolorze. |
| **2♦** | Dwukolorówka: oba starsze (♥ + ♠). |
| **2♥** | Dwukolorówka: ♥ + kolor młodszy. |
| **2♠** | Dwukolorówka: ♠ + kolor młodszy. |
| **2BA** | Oba młodsze (♣ + ♦). |

Odpowiedzi partnera:
- **po 2♣**: 2♦ pyta o kolor; wpisujący pasuje, jeśli jego kolorem są ♦.
- **po 2♦**: kolor starszy — naturalnie, do gry; kolor młodszy — forsing; 2BA — negat.
- **po 2♥ / 2♠**: kolor młodszy — naturalnie.

## 4. Pytanie o asy

### Gerber — 4♣ (bez uzgodnionego atu, zwykle po BA)
4♦ = 0 lub 4 asy · 4♥ = 1 · 4♠ = 2 · 4BA = 3.

### RKCB — 4BA (atu ustalone), wariant 1430
Kluczy jest 5: cztery asy i król atutowy.

| Odpowiedź | Znaczenie |
|---|---|
| **5♣** | 1 lub 4 klucze |
| **5♦** | 0 lub 3 klucze |
| **5♥** | 2 lub 5 kluczy, bez damy atu |
| **5♠** | 2 lub 5 kluczy, z damą atu |

Orientacyjnie: szlemik ≈ 33 PC na linii, szlem ≈ 37 PC (ogólna reguła, nie z klubowych karteczek).

---

## Historia ustaleń

- **RKCB:** na pierwszej wersji kart 5♣ i 5♦ były zamienione (0/3 i 1/4). Poprawione na 1430: 5♣ = 1/4, 5♦ = 0/3.
- **Transfery 2♦/2♥:** bez dolnej granicy siły, także poniżej 7 PC.
- **Stayman:** dolna granica 7–9 PC.
- **2♠ po 1BA:** to zgłoszenie młodszych (5+♣ / 5+♦ / 4-4), a nie pytanie — otwierający odpowiada 3♣ obowiązkowo.
- **1♦:** od 3 kart. Karteczka podaje ogólnie „1 kolor = 5+ kart”; ustalono, że dotyczy to tylko starszych.

## Do ustalenia

- **2♣ — szybkie lewy:** na karteczce odczytane jako „4 szybkie lewy z góry”. Jeśli miało być „2”, popraw w `build/content.py`.
- **2♠ → 3♣ → ?** Co odpowiadający robi po przymusowym 3♣ (typowo: pas z treflami, 3♦ z karami, coś innego z 4-4).
- **Cappelletti „od ok. 14 PC”** — tak zapisano na karteczce; w praktyce wiele par wchodzi lżej, zwłaszcza z dobrym układem.

## Na tle innych systemów

- **SAYC** — praktycznie ten sam szkielet: 5-kartowe starsze, krótki młodszy, 1BA 15–17, silne 2♣, słabe dwójki, Stayman i transfery.
- **2/1 Game Forcing** — ten sam szkielet, ale odpowiedź 2 w nowy kolor jest forsingiem do końcówki, a 1BA na otwarcie w starszy jest forsujące. U nas tego nie ma.
- **Wspólny Język (Polish Club, WJ)** — najpopularniejszy w Polsce, ale zupełnie inny: wieloznaczne 1♣ (m.in. 12–14 bez piątki, 18+ dowolne) i słabe 1BA.
- **Acol** — czterokartowe starsze i słabe 1BA 12–14.
- **Precision** — sztuczne silne 1♣ od 16 PC.

## FunBridge

Najbliższy profil to **SAYC** (`Menu → Settings → Bidding conventions`). Nie wybierać Polish Club
(to WJ). 2/1 jest blisko, ale z forsingiem do końcówki po odpowiedzi 2 w nowy kolor.

Na stronie polecamy też **Tricky Bridge** (nauka od zera, po angielsku) i **BBO** (gra z ludźmi i robotami; roboty licytują 2/1).
