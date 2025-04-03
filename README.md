# Niezawodność i diagnostyka układów cyfrowych

## Opis

Projekt jest prostą symulacją sklepu. Symulacja ma odpowiedzieć na pytanie:
Czy w danym sklepie opłaca się postawić kasę samoobsługową czy może zatrudnić więcej pracowników? Wykonawcy Krzysztof Zalewa, Jakub Maciocha, ...

1. Losuje sklep ( Ilość pracowników, Ilość kas normalnych i samoobsługowych,
liczba pracowników na zmianie)
2. Zmiana 1 6:00 – 14:00, Zmiana 2 14:00 – 22:00
3. Godziny otwarcia są stałe 6:00 - 22:00 pn-sob
4. Wciągu dnia do sklepu przychodzą ludzie (krzywa gaussa przesunięta tak by
najwyższy punkt wypadał ~15)
5. Pracownik przy kasie może obsłużyć ~3 os/min kasa samoobsługowa ~4 os/min
6. Pracownik zarabia 3262 zł/mies kasa kosztuje 50000zł
7. Klienci podchodzą do kasy co 5min (losowanie grupy klientów z gaussa)
8. Każdy klient robi losowe zakupy (może przynieść x zł zysku)
9. Klient czekający w kolejce ponad 30min wychodzi ze sklepu bez zakupów
10. W zależności od średniego czasu oczekiwania może zostać otwarta dodatkowa
kasa
11. Pod koniec dnia liczony jest zysk i potencjalny zysk

## Obsługa

1. Aby program uruchomił się poprawnie należy użyć pliku main.py
2. Po uruchomieniu wydrukowane zostanie menu pozwalające na uruchomienie symulacji
3. Po wybraniu symulacji można użyć opcji zapisanych( można je zmienić ) lub zupełnie losowych
4. Długość symulacji podawana jest w dniach
5. W konoli zostają wydrukowane statystki symulacji (Można je zapisać lub zwizualizować)
