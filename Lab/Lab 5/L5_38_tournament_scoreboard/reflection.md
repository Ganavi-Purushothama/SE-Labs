# Static analysis reflection

Ganavi Purushothama | PES2UG24CS167

## Easiest and hardest fixes

Whitespace was easy because Flake8 supplied exact locations and the fixes did not affect output. The roster warning needed more care. The function now creates a fresh list for default rosters and copies an explicitly supplied roster so later edits cannot affect another team.

## Findings that depended on context

Bandit B311 identifies a real use of ordinary pseudorandomness. The only use here was printing a demo toss, so the practical security impact was low. Replacing it with secrets.choice kept the two outcomes and cleared the finding.

## Integrating the tools into development

I would run Flake8 and Pylint while editing, then rerun all three tools in CI with pinned versions. Bandit findings would be reviewed by severity, and a small runtime check would confirm that standings and match totals still behave as expected.

## Improvements observed

Pylint increased from 4.75 to 10.00. Bandit went from four findings to zero, and Flake8 went from four violations to zero. The final demo printed the same standings and totals. The runtime checks also confirmed separate rosters and safe queries against an empty or single-team table.
