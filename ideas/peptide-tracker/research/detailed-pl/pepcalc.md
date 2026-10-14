# Peptide Calculator: PepCalc — analiza konkurenta

Stan źródeł: 14 października 2026. Analizowany produkt: **David Dzeveckij, App Store ID 6747501164**. Nie jest to PepCalc firmy Awesome Labs. Źródłem recenzji jest cały dostarczony CSV, który zawiera cztery wpisy. Nie instalowałem aplikacji; stan funkcji opisuję według oficjalnego listingu, a doświadczenia według recenzji.

## Oficjalny produkt i komunikacja

Źródło: [App Store USA](https://apps.apple.com/us/app/peptide-calculator-pepcalc/id6747501164).

Listing: darmowa aplikacja medyczna; 4,7/5 z 497 ocen; język angielski, iPhone/iPad, iOS 15.1+. Brak widocznego panelu zakupów wewnętrznych. Deklaracja prywatności: deweloper nie zbiera danych; Apple jej nie weryfikuje.

Promowane funkcje: obliczanie objętości dla wpisanej dawki i zawartości fiolki; obliczanie objętości rozpuszczalnika dla wybranego stężenia; przeliczanie mL na jednostki strzykawki U-100. Opis deklaruje wejście w mcg albo mg i uniwersalność niezależnie od peptydu. Nie wymienia historii, przypomnień, zapasu, wykresów, AI, HealthKit ani eksportu. Brak wzmianki nie dowodzi braku funkcji w aplikacji.

Marketing eksponuje prostotę, szybkość, precyzję i ograniczenie pomyłek. Alternatywami są arkusze, ręczne obliczenia i kalkulatory internetowe z reklamami. Deklaruje interfejs bez reklam i rozpraszania, adresowany do badaczy, biohackerów, entuzjastów fitness i wellness. Historia wersji: 1.0.0 — 1 sierpnia 2025; 1.0.1 — 5 sierpnia 2025, poprawka błędu. W listingu nie widać późniejszych aktualizacji. Link polityki prywatności prowadzi do https://www.dzeveckij.studio/apps/peptide-calculator, ale narzędzie internetowe nie uzyskało dostępu do tej strony.

## Statystyka całego CSV

Plik: `Peptide_Calculator__PepCalc_US_reviews_2026-10-14 02-45-30.csv`.

| Wskaźnik | Wynik |
|---|---:|
| Wszystkie wiersze | 4 |
| Unikalne review_id | 4 |
| Kraj | 4/4 USA |
| Zakres dat UTC | 12.12.2025–08.09.2026 |
| Średnia w CSV | 4,00/5 |
| Mediana w CSV | 4,5/5 |
| 5 gwiazdek | 2 (50%) |
| 4 gwiazdki | 1 (25%) |
| 3 gwiazdki | 0 |
| 2 gwiazdki | 1 (25%) |
| 1 gwiazdka | 0 |
| Odpowiedzi dewelopera | 0/4 |

**497 ocen w sklepie nie jest liczbą tekstowych opinii w pliku.** Średnia 4,00 w czterech recenzjach nie podważa sklepowego 4,7. To różne zbiory. Próba jest ekstremalnie mała i niereprezentatywna; jeden dodatkowy wpis istotnie zmieniłby procenty. Z braku odpowiedzi nie można wyciągać wniosku o jakości prywatnego supportu.

## Wszystkie recenzje — dowody i interpretacja

### 12.12.2025, 4/5, really86 — „Great app”

Krótki cytat: „Does not roundup like others.”

Autor docenia brak zaokrąglania, a jednocześnie prosi o możliwość przełączenia jednostek z mcg na mg. To istotne połączenie: użytkownik może lubić podstawowe działanie i nadal odczuwać realny problem użyteczności. Recenzja nie zawiera danych pozwalających sprawdzić, czy algorytm faktycznie nie zaokrągla lub jak prezentuje wyniki.

Wniosek dla naszego produktu: jawne jednostki przy każdej wartości, prosty wybór jednostki wejściowej, kontrolowane zaokrąglenie wyniku i odrębne pokazanie wartości obliczonej oraz prezentowanej. Nie wolno traktować liczby miejsc po przecinku jako dowodu bezpieczeństwa klinicznego.

### 01.04.2026, 5/5, kat78061 — „Love this”

Krótki cytat: „This takes the guesswork out of it!”

Autor wspomina różnicę między mikrogramami i miligramami i chwali łatwość użycia. Nie prosi o nowe funkcje. To wskazuje na wartość ograniczenia wysiłku związanego z jednostkami. Nie potwierdza jednak istnienia przełącznika: recenzja może opisywać ogólne korzyści kalkulatora.

Wniosek dla naszego produktu: wyświetlać wynik jako czytelne podsumowanie wpisanych danych, tak aby użytkownik mógł sprawdzić, skąd wynik się wziął; krótkie objaśnienie jednostek lepsze od ukrytej konwersji.

### 28.05.2026, 5/5, 65andmore — „Easy peasy”

Krótki cytat: „so easy o reconstitute and dose”.

Ogólna pochwała łatwości wykonania dwóch podstawowych zadań. Brak opinii o historii, zapasie lub monetyzacji. Najbardziej ostrożna interpretacja: proste narzędzie potrafi dostarczać wystarczającą wartość bez rozbudowanego zestawu funkcji.

Wniosek dla naszego produktu: podstawową czynność należy projektować jako samodzielny, szybki przepływ. Nie zmuszać użytkownika do tworzenia profilu, dodawania celu czy przechodzenia przez rozbudowany onboarding przed prostym zadaniem.

### 08.09.2026, 2/5, Sirjojo — „Can’t switch between mcg and mg”

Krótki cytat: „I shouldn’t have to add three zeros”.

Autor zgłasza brak możliwości używania obu jednostek i konieczność ręcznego przeliczania przez trzy zera. To najbardziej konkretna negatywna recenzja. Zbliżony problem zgłoszono dziewięć miesięcy wcześniej. Nie mamy numerów wersji w eksporcie, więc nie możemy przypisać obu opinii do konkretnego wydania.

Wniosek dla naszego produktu: konwersja jednostek jest problemem podstawowego przepływu, nie dodatkiem premium. Przełączenie jednostki powinno zachować fizyczną wielkość, a nie sam numer. Stan jednostki musi być zawsze widoczny. Należy sprawdzić poprawność po zmianie jednostki, ponownym otwarciu ekranu i edycji danych.

## Kodowanie tematów

Kategorie mogą się nakładać; jedna recenzja może chwalić i krytykować.

| Temat | Liczba recenzji | Siła wniosku |
|---|---:|---|
| Łatwość i wygoda | 2/4 | Konkretny sygnał, ale mała próba |
| Brak/nieodnajdywalny przełącznik mcg–mg | 2/4 | Dwa niezależne zgłoszenia; priorytet do sprawdzenia |
| Ograniczenie zgadywania z jednostkami | 1/4 | Wartość percepcyjna, nie audyt obliczeń |
| Pochwała braku zaokrągleń | 1/4 | Jednostkowa preferencja |
| Cena lub paywall | 0/4 | Brak dowodu problemu i brak dowodu gotowości do płacenia |
| Przypomnienia, backup, eksport, Apple Health | 0/4 | Nie są żądaniami z tego pliku |

Nie należy zamieniać „2/4” na tezę, że połowa wszystkich użytkowników ma ten problem. Jednocześnie zgodne zgłoszenia konkretnych jednostek są lepszą podstawą decyzji UX niż abstrakcyjna chęć „dodania AI”.

## Co prawdopodobnie działa

1. Bardzo wąska obietnica produktu. Użytkownik trafia z konkretnym zadaniem i widzi dedykowane narzędzie. Dwie recenzje wyraźnie doceniają łatwość.
2. Zdejmowanie wysiłku matematycznego. Opinia kat78061 opisuje korzyść emocjonalną: mniejsza niepewność podczas pracy z jednostkami.
3. Bezpłatny dostęp może redukować tarcie wyboru; to hipoteza oparta na cenie, nie wniosek o konwersji z CSV.
4. Wrażenie precyzji: jeden użytkownik wyróżnia niezaokrąglanie. Może to być ważne w komunikacji wyniku, ale nie jest potwierdzeniem dokładności medycznej.

Nie mamy danych o instalacjach, retencji, przychodach ani skuteczności poszczególnych haseł marketingowych. Wysoka średnia sklepu potwierdza korzystną ocenę wielu osób; nie identyfikuje przyczyny biznesowego sukcesu.

## Co można poprawić i jak się odróżnić

### Najmocniej poparta okazja: ergonomia jednostek

Zaimplementować wyraźny przełącznik mg/mcg przy każdym odpowiednim polu i natychmiastowe spójne przeliczenie. Dodać podsumowanie danych wejściowych, odwracalne zmiany oraz walidację pustych, zerowych i sprzecznych wartości. Poprawność i czytelność należy zweryfikować testami matematycznymi oraz testami z użytkownikami. Przed rozwojem kalkulatora konieczna jest odrębna ocena wymagań publikacji i kwalifikacji takiej funkcji.

### Okazja o słabszym dowodzie: wyjaśnialne wyniki

Pokazać nazwy jednostek, zależności i sposób prezentacji zaokrągleń; ułatwić sprawdzenie własnych danych. Nie używać ogólnych gwarancji bezpieczeństwa. Hipoteza wynika z pochwały precyzji i kłopotów jednostkowych, nie z bezpośredniej prośby o ekran wyjaśnienia.

### Rozszerzenie poza kalkulator

Przejście od jednorazowego zadania do historii użytkownika, harmonogramu, zapasu lub eksportu może dawać powód do regularnego używania. **W tych czterech recenzjach nie ma prośby o takie rozszerzenie.** Nie wolno przedstawiać tego jako potwierdzonej potrzeby klientów PepCalc. Trzeba sprawdzić ją w recenzjach trackerów i rozmowach.

### Co nie wystarczy jako przewaga

Sama prostota, brak reklam, prywatność i darmowy kalkulator są już elementami komunikacji tego konkurenta. „My też mamy kalkulator” nie uzasadnia abonamentu. Najlepsze różnicowanie wymaga udowodnienia przewagi w użyteczności konkretnego przepływu lub dodania regularnej korzyści, której użytkownik potrzebuje.

## Ocena strategiczna

PepCalc jest konkurentem o zadanie i frazę wyszukiwania, a nie pełnym odpowiednikiem rozbudowanego dziennika. Pokazuje, że bardzo wąskie narzędzie zbiera dobre oceny. Jednocześnie daje konkretny sygnał niedopracowania jednostek. Nie jest wystarczającym dowodem, że użytkownicy zapłacą za lepszy kalkulator, ponieważ ten produkt jest darmowy, a CSV nie zawiera żadnej wypowiedzi o płatnościach.

Przed projektowaniem warto ręcznie przetestować wybór jednostek w aktualnej wersji. Możliwe wyjaśnienia rozbieżności obejmują brak funkcji, słabą widoczność, inną jednostkę danego pola lub zachowanie starszej wersji. Bez instalacji nie wybieram jednego z nich jako faktu.
