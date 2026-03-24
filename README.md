# CI/CD

Projekt pokazuje mój sposób podejścia do automatyzacji CI/CD przy własnej aplikacji eksperymentalnej. 
Workflow został zaprojektowany i wdrożony przeze mnie, ze wsparciem AI przy tworzeniu szablonów i kroków pipeline. 
Wszystkie decyzje dotyczące budowy obrazów, testów i publikacji raportów były podejmowane przeze mnie.

## Co zrobiłem

- Opracowałem pełny **workflow CI/CD** z użyciem GitHub Actions, który:
  - buduje obraz Dockera z aplikacją,
  - uruchamia **unit testy**,
  - buduje obraz z testami **E2E**,
  - uruchamia testy i generuje raport,
  - publikuje raport na **GitHub Pages**.

> Uwaga: repo jest mocno “śmietnikowe”, ale pokazuje, jak eksperymentowałem z workflow i debugowałem problemy.
