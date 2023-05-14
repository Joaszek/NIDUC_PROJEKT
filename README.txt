CRC (Cyclic Redundancy Check) to technika detekcji błędów w przesyłanych danych.
Polega ona na obliczeniu wartości sumy kontrolnej (CRC) dla danych przed ich wysłaniem, a następnie przesłaniu danych i wartości CRC do odbiorcy.
Odbiorca dokonuje obliczenia wartości CRC dla otrzymanych danych i porównuje ją z otrzymaną wartością CRC. Jeśli wartości są identyczne, to dane uznaje się za poprawnie przesłane.
W przeciwnym przypadku uznaje się, że wystąpił błąd w transmisji danych.

CRC jest obliczana poprzez dzielenie przesyłanych danych przez ustalony wcześniej wielomian, a następnie uzyskanie reszty z dzielenia.
Wartość CRC jest dodawana na końcu przesyłanych danych jako dodatkowe bity kontrolne.
Odbiorca dokonuje tego samego obliczenia i porównuje wynik z przesłaną wartością CRC, aby stwierdzić, czy dane zostały przesłane poprawnie.

CRC jest popularną techniką detekcji błędów w przesyłanych danych, ponieważ jest prosta w implementacji,
szybka w działaniu i efektywna w wykrywaniu różnego rodzaju błędów, takich jak pojedyncze bity, transpozycje, zamiany kolejności bitów itp.
CRC jest również często stosowana w połączeniu z techniką ARQ, aby zapewnić bezpieczną transmisję danych przez sieć.