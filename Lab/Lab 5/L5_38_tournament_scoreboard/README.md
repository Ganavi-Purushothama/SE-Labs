# Sports Tournament Scoreboard

Ganavi Purushothama | PES2UG24CS167

[Assigned starter](https://github.com/SETAPESU26/L5_38_tournament_scoreboard) at commit c9ef096.

The final script comes from the [recovered personal repository](https://github.com/Ganavi-Purushothama/PES2UG24CS167_L5_38_tournament_scoreboard/tree/6afce6f7747184a9b1c9cfd9880a9bcb6f984072), with one blank line added to pass Flake8. The [six original reports](reports/recovered/) are preserved alongside the verified reruns.

| Tool | Before | After |
|---|---|---|
| Pylint | 4.75/10 | 10.00/10 |
| Bandit | 4 findings | 0 findings |
| Flake8 | 4 violations | 0 violations |

- [Issue table](issues.md)
- [Reflection](reflection.md)
- [Original code](submission%20reports/tournament_scoreboard_original.py)
- [Updated code](tournament_scoreboard.py)
- [Before reports](reports/before/)
- [After reports](reports/after/)
- [Runtime checks](reports/after/runtime_checks.txt)

The empty after Flake8 report is its raw successful output. Run these commands from this folder in an activated Python virtual environment.

```powershell
python -m pip install -r requirements-dev.txt
python tournament_scoreboard.py
python -m pylint tournament_scoreboard.py
python -m bandit -r tournament_scoreboard.py
python -m flake8 tournament_scoreboard.py
```
