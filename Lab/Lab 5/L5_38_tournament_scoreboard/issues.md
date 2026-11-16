# Static analysis findings

Ganavi Purushothama | PES2UG24CS167

Line numbers refer to the original assigned script at commit c9ef096.

| Issue | Type | Original lines | Description | Fix approach |
|---|---|---:|---|---|
| Bandit B605 | Security, high | 69–71 | The unused publishing helper passed an external destination into a shell command. | Removed the helper and shell dependency. |
| Bandit B306 | Security, medium | 64–66 | The unused temporary path helper selected a filename without creating it securely. | Replaced it with NamedTemporaryFile, which creates the file securely. The caller is responsible for removing it. |
| Bandit B105 | Security, low | 6 | An unused demo password was hardcoded. | Removed the constant. |
| Bandit B311 | Security, low | 60–61 | The demo toss used a generator unsuitable for security-sensitive randomness. | Used secrets.choice. |
| Pylint W0102 | Correctness | 11–13 | Teams could share the same default roster. | Use None as the default and give every team its own list. |
| Pylint R1714 | Simplification and robustness | 56–58 | Explicit indexes assume at least two teams. | Check membership in the first two entries using a slice. |
| Pylint C0103 and C0114/C0116 | Readability | 1, 11–74 | Names and missing docstrings made responsibilities less clear. | Use snake_case and add concise docstrings. |
| Flake8 E203/E302/E231/E261 | Style | 5, 60, 79, 87 | Spacing and blank lines were inconsistent. | Corrected spacing and broke long lines. |
