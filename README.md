# Övning: Trunk based development

I denna övning ska du och en partner öva på arbetsflödet i trunk-based development. Det innebär att ni gör små förändringar i kortlivade brancher och integrerar dem snabbt till `main`, efter kodgranskning och verifiering.

## Förutsättningar

För att göra denna övning behöver du vara tillagd som collaborator på detta git repo.

## Uppgiften

Ni ska jobba två och två. Arbeta enligt trunk-based development och test-driven development (TDD) med feature flags.

1. Skapa en lokal branch från `main`.
1. En av er skriver ett test för den funktion ni blivit tilldelad i `main_test.py`, bakom feature-flaggan. Testet ska initialt misslyckas om funktionen ännu inte är implementerad.
1. Den andre av er granskar koden enligt checklistan (se nedan).
1. Gör rebase mot `main`, kör tester, och pusha er commiten till `main`.
1. Implementera funktionen bakom samma flagga.
1. Den andre av er granskar koden enligt checklistan (se nedan).
1. Gör rebase mot `main`, kör tester, och pusha er commiten till `main`.
1. Be ett annat team eller läraren om kodgranskning.
1. Efter godkännande: Ta bort feature-flaggan från både funktion och test.
1. Gör rebase mot `main`, kör tester, och pusha er commiten till `main`.

Syftet med flaggorna är att ni ska kunna arbeta iterativt och göra många små commits utan att påverka den gemensamma kodbasen förrän koden är granskad och godkänd.

## Checklista för kodgranskning

- Koden implementerar det som dokumentationen för funktionen beskriver.
- Koden är läsbar och begriplig.
- Kodrader som tar vtid att förstå har kommentar som hjälper läsaren att förstå.
- Bra namnval på funktioner och variabler.
- Inga onödiga eller överflödiga rader.

---

## Länkar

- Trunk based development (TBD): https://dora.dev/capabilities/trunk-based-development/
- Test driven development (TDD): https://martinfowler.com/bliki/TestDrivenDevelopment.html
- Feature flags: https://martinfowler.com/articles/feature-toggles.html
- Rebase: https://git-scm.com/book/en/v2/Git-Branching-Rebasing

Lycka till med övningen!