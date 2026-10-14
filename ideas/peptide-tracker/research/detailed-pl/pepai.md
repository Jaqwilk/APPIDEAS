# Pep AI — szczegółowa analiza konkurenta i 138 recenzji US

Stan badania: 14 października 2026. Badany produkt: Pep AI: GLP-1 Peptide Tracker / Peptide GLP-1 Tracker, Zode Development LLC, Apple ID 6758682710. Nazwa w marketingu i indeksie bywa przestawiana. Źródło recenzji: dostarczony CSV `Pep_AI__GLP-1_Peptide_Tracker_US_reviews_2026-10-14 02-45-33.csv`. Plik źródłowy pozostał nienaruszony.

## Najważniejszy wniosek

Pep AI potwierdza, że użytkownicy płacą za porządek w wielu harmonogramach, kontrolę zapasu i zebranie danych zdrowotnych w jednym miejscu. Najbardziej obiecująca droga konkurowania to jednak **stabilny, szybki i przewidywalny codzienny tracker**, a nie jeszcze większa liczba funkcji. Recenzje bardzo wyraźnie pokazują koszt utraty podstawowej funkcji, zmian układu oraz zawodnego zapisywania. Użytkownik, który chce tylko zapisać przyjęcie, nie musi chcieć maskotki, społeczności ani rozbudowanego żywienia.

Istotna korekta: duża fala skarg dotyczy wersji z 30 września. Deweloper następnie przywrócił kalkulator, jednostki oraz klasyczny wygląd. To dowód problemu przy wdrożeniu i okazji do zdobycia zaufania, **nie dowód, że konkurent obecnie nie ma tych funkcji**.

## Metoda i ograniczenia

- Odczyt całego CSV przez parser CSV, także treści wielowierszowych, i kontrola identyfikatorów. Wszystkie 138 rekordów mają różne review_id.
- 138 recenzji tekstowych nie jest pełną populacją ocen aplikacji. Nie znamy zasad eksportu, kompletności ani reprezentatywności. CSV jest znacznie bardziej negatywny od oceny widocznej w sklepie, ale to nie dowodzi manipulacji oceną.
- Średnie są liczone z rating, daty z date_utc. Daty podane dalej w UTC, więc pojedynczy lokalny dzień może wypaść inaczej.
- Tematy analizowano ręcznie po przeczytaniu całego korpusu. Niżej podaję jawne listy ID dla wybranych kategorii. Kategorie mogą się nakładać. Nie jest to automatyczna klasyfikacja ani odsetek wszystkich użytkowników.
- Publiczne funkcje są deklaracjami producenta i historią wersji, nie wynikiem testu aplikacji na telefonie. Recenzja potwierdza doświadczenie konkretnej osoby, nie bezbłędne działanie u wszystkich.
- CSV nie zawiera wersji aplikacji użytej przez autora. Powiązanie z 4.0 opiera się na dacie, treści i odpowiedziach firmy, nie na polu technicznym. data_utc może odzwierciedlać także aktualizację opinii, więc nie rekonstruuje pełnej historii ocen.
- Słowa „scam” używane w opiniach są oceną autorów, nie ustaleniem oszustwa. Zgłoszenia naliczeń i utraty danych nie były weryfikowane w logach produktu.

## Statystyki korpusu

| Miara | Wynik |
|---|---:|
| Rekordy / unikalne review_id | 138 / 138 |
| Kraj | US, wszystkie rekordy |
| Zakres dat | 17.02.2026–12.10.2026 |
| Średnia | 2,6884 / 5 |
| 1★ | 65 — 47,1% |
| 2★ | 12 — 8,7% |
| 3★ | 8 — 5,8% |
| 4★ | 7 — 5,1% |
| 5★ | 46 — 33,3% |
| 1–2★ razem | 77 — 55,8% |
| 4–5★ razem | 53 — 38,4% |
| Rekordy z odpowiedzią dewelopera | 58 — 42,0% |

| Miesiąc | Liczba | Średnia | Oceny 1–2★ |
|---|---:|---:|---:|
| Luty | 5 | 4,20 | 1 |
| Marzec | 9 | 2,89 | 5 |
| Kwiecień | 8 | 3,25 | 3 |
| Maj | 20 | 3,05 | 9 |
| Czerwiec | 26 | 2,42 | 15 |
| Lipiec | 14 | 2,64 | 8 |
| Sierpień | 11 | 4,00 | 3 |
| Wrzesień | 20 | 2,15 | 15 |
| Październik do dnia eksportu | 25 | 2,00 | 18 |

Przed 30.09: 104 recenzje, średnia 2,98. Od 30.09: 34 recenzje, średnia 1,79, z czego 27 to 1–2★. To silny sygnał kryzysu w analizowanym zbiorze po wdrożeniu 4.0. Nie wolno czytać go jako zmierzonego spadku retencji lub konwersji.

## Co produkt promuje

Na stronie producenta dominują trzy obietnice: cały protokół w jednym miejscu, kontrola następnego przyjęcia i zapasu oraz żywienie dopasowane do użytkowników GLP-1. Białko i błonnik są eksponowane bardziej niż sama liczba kalorii. Strona pokazuje twórców społecznościowych i powołuje się na 200 tys. pobrań oraz około 3700 ocen. Są to deklaracje firmy, a „#1” jest hasłem marketingowym, nie udowodnionym rankingiem. [Strona główna](https://pepaiapp.com/).

Firma opisuje wzrost przez współpracę z twórcami w społeczności peptide/GLP-1 oraz szybkie wdrażanie zmian. Zespół to Cedric Roberge, Adrian Partain i Lucas Bennett; produkt powstał na początku 2026 r. Opowieść o zastępowaniu arkuszy i notatek odpowiada potrzebie widocznej w recenzjach. Nie potwierdza natomiast przychodu ani rentowności. [O firmie](https://pepaiapp.com/about).

Widoczny ekosystem stron o poszczególnych trackerach, kalkulatorach, półtrwaniach i porównaniach sugeruje szeroką strategię SEO. To mój wniosek ze struktury serwisu, nie pomiar jego ruchu. Bezpłatne narzędzia internetowe mogą być wejściem do aplikacji, a różne landing pages adresują intencje „calculator”, „cycle”, „protein” i konkretne substancje.

## Mapa funkcji i tego, co użytkownicy faktycznie doceniają

| Obszar | Zakres potwierdzony publicznie lub przez recenzje | Znaczenie konkurencyjne |
|---|---|---|
| Dziennik przyjęć | Historia, harmonogramy, przypomnienia, wiele substancji | Podstawowa wartość: nie pamiętać wszystkiego samemu |
| Fiolki | Zapas, pozostała ilość, przewidywanie końca, reconstitution math | Powód wyboru nad zwykłym kalendarzem |
| Cykle | Indywidualne okresy on/off, wiele cykli jednocześnie, przypomnienie restartu, historia | Odpowiada bardziej złożonej grupie niż pojedynczy GLP-1 |
| Miejsca iniekcji | Mapa i rotacja | Doceniane jako część jednej rutyny |
| Poziomy | Szacowane krzywe na podstawie historii i półtrwania | Zrozumiały wizualny argument, ale nie pomiar biologiczny |
| Żywienie | Zdjęcie, barcode, wyszukiwanie, quick-add, głos; makro, białko, błonnik, woda | Dla części użytkowników tworzy codzienny nawyk |
| Objawy | 18 gotowych kategorii GLP-1 oraz własne | Łączenie objawów z osią czasu |
| Postępy | Waga, kroki, zdjęcia; Apple Health | Zastępowanie kilku aplikacji |
| Edukacyjne AI | Pep Bot | Mocno promowane, ale opinie pokazują oczekiwania przekraczające ograniczenia funkcji |
| Dane pomocnicze | Recenzje wspominają badania, sen, aktywność, raporty | Wartość dla bardziej zaangażowanych użytkowników |
| Interakcje społecznościowe | Grupy, community i ankiety; chwalone w recenzji 11.10 | Dodatek dla części grupy; nie jest uniwersalnie pożądany |

Zestaw dawek/fiolki/mapa/poziomy/AI potwierdza [strona peptide tracker](https://pepaiapp.com/peptide-tracker). Zakres cykli potwierdza [cycle tracker](https://pepaiapp.com/peptide-cycle-tracker). Zakres GLP-1, metod zapisu, symptomów i Health potwierdza [GLP-1 tracker](https://pepaiapp.com/glp-1-tracker-app). Żywienie szczegółowo opisuje [food tracker](https://pepaiapp.com/glp-1-food-tracker). Rozróżniam deklarowaną obsługę od łatwości i niezawodności jej realizacji.

## Aktualne ceny, wersje i naprawy

Listing US pokazuje 9,99 USD miesięcznie, produkty roczne 29,99–49,99 USD i produkt tygodniowy 3,99 USD. To lista IAP, nie dowód, że każdy widzi wszystkie oferty. W recenzjach wielokrotnie pojawia się trial 3 dni i paywall przed realnym wypróbowaniem. [App Store](https://apps.apple.com/us/app/pep-ai-peptide-glp-1-tracker/id6758682710).

Historia wersji: 4.0.0 z 30.09 — redesign z Arlo; 4.0.1 z 01.10 — według odpowiedzi firmy powrót kalkulatora; 4.0.2 z 03.10 — powrót jednostek przy dawkach; najnowsza 4.0.3 — Classic look, szybki log na Home i personalizacja kalorii/błonnika. Wcześniej dodawano Watch, widgets, Live Activities, różne drogi podania, własne objawy i backdating. Odpowiedź do kwietniowej recenzji deklaruje naprawę zapisu badań i duplikowania harmonogramu. [Historia wersji](https://apps.apple.com/us/app/pep-ai-peptide-glp-1-tracker/id6758682710).

Uwaga: powrót ciemnego stylu i jednostek już osłabia możliwość odróżnienia się samym wyglądem. Potrzebna przewaga trwała: przewidywalność obsługi i danych.

## Co się sprawdza — dowody z recenzji

### 1. Uwolnienie od notatek i pamiętania harmonogramów

- 11.09, 5★, „Love it”, ID 14535991314: autor opisuje chaos zeszytu i wiele informacji co/kiedy/ile; aplikacja przyniosła spokój, a żywienie było dodatkową korzyścią.
- 02.09, 5★, „Must have!”, 14502381148: szczególnie przydatna przy wielu peptydach z różnymi harmonogramami.
- 01.05, 5★, „Love it!!”, 14017568595: poprzednio trudność z pamiętaniem przyjęć i z rozpoznaniem, co już zostało przyjęte.
- 12.10, 5★, „Best app for your pep”, 14657805964: po około dwóch miesiącach autor nie potrzebuje zapisywać wszystkiego w kalendarzu i przypomnieniach.

Wniosek dla nas: komunikować konkretną ulgę „wiesz, co już zapisano i co planujesz”, a nie liczbę ekranów. Szybki widok dnia i oddzielenie „planowane” od „przyjęte” są krytyczne.

### 2. Zapasy i arytmetyka

- 20.02, 5★, „Great for tracking”, 13771055656: ile dni zostało oraz kiedy zamówić kolejną fiolkę.
- 20.02, 5★, „Great app”, 13770720510: pozostała ilość w fiolkach.
- 28.08, 5★, „Great app”, 14481941480: kalkulator, harmonogramy, reminders i tracking wielu substancji.
- 11.08, 5★, „SellingThe937’s FAVORITE Peptide App”, 14416169507: uporządkowane wpisy i zastąpienie ręcznego sprawdzania matematyki.

Wniosek: zapas ma wartość także wtedy, gdy użytkownik zna dawkę i niczego od aplikacji medycznie nie oczekuje. Sam kalkulator nie wyjaśnia całej wartości: liczy się związek fiolki, wpisu i historii. Funkcje obliczeń należy jednak ocenić odrębnie pod kątem wymagań sklepu i zakresu medycznego.

### 3. Jeden produkt i częstszy nawyk

- 03.07, 5★, „W app”, 14256628945: korzystanie codziennie dzięki żywieniu, krokom i wadze także w dni bez przyjęcia.
- 06.09, 5★, „Best Protocol Tracker”, 14515589996: planował anulować trial, ale po przetestowaniu dawek, matematyki, żywienia, wagi i Apple Health zdecydował, że warto płacić.
- 18.04, 5★, „Tracking Reta & TRT”, 13969282405: ceni dawki, mapę, częstotliwość, posiłki, wodę, sen, badania i skanowanie posiłków.
- 11.10, 5★, „The New Pep AI Upgrade Is on a Whole Different Level!”, 14654140571: bardzo pozytywnie ocenia integrację protokołów, preset meals i grup; prosi o Fitbod.

Wniosek: rozbudowa może pomagać retencji części użytkowników, ale nie dowodzi wzrostu retencji całej bazy. Ten sam all-in-one odstrasza inny segment. Najbardziej sensowna interpretacja to modułowość, nie dokładanie każdemu wszystkich ekranów.

### 4. Reakcja na feedback

- 20.03, 5★, „Worth it”, 13869331648: sugestia weszła w następnym update.
- 31.05, 5★, „Awesome!”, 14127475204: autor chwali wdrożenie zaproponowanej zmiany i uważny zespół.
- 29.05, 5★, „Great App”, 14120997583: wspomina naprawę funkcji w 24 h, przy tym chwali estymator poziomów.
- 11.10, 3★, „Not the worst, but not my fave”, 14653693854: aplikacja nie odpowiadała, ale szybkie rozwiązanie problemu z trialem skłoniło do przyznania 3★.

Nie wystarczy „mamy support”: liczy się konkretne przywrócenie działania. W innych recenzjach ten sam support jest oceniany negatywnie.

## Co nie działało i czego chcą użytkownicy

### A. Redesign naruszył codzienną rutynę

28 recenzji w jawnej kategorii negatywnej reakcji na redesign. Autorzy skarżą się na konieczność szukania funkcji, kreskówkowy styl, rozpraszającą maskotkę i poczucie zmiany produktu z organizatora protokołów na zwykły tracker wagi. Kilku deklaruje odejście, anulowanie lub zwrot. To deklaracje, nie potwierdzone wydarzenia w billingach.

Najmocniejsze dowody:

- 30.09, 2★, „New update”, 14611262385: prośba o wybór profesjonalnego ciemnego wyglądu zamiast cartoon style.
- 01.10, 1★, „This update is…”, 14613571037: trudniej zapisać pominiętą dawkę; maskotka rozprasza.
- 02.10, 2★, „New update sucks”, 14617913890: nie tylko estetyka, także ponowne uczenie się, gdzie są funkcje.
- 04.10, 2★, „Non stop updates”, 14625335194: ludzie chcą szybko zapisać przyjęcie i wrócić do dnia; funkcje przychodzą i znikają, a aplikacja jest przeładowana.
- 01.10, 1★, „Last version was perfect..”, 14615441271: autor wcześniej polecał produkt klientom i teraz żałuje tych rekomendacji.

Dla nas: stały układ najważniejszych działań, opcjonalne moduły, spokojny styl, zachowanie istniejących skrótów po aktualizacji. Naprawiony Classic look oznacza, że „mamy dark mode” jest zbyt słabym wyróżnikiem.

### B. Utrata kalkulatora i czytelnych jednostek

15 recenzji ręcznie zakodowanych jako zarzut utraty kalkulatora, konwersji lub jednostek po redesignie. Dodatkowo 04.10 autor zaktualizował swoją ocenę do 5★, „CALCULATOR IS BACK!!”, 14628483179. Inny autor 01.10, „Put it’s back”, 14615971250, napisał, że kalkulator jest pod „+”, choć sam nadal nie lubił update.

To ma dwie lekcje: część ludzi naprawdę płaciła za konkretne narzędzie; oraz funkcja przeniesiona do trudno widocznego miejsca bywa odbierana jak usunięta. Deweloper przyznał, że wyjęcie kalkulatora było błędem. Powrót funkcji nie musi natychmiast przywrócić zaufania.

### C. Zapisy i dane

12 wskazanych recenzji zgłasza utratę danych, niemożność zapisu lub niedostępność logowania (kategorię definiuję szerzej niż tylko fizyczne usunięcie danych). Dużo zgłoszeń przypada na czerwiec–lipiec.

- 13.07, 1★, „Not worth paid premium”, 14298998225: dwukrotna konfiguracja, ponowne uruchomienie jak u nowego użytkownika.
- 03.07, 1★, „Not saving anything i enter”, 14258769030: compounds/schedules/cycles nie widać następnego dnia.
- 30.06, 1★, „I really wanted to like it”, 14245799719: po ponownym wprowadzeniu wszystkich informacji rano historia zniknęła.
- 30.06, 3★, „Refuses to log my doses”, 14244668623: zakończone wpisy następnego dnia oznaczone jako missed, utrata streak.
- 31.05, 3★, „Useful app, but buggy”, 14127541075: update usunął zapisane posiłki.
- 05.04, 3★, „First day review”, 13925534660: zapis badań się kręci i harmonogram duplikuje; developer deklaruje późniejszą naprawę obu.

Nie twierdzę, że problemy są nadal obecne. Historyczne raporty są wystarczające, by wskazać wymóg produktu: potwierdzenie zapisu, działanie offline, backup/eksport, spójne cofanie edycji, migracje danych testowane przed wydaniem. Bez danych z aplikacji nie wiemy, czy zniknięcie było błędem sync, konta, widoczności czy usunięciem.

### D. Jednostki nie odpowiadają wszystkim substancjom

09.08, 2★, „Good Concept, but the Developers Have More Work to Do”, 14406725241: przy jednej substancji można wybrać mg/mcg/units, przy innej units są widoczne, lecz nie da się ich wybrać, a przy HCG dostępne jednostki nie odpowiadają potrzebie IU. Autor chce móc zapisać faktycznie podaną liczbę jednostek i odrzuca płatność, dopóki core nie działa. Deweloper proponuje powiadomienie, kiedy opcje zostaną dodane, bez potwierdzenia ukończenia.

14.09, 2★, „Not for me!”, 14549731895: także niedostępny domyślny wybór IU, brak odpowiedzi i około godziny konfiguracji.

Dla nas: model danych musi odróżniać masę, objętość i jednostki aktywności oraz zachowywać zapis źródłowy. Nie wolno traktować IU i syringe units jak synonimów. To nie powinien być wolny tekst bez walidacji.

### E. Paywall zanim użytkownik zobaczy wartość

10.09, 2★, „Looks great but ask for subscription immediately”, 14532254005: deklaruje gotowość do zapłaty, ale dopiero po poznaniu produktu; wybiera darmową alternatywę. Odpowiedź firmy potwierdza model paid software z trialem, a nie dłuższe darmowe używanie.

18.05, 2★, „Possibly good but misleading”, 14080106078: informacje o opłacie dopiero po konfiguracji. 28.04, 1★, „Have to pay”, 14006661948: nie chce płacić za nieznany sposób działania. 12.03, 2★, „You have to pay to use”, 13841402278: brak dostępu do powodów pobrania: fiolki i harmonogram.

Dla nas: pokaż demo, pozwól zrobić pierwszy pełny wpis i wcześnie przedstaw cenę. Z tych recenzji nie wynika automatycznie, że freemium ma wyższy zysk; wynika jasno potrzeba uczciwego pokazania wartości przed zobowiązaniem.

### F. Billing i anulowanie

10 recenzji w jawnej kategorii problemów z trialem, naliczeniem, dublowaniem subskrypcji, anulowaniem lub rozpoznaniem aktywnej płatności. Przykłady:

- 14.09, 2★, 14549731895: według autora dwie aktywne subskrypcje, Apple i Stripe.
- 21.07, 1★, „Terrible”, 14330533679: jednoczesne obciążenie roczne i miesięczne.
- 24.09, 1★, „Cannot cancel”, 14589209864: strona anulowania nie otwiera się, potem naliczenie.
- 06.09, 1★, „Don’t download.”, 14517789045: brak subskrypcji w Apple, przekierowanie na stronę i brak e-maila.
- 28.05, 1★, „3 days free trial fluke”, 14115177426: po anulowaniu dla bezpieczeństwa utrata premium przed końcem trialu.

Deweloper oferuje sprawdzenie aktywnych planów i pomoc. Nie mamy potwierdzenia każdego rozwiązania. Dla nas: jeden czytelny ekran planu ze wskazaniem kanału zakupu, końca trialu i miejsca anulowania; blokada przypadkowego drugiego aktywnego planu. Jeden kanał płatności na początku może uprościć produkt.

### G. AI z obietnicą szerszą niż rzeczywista użyteczność

7 recenzji w jawnej kategorii skargi na Pep Bot/AI. Część chce odpowiedzi o dawkach i praktykach, których produkt według aktualnych zastrzeżeń nie powinien indywidualnie rekomendować. Inne zgłaszają brak połączenia, blokowanie pytań lub błędną informację o funkcjach produktu.

- 08.05, 3★, „Cool app, AI chat sucks”, 14042340667: tracker oceniony jako przydatny, chat jako nieodpowiadający.
- 05.06, 1★, „AI bot doesn’t work at all”, 14145537614: nie odpowiada na pytanie o skutki uboczne.
- 28.09, 1★, „Useless”, 14603326812: oczekiwanie informacji o dawkach i przechowywaniu.
- 01.10, 1★, „Update is awful!!”, 14615939726: bot powiedział, że kalkulatora nigdy nie było; developer przyznał błędną odpowiedź i deklaruje naprawę.

Dla nas: AI opcjonalne, precyzyjnie opisane, z oddzielonym wsparciem obsługi produktu i edukacją. Pomoc ekranowa powinna czerpać z aktualnej wersji dokumentacji, a nie generować niezweryfikowane instrukcje. Nie reklamować AI jako doradcy dawki. Tych skarg nie traktować jako uzasadnienia, żeby dawać ryzykowniejsze medyczne rekomendacje.

### H. Żywienie: łatwość kontra dokładność

12.09, 5★, „Everything You Need”, 14540044592: skanowanie opakowanych produktów chwalone, przy zdjęciach czasem ręczna korekta makro z pomocą innego AI. 16.06, 3★, „Meal intake”, 14187855994: błędne ilości wymagają ręcznej korekty. 04.07, 1★, „James”, 14261496644: autor ocenia wygenerowany cel kalorii jako zawyżony.

Dla nas: szybka poprawka porcji, wyraźny status „szacunek”, łatwy ręczny wpis. Budowa własnego skanera nie jest automatycznie dobrym priorytetem MVP, jeśli główną obietnicą ma być porządek dawek.

### I. Review prompts i reklamy

05.08, 1★, „30 questions”, 14391146387: wiele pytań i prośba o ocenę przed właściwym doświadczeniem. 24.06, 1★, „Stop”, 14220503635 oraz 18.06, 5★, „Rate the app”, 14197699561: irytujące częste pytania o ocenę. Ostatnia recenzja zachowuje 5★ mimo skargi — kolejny powód, by nie klasyfikować tematu wyłącznie po rating.

02.06, 4★, „Everything I need in one app”, 14134896755: chwali tracking i zapas, ale uważa popupy promujące peptydy za irytujące. Nie dowodzi to bieżącej afiliacji. Aktualna odpowiedź w listingu dotyczącym food picks twierdzi, że są to wybory community, nie reklamy, i można je ukryć. Nie należy łączyć automatycznie starej skargi na peptydy z późniejszą funkcją jedzenia.

## Konkretne prośby i status

| Prośba | Evidence | Status na podstawie dostępnych źródeł |
|---|---|---|
| Ciemny profesjonalny styl | 30.09, 14611262385 | Classic look już ogłoszony w 4.0.3 |
| Powrót kalkulatora | wiele opinii 30.09–02.10 | Przywrócony 4.0.1; użytkownik potwierdza 04.10 |
| Widoczne jednostki | 02.10, 14618957158 i inne | Przywrócone 4.0.2 |
| Kalorie zamiast błonnika na Home | 03.10, 14624120008 | Developer potwierdza istniejący przełącznik |
| Fitbod / import treningów | 11.10, 14654140571 | Brak potwierdzenia bezpośredniej integracji Fitbod |
| Większa biblioteka informacji | 21.08, 14453082626 | Developer odnotował, bez dowodu realizacji całej prośby |
| IU i prawidłowe units per compound | 09.08 i 14.09 | Brak jednoznacznego potwierdzenia pełnego rozwiązania |
| Track workouts | 24.03, 13881791613 | Późniejsze recenzje wspominają workout tracking; nie jest nadal pewną luką |
| Zapis badań i brak duplikacji | 05.04, 13925534660 | Developer deklaruje naprawę |
| Łatwiejszy pierwszy setup | 02.09, 14499812358 i 14.09 | Brak pomiaru aktualnej łatwości |

## Prywatność jako hipoteza wyróżnienia

Polityka Pep AI mówi o zapisie danych zdrowotnych i danych z Apple Health/Health Connect w koncie; deklaruje brak sprzedaży danych zdrowotnych i brak ich udostępniania do targetowania reklam. Wymienia m.in. Firebase, RevenueCat, Anthropic, Gemini, Mixpanel, AppsFlyer, Meta, Stripe i Sentry jako dostawców. Nie należy wnioskować, że każdy otrzymuje wszystkie dane. [Privacy](https://pepaiapp.com/privacy).

Prywatność/offline może więc być różnicą architektoniczną, jeśli naprawdę ograniczymy serwery i zewnętrzne SDK. Ale w CSV nie ma silnej serii próśb o prywatność: to propozycja strategiczna, nie policzony priorytet tych użytkowników. Pewniejsze wsparcie mają kontrola nad danymi, eksport i niezawodny zapis.

## Rekomendacja dla naszej aplikacji

Najlepsza obietnica do testu: **„Twój plan i historia w kilka sekund. Czytelnie, stabilnie, bez zamieszania.”**

1. Widok „dziś”: jasne planowane/przyjęte/pominięte oraz szybki log.
2. Zapas związany z rzeczywistymi wpisami, z cofnięciem edycji i śladem zmian.
3. Czytelne jednostki i zachowanie oryginalnej ilości, bez cichej konwersji IU/units.
4. Offline, widoczne potwierdzenie zapisu, backup oraz eksport od początku.
5. Personalizacja modułów: prosta rutyna podstawowa, objawy/waga na życzenie, żywienie opcjonalne.
6. Krótki setup i pokazanie przykładowego produktu przed paywallem.
7. Wersjonowanie i stabilne skróty po update; testy migracji danych ważniejsze niż kolejne maskotki.
8. Ekran subskrypcji i anulowania z jednym źródłem prawdy o płatności.

Nie polegałbym na „dark mode + kalkulator” jako całej przewadze, bo Pep AI już naprawia te punkty. Nie zaczynałbym też od kopii żywienia, społeczności i AI. Zestaw funkcji all-in-one jest atutem Pep AI dla części użytkowników; nasza okazja to użytkownicy, którzy chcą mieć minimum potrzebnych działań i ufać historii.

Hipotezę trzeba zweryfikować rozmowami i pilotem. CSV daje bardzo dobry materiał do pytań: ile trwa wpis, co się dzieje po zmianie planu, jak rozpoznajesz związek wpisu i fiolki, czy chcesz zapisywać posiłki tutaj, co sprawiło że zrezygnowałeś. Nie daje dowodu, że określony odsetek użytkowników konkurenta przejdzie do nas.

## Audyt ręcznych kategorii

Poniższe listy są jawnie wybranymi recenzjami spełniającymi definicję; pozostałych kategorii nie kwantyfikuję. Nie sumować kategorii do 138.

- Redesign, negatywna reakcja (28): 14654199486, 14625335194, 14621306446, 14620865465, 14618957158, 14618931353, 14617913890, 14617060194, 14616434897, 14616327054, 14615988293, 14615971250, 14615939726, 14615441271, 14615140224, 14613587881, 14613571037, 14613520277, 14612874722, 14612276646, 14611928007, 14611572656, 14611572570, 14611262385, 14611088123, 14610859316, 14610379154, 14609540696.
- Zarzut utraty kalkulatora/konwersji/jednostek po redesignie (15): 14618957158, 14618931353, 14617060194, 14616434897, 14616327054, 14615988293, 14615939726, 14615140224, 14613520277, 14612874722, 14612276646, 14611572570, 14611088123, 14610379154, 14609540696.
- Dane/zapisy/logowanie (12): 14298998225, 14258769030, 14245799719, 14244668623, 14222540373, 14211525735, 14174281603, 14170201945, 14167941142, 14166213747, 14127541075, 13925534660.
- Billing/trial/rozpoznanie planu/anulowanie (10): 14653693854, 14589209864, 14549731895, 14517789045, 14330533679, 14271488420, 14249725504, 14184477474, 14173571965, 14115177426.
- Pep Bot/AI, skarga (7): 14615939726, 14611088123, 14603326812, 14145537614, 14091177830, 14047145234, 14042340667.

## Źródła do ponownego sprawdzenia

- https://apps.apple.com/us/app/pep-ai-peptide-glp-1-tracker/id6758682710
- https://pepaiapp.com/
- https://pepaiapp.com/peptide-tracker
- https://pepaiapp.com/peptide-cycle-tracker
- https://pepaiapp.com/glp-1-tracker-app
- https://pepaiapp.com/glp-1-food-tracker
- https://pepaiapp.com/about
- https://pepaiapp.com/privacy
- Oryginalny CSV użytkownika, 138 unikalnych review_id.
