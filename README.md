# Automatizované testy REST API

Tento repozitár obsahuje sadu automatizovaných testov pre REST API, ktoré sú implementované pomocou jazyka Python a knižnice requests.

## Inštalácia

1. Klonujte tento repozitár na svoj lokálny počítač.
2. Uistite sa, že máte nainštalovaný Python na vašom počítači.
3. Nainštalujte knižnicu requests pomocou pip:
pip install requests
pip install jsonschema


## Spustenie testov

Pre spustenie testov použite nasledujúce príkazy z príkazového riadku:

1. Testovanie - Test Case 1 - Get - List users:
python test_list_users.py

2. Testovanie Test Case 1 - Get - List users (bonus):
python test_list_users_assertions.py

3. Testovanie - Test Case 2 - Post - Create:
python test_create.py

4. Testovanie - Test Case 2 - Post - Create (bonus):
python test_create_verify.py

## Prispievanie

Ak chcete prispieť k tomuto projektu, prosím vytvorte vetvu (branch) pre vašu prácu, implementujte vaše zmeny a pošlite pull request.

## Licence

Tento projekt je licencovaný pod MIT licenciou. Pre viac informácií si prečítajte súbor [LICENSE](LICENSE).
