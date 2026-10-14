# Shotsy GLP-1 Tracker — analiza konkurenta i recenzji

Stan researchu: 14 października 2026. Źródło recenzji: przekazany CSV `Shotsy_GLP-1_Tracker_US_reviews_2026-10-14 02-45-28.csv`, app_id 6499510249. Oryginału nie zmieniano. Opisy funkcji oznaczają potwierdzenie w publicznej dokumentacji; nie instalowano produktu i nie wykonano audytu jego kodu ani testu wszystkich ekranów.

## Najważniejszy wniosek

Shotsy jest silnym konkurentem dzięki czytelnej wizualizacji postępów, historii przyjęć, pamiętaniu miejsca iniekcji i prostocie codziennego używania. Przyciąga obrazem postępu i poziomów leku, a utrzymuje użytkownika przez organizację rutyny. To wniosek z treści recenzji, a nie pomiar lejka marketingowego.

Najbardziej wiarygodne kierunki konkurowania z nim to trwałość historii i łatwa migracja, przewidywalny model płatności, lepsze odkrywanie istniejących funkcji oraz kontrola zapasu. Sam PDF, własne substancje, wiele harmonogramów czy tryb utrzymania wagi nie są już nowymi kategoriami funkcji względem Shotsy.

## 1. Próba i metoda

Cały plik przetworzono skryptem: 3953 rekordy i 3953 unikalne review_id. To pisemne recenzje USA, nie wszystkie oceny gwiazdkowe App Store, nie wszyscy użytkownicy i nie reprezentatywna ankieta.

Daty: 2024-05-29 do 2026-10-12. Odpowiedź dewelopera występuje w 21 rekordach (0,53%). Niska liczba odpowiedzi w eksporcie nie dowodzi, że producent nie odpowiada na zgłoszenia wysyłane innymi kanałami.

Kontrola duplikatów: 40 rekordów ponad liczbę unikalnych kombinacji autor+tytuł+treść, 41 ponad unikalne autor+treść, 47 ponad unikalne tytuł+treść, 78 ponad unikalne same treści. Nie usuwano ich automatycznie, ponieważ mogą obejmować aktualizacje opinii. Nie należy traktować każdego ID jako dowodu odrębnego człowieka. W pliku są również recenzje z niezgodnością gwiazd i tekstu: 2025-06-27, 1★, „Best app on my phone” mówi „I give it 5 stars”, a 2026-09-10, 1★, „The best app to stay Organized” zawiera pochwałę. Istnieją też opinie o leku zamiast aplikacji.

Metoda tematyczna: wyszukiwanie słów i wzorców w całym CSV; ręczna lektura nisko ocenianych opinii i kandydatów na prośby o funkcje, a dodatkowo systematyczna próbka 104 opinii 4–5★ (co 35. rekord w tej grupie). Nie twierdzę, że każdą z 3953 recenzji ręcznie przeczytano. Liczby tematów poniżej są liczbą dopasowań heurystycznych, nie zweryfikowaną klasyfikacją sentymentu.

| Ocena | Liczba | Udział |
|---|---:|---:|
| 5★ | 3281 | 83,00% |
| 4★ | 345 | 8,73% |
| 3★ | 117 | 2,96% |
| 2★ | 76 | 1,92% |
| 1★ | 134 | 3,39% |

Średnia w CSV: 4,660/5. Opinie 4–5★: 3626 (91,73%); 1–3★: 327 (8,27%). Widoczne w sklepie 4,8/5 to inny zbiór: wszystkie ratingi, nie tylko pisemne komentarze.

### Zmiana ostatnio widoczna w danych

| Okres | Recenzje | 1–3★ | Średnia |
|---|---:|---:|---:|
| grudzień 2025 | 156 | 22 | 4,474 |
| marzec 2026 | 95 | 22 | 4,074 |
| czerwiec 2026 | 156 | 14 | 4,590 |
| lipiec 2026 | 151 | 22 | 4,510 |
| sierpień 2026 | 163 | 28 | 4,393 |
| wrzesień 2026 | 142 | 24 | 4,380 |
| 1–12 października 2026 | 48 | 9 | 4,375 |

Łącznie od 1 września: 190 opinii, 33 z oceną 1–3★ (17,37%), w tym 21 z oceną 1–2★. Średnia 4,379. To sygnał większego udziału krytyki w świeżych pisemnych recenzjach, nie dowód spadku całej bazy, retencji lub przychodów. Zbieżność w czasie z aktualizacjami nie ustala przyczyny.

## 2. Produkt, zakres i cena — stan publicznie udokumentowany

**Funkcje rutyny:** wpis przyjęcia z czasem, dawką i miejscem, rotacja miejsc, notatki i objawy z nasileniem, wykresy wagi, odliczanie i widżety. Poziomy leku są estymacją, nie pomiarem. Przebieg dawek i objawów można zestawić w czasie. Są statystyki wg dawki i miejsca, tryb utrzymania wagi, podsumowanie podróży, raport PDF. Tabletki są obsługiwane na iOS. Źródło: [opis produktu](https://shotsyapp.com/glp-1-tracker/).

**Darmowy zakres:** wpisy przyjęć, przypomnienia, rotacja, objawy, waga i trendy, zmiana leków, własne dawki, szczegółowe analizy. **Shotsy+:** wykres szacowanego poziomu oraz synchronizacja Apple Health na iOS i Health Connect na Androidzie. Strona deklaruje brak limitu czasu podstawowej wersji i możliwość korzystania bez karty; zastrzega zmienność zakresu i cen. Dostępność eksportu za darmo potwierdzają także konkretne recenzje. Źródło: [free vs Shotsy+](https://shotsyapp.com/free-glp-1-tracker/).

**Listing i historia zmian:** 33K ratingów, 4,8/5. Zakupy: 9,99/14,99/19,99 USD miesięcznie i 39,99/59,99 USD rocznie; listing zawiera wiele wariantów, nie dowodzi jednego paywalla dla wszystkich. Wersja 3.3.9 z 15 września poprawia backup, odtwarzanie, Health imports i eksport; 3.3.8 z 8 sierpnia przypomnienia i startup. 3.1.0 z kwietnia dodała własne leki, a 3.2.0 pomiary tłuszczu, beztłuszczowej masy, talii i glukozy. 3.0.0 z marca dodała maintenance, tabletki i osobne harmonogramy wielu leków. Źródło: [App Store USA](https://apps.apple.com/us/app/shotsy-glp-1-tracker/id6499510249).

**Prywatność:** polityka z 6 marca 2026 rozróżnia iOS bez konta, prywatny iCloud, od Androida z Google Sign-In i Firebase. W USA na iOS zbierane mogą być anonimowe dane doświadczeń z opcją wyłączenia przyszłego zbierania; wykluczane są pola tekstowe i bezpośrednie identyfikatory. Producent deklaruje brak sprzedaży danych i przekazywania ich do reklamy targetowanej. Nie należy powtarzać uproszczenia „zero danych zbieranych”. Źródło: [privacy policy](https://shotsyapp.com/privacy/).

**Niepotwierdzone w przejrzanej dokumentacji:** kompletny food database/barcode logger, zarządzanie fiolkami/zapasem i automatyczne zamawianie, migracja iOS↔Android, dashboard kliniczny z dostępem lekarza, dowolne profile rodziny. Brak potwierdzenia nie jest dowodem nieistnienia funkcji. Te punkty wymagają instalacji lub zapytania producenta.

## 3. Co promują i jak się pozycjonują

Strona główna eksponuje rutynę GLP-1, wykresy, historię, objawy, poziomy i postęp. Deklaruje ponad milion pobrań — to liczba producenta, nie niezależnie zweryfikowany wynik. Założycielka Aja Beckett przedstawia osobistą historię i doświadczenie programistyczne, budując wiarygodność przez zrozumienie użytkownika. PDF i opieka medyczna są prominentne. Źródło: [strona główna](https://shotsyapp.com/).

Drugą warstwę wiarygodności tworzy „science”: Chief Science Officer Eric Perakslis, jego doświadczenie i nacisk na dane pacjenta, prywatność i ograniczenia estymacji. Nie oznacza to zatwierdzenia produktu przez FDA ani dowiedzionej skuteczności klinicznej. Źródło: [science](https://shotsyapp.com/science/).

Kanał kliniczny już istnieje: welcome kits dla gabinetów, materiały dla pacjentów, 30-dniowe kody próbne i przygotowanie PDF na wizytę. Nie znalazłem dowodu pełnej integracji z dokumentacją medyczną. Źródło: [providers](https://shotsyapp.com/providers/).

Z widocznej struktury linków wynika strategia SEO obejmująca nazwy leków, skutki uboczne, utrzymanie, porównania i alternatywy. To moja interpretacja architektury strony, a nie wiedza o skuteczności SEO. Recenzje wspominają rekomendacje Reddita, screenshoty wykresów, znajomych, lekarzy i reklamy Instagram. Nie znam udziałów tych kanałów.

## 4. Co działa według użytkowników

### Porządek zamiast notatek i arkuszy

Wiele osób mówi o zastąpieniu arkusza, notesu i kalendarza. Korzyścią jest mniejszy wysiłek pamiętania i jedna historia. Ważne: użytkownicy pozytywnie oceniają również wersję darmową, zatem nie każda pochwała stanowi dowód skłonności do zapłaty.

Evidence: 2025-03-29, 5★, „Everything I wanted and more!” (12478382746) — aplikacja zastąpiła Notes i zawiera więcej, niż autor początkowo oczekiwał. 2025-01-19, 5★, „Great app for tracking GLP-shots and weight” (12204653860) — przejście z arkusza, ręczne dodanie wcześniejszej historii i użyteczne notatki.

### Wykres daje motywację, gdy codzienna waga rozprasza

Ludzie lubią średnie, procenty i widoczny trend. Wyraźnie cenią widok długiego okresu, dzięki któremu chwilowy zastój nie niszczy motywacji.

Evidence: 2026-06-09, 5★, „Great App” (14162294108): wykresy pomagają nie zniechęcać się, gdy postęp wydaje się wolny. 2026-08-01, 5★, „Great for Newbies to GLP-1s!” (14375502001): trend przypomina o długim horyzoncie. W systematycznej próbce 2025-08-31, 5★, „Love!” opisuje ulgę przy plateau dzięki średniej tygodniowej.

### Pamięć miejsca zastrzyku i widget są małymi funkcjami o dużej wartości

Ludzie nie muszą otwierać rozbudowanej analityki, żeby docenić produkt. Szczególnie mocny przykład dotyczy osoby używającej widgetu do innego leku niż GLP-1.

Evidence: 2026-08-23, 5★, „Great App” (14463261179) — widget pomaga pamiętać o biologicznym leku; użytkownik wprost nie ocenia pozostałych funkcji. 2026-06-08, 5★, „Great app” (14159739364) — sugestia następnego miejsca jest ulubioną funkcją. 2025-04-04, 4★, „Great but…” (12501102945) chce jeszcze prostszej listy dat i miejsc zamiast parsowania kilku wykresów.

### Poziomy leku są atrakcyjnym magnesem premium

Użytkownicy często wskazują je jako ulubiony element; próbują zestawiać z apetytem i samopoczuciem. To evidence wartości postrzeganej, nie potwierdzenie precyzji medycznej. Recenzje mylą czasem estymację z realnym poziomem w organizmie; nasz produkt powinien jasno objaśniać ograniczenia.

Evidence: 2025-09-17, 3★, „Meh” (13146574650) wątpi w wynik niestandardowych dawek. 2025-08-20, 5★, „Very helpful” (13040174031) docenia wizualizację kumulacji. 2026-10-12, 3★, „Bait and Switch” (14656075675) mówi, że był to najlepszy element, teraz płatny.

### Automatyzacja danych i przygotowanie wizyty

Evidence: 2026-08-15, 5★, „The BEST Tracker!” (14432290441) chwali wagę z Omada przez Apple Health oraz dane żywieniowe z MyFitnessPal. Nie jest to dowód bezpośredniej integracji z każdym serwisem. 2026-08-04, 5★, „Good app!” (14386950161) chce przekazać lekarzowi dokładne informacje. 2026-06-14, 5★, „Data Nerds Dream” (14181484821) chwali darmowy eksport do własnych analiz.

### Kontakt z zespołem może budować lojalność

Evidence: 2025-07-21, 5★, „I freakin love this app… and the company behind it” (12919852663) opisuje dodanie sugerowanej opcji i przedłużenie subskrypcji. 2026-06-28, 5★, „They listen” (14235405663) chwali implementację sugestii. Trzeba zestawić z przeciwnymi doświadczeniami niżej.

## 5. Krytyka i potrzeby — evidence oraz konsekwencje

| Problem | Konkretny evidence CSV | Co można zrobić u nas |
|---|---|---|
| Niejasny trial i cena dopiero po konfiguracji | 2026-09-21, 1★, „Has you fill out all your information…” 14577117334; 2026-08-19, 1★, „Deceptive” 14448379617 | Cena i tabela zakresu przed osobistymi danymi, widoczny przycisk wersji darmowej, konkretny dzień naliczenia opłaty |
| Za krótki trial przy cotygodniowym leku | 2026-09-21, 3★, „Could be great?” 14574794236: 7 dni za krótko; chce miesiąc | Sprawdzić 21–30 dni lub trial po kilku realnych cyklach; nie uznawać dłuższego trialu za pewny wzrost konwersji |
| Utrata dostępu opłaconego wcześniej | 2026-10-05, 1★, „Bait and switch” 14628739378; 2026-09-15, 1★, „This is a great app being destroyed by greed” 14552213857 | Zachowanie przyznanych praw, jednoznaczny restore i widoczny status subskrypcji |
| Znikające wpisy/history | 2026-10-03, 3★, „Glitchy Saves” 14621169806; 2026-09-22, 2★, „Never saves!” 14581750760 | Potwierdzenie trwałego zapisu, historia zmian, lokalny backup, brak nadpisywania lokalnych rekordów opóźnioną synchronizacją |
| Niedziałające przypomnienia | 2026-10-11, 3★, „Notifications” 14651916457; 2026-09-12, 3★, „Notifications stopped working” 14541953803 | Ekran diagnostyki zgody/systemu, „następna zaplanowana notyfikacja”, test przypomnienia i odróżnienie planu od wpisu |
| Sync bez informacji o błędzie, powielanie kalorii | 2026-08-30, 3★, „No longer pulls in health data” 14489907900 | Status ostatniej synchronizacji, źródło i czas każdego rekordu, deduplikacja i instrukcja naprawy |
| Brak migracji Android→iPhone | 2026-05-28, 3★, „Systems incompatible” 14116767761; 2026-01-01, 1★, „Don’t change phones” 13580037224 | Otwarty format eksport/import, przeniesienie historii niezależne od platformy |
| Trudna edycja i wpisy wstecz | 2026-08-24, 4★, „Worth the Purchase!” 14466411274; 2026-10-06, 3★, „The app” 14634624467 | Edycja w miejscu, cofanie, liczbowy dziennik, łatwe dodanie pierwszych miesięcy leczenia |
| Prośby o ocenę za wcześnie/za często | 2026-09-21,1★,14577117334; 2026-08-31,3★,„Constant review nagging”14493818329 | Prośba po realnej korzyści, respektowanie odmowy, brak przerwania procesu |
| Photos/miary zamiast samej wagi | 2026-09-23,4★,„Excellent at tracking”14585728332; 2026-08-04,5★,„Great app for Seniors!”14384965545 | Prywatne zdjęcia i porównania w czasie, szerszy zestaw obwodów, prosty widok sukcesów innych niż waga |
| Log jedzenia to dodatkowa aplikacja | 2026-08-14,3★,„It’s okay”14426814127; 2026-07-29,4★,„Review”14361067206 | Najpierw proste sumowanie porcji i jasna integracja; budowę bazy żywności rozważyć po walidacji |
| Zapas i refill | 2024-12-27,5★,„Great app to track shots and progress with!”12112742006; 2025-07-02,5★,„Incredibly useful”12843773301 | Liczba pozostałych przyjęć, data przewidywanego wyczerpania, przypomnienie o uzupełnieniu |
| PDF za ogólny | 2025-10-25,5★,„Simple”13310247996 | Podsumowanie + opcjonalny szczegółowy dziennik dawek, objawów i notatek |
| Opt-out danych zdrowotnych | 2026-03-21,1★,„Opt-out Privacy Change”13871695720; 3★,„Popular for a reason.”13870423413 | Dobrowolny opt-in na dodatkową analizę, konkretne objaśnienie wysyłanych danych |
| Support nie zamyka problemu | 2026-06-20,1★,„Sad to go”14205147459; 2026-04-23,2★,„Info keeps disappearing after trial”13986969287 | Numer sprawy, status, potwierdzenie odebrania i procedura odtwarzania |

Powyższe są doświadczeniami autorów. Nie potwierdzają, że każdy opisany błąd występuje u każdego użytkownika lub nadal w aktualnej wersji. Deweloper w odpowiedzi 2026-03-07 do recenzji 13821991386 zaprzecza usunięciu darmowych funkcji trackingowych. Oficjalna strona obecnie potwierdza podstawowy darmowy tracker. Występuje realna rozbieżność komunikacji/odbioru, lecz z samych opinii nie da się rozstrzygnąć historii wszystkich taryf i uprawnień.

Szczególnie ważne są pozytywne recenzje z prośbami: to użytkownicy, którym produkt już pomaga, a nie wyłącznie osoby niezadowolone z ceny. Nie każdy brak jest brakującą funkcją; czasem jest nieodkrytą funkcją. 2026-09-08,5★, „Best” (14526787312) nie wie jak śledzić kilka leków, choć publiczny produkt to już obsługuje. Podobnie opinie o braku wprowadzania wagi wstecz mają odpowiedź dewelopera z 2024-06-20 wskazującą ekran Calendar (11404458355).

## 6. Heurystyczne częstości w całej próbie

Każda recenzja może wpadać w kilka wierszy. Tekst może negować problem, opisywać życzenie albo chwalić istniejącą funkcję. Nie są to liczby „tylu ludzi skarży się”.

| Wzorzec słów | Wszystkie | W 1–3★ | W 4–5★ |
|---|---:|---:|---:|
| Waga/postęp/cel/wykres |1598|69|1529|
| Prostota/ease/intuitive |1048|13|1035|
| Poziom/half-life/concentration |477|29|448|
| Miejsce/rotacja |422|13|409|
| Cena/płatność/trial/paywall |395|141|254|
| Żywienie/protein/calorie/water |328|24|304|
| Przypomnienia |289|18|271|
| Prośby/wish/suggestion |271|38|233|
| Custom/multiple/other med/reta |184|19|165|
| Bug/crash/slow/load |174|50|124|
| Lost/missing/gone/not save |147|49|98|
| Health/sync |145|13|132|
| Eksport/doctor/provider |91|3|88|

Przykład pułapki: lost może oznaczać utraconą wagę, a wish może oznaczać „żałuję, że nie znalazłem aplikacji wcześniej”. Nie wolno przedstawiać 147 jako liczby utrat danych lub 271 jako liczby próśb o nowe funkcje.

## 7. Co już poprawiono lub dodano

Stare prośby o pojedynczy tracker, brak tabletek, glukozy, lean mass, maintenance czy części miejsc brzucha muszą być zestawione z historią zmian. One pokazują rozwój rynku, nie automatycznie otwartą lukę.

Potwierdzenia w odpowiedziach CSV: blokowanie Settings w 1.3.2 na iOS17 naprawiono według dewelopera w 1.3.3 (2024-11-11,11939452773); automatyczny import/freezing 1.4.0 naprawiono według dewelopera w1.4.1 (2025-02-07,12282964934); wagę 1.2.8 poprawiono w1.2.9 (2024-10-29,11888059268); sync urządzeń miał działać od1.1.0 (2024-07-11,11479137635). Nie testowano tych napraw. Powracające późniejsze skargi wskazują, że niezawodność pozostaje ważnym wymaganiem kategorii, lecz nie ustalają tego samego root cause.

## 8. Propozycja odróżnienia od Shotsy

**Pierwszy priorytet: historia, której użytkownik może zaufać i którą może zabrać.** Local-first zapis, potwierdzenie sukcesu, historia edycji, backup przed migracją danych i czytelny eksport bez blokowania dostępu po anulowaniu. To nie „atrakcyjna nowa zakładka”, lecz rozwiązanie najbardziej kosztownej emocjonalnie klasy skarg.

**Drugi: zapas i logistyka.** Zapas fiolki/pena, pozostałe przyjęcia, kiedy zamówić, rzeczywiste zużycie oddzielone od planu, skip/pauza z powodem, zapis nietypowego harmonogramu wprowadzonego przez użytkownika. Evidence zapasu jest mocne treściowo, ale skromne liczebnie — potrzebna walidacja, nie teza o masowym zapotrzebowaniu.

**Trzeci: szybki i czytelny dziennik.** Ostatnie przyjęcie, następny plan, przycisk zapisu oraz liczby bez konieczności interpretowania wykresu. Waga i edycja powinny być widoczne. Gdy ktoś szuka funkcji, aplikacja ma prowadzić go do właściwego ekranu zamiast sugerować upgrade.

**Czwarty: raport o odpowiednim poziomie szczegółowości.** Sam PDF już istnieje. Można konkurować wyborem okresu, pełną listą przyjęć, osobnym widokiem objawów 0/obecne/brak wpisu, kompletnymi notatkami i pytaniami na wizytę. Raport nie powinien sugerować klinicznej przyczynowości z korelacji.

**Piąty: przewidywalna cena.** Jasna różnica darmowy/płatny, próba pozwalająca zobaczyć kilka cykli, brak zasłaniania zapisanej historii i zachowanie wcześniej nabytych praw. Nie trzeba walczyć wyłącznie najniższą ceną — użytkownicy chwalą też płatny produkt jako wart pieniędzy.

**Dodatki do walidacji:** prywatne zdjęcia postępu, obwody poza talią, subiektywny dzienny stan i „food noise”, niestandardowe metryki (np. BP/A1C), profile opiekuna. Prośby o A1C i ciśnienie są nieliczne; nie budowałbym od razu pełnego dashboardu diabetologicznego. Menstrual cycle występuje jako pojedyncza wyraźna prośba, nie silny statystyczny segment.

**Nie obiecywać bez walidacji:** dokładnego poziomu leku, przewidywania efektu terapii, rekomendowania dawkowania i leczenia, poprawnej estymacji dowolnych badawczych peptydów. Recenzje zawierają życzenia takich zastosowań, lecz życzenie użytkownika nie jest dowodem naukowej wykonalności ani upoważnieniem do instrukcji medycznych.

## 9. Ocena siły konkurenta

Największe przewagi: rozpoznawalność, treści i polecenia społeczności, łatwo udostępniane wykresy, dopracowana rutyna, integracje i częste aktualizacje. Dane dostarczają mocnych dowodów wartości użytkowej, lecz nie dowodzą retencji i rentowności. Największe słabości dostrzegalne w CSV: poczucie cofnięcia uprawnień/cen, skargi na zapis i migrację, słaba odkrywalność niektórych funkcji oraz niepełny ekosystem zapasu i żywienia.

Wniosek: konkurencja z Shotsy przez zwykły „tracker+reminders+PDF” będzie trudna. Wiarygodniejszy produkt ma oferować lepszy pełny przepływ: **wprowadzam dane szybko → wiem, że zapisano → widzę zapas i następny plan → poprawiam bez stresu → mogę odzyskać i przenieść całą historię**. To hipoteza do przetestowania z osobami opuszczającymi dotychczasowe aplikacje.
