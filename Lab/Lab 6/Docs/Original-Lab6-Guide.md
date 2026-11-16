# Lab 6: Elevator Dispatch

The application code is unchanged. Two additional test files exercise the
application's lines and decision branches.

## Verified results

| Suite | Tests passing | Application coverage |
| --- | ---: | --- |
| Original starter tests | 2 | 31% line; 25% combined line/branch |
| CodeCoverageTest_elevator_dispatch.py | 14 | 100% line (39/39 statements) |
| BranchCoverageTest_elevator_dispatch.py | 35 | 100% line and branch (39/39 statements, 28/28 branches) |

The branch-mode terminal `Cover` column combines statement and branch coverage.
The final suite covers every measured branch, with zero partial branches.
Coverage is evidence of execution; it does not prove correctness for all inputs.

## Understand the tests

- `next_direction`: keeps the current direction when there are requests ahead,
  reverses when only requests behind remain, and becomes idle when no other
  floor is requested. An idle car prefers requests above over requests below.
- `door_action`: emergency takes priority over overload, which takes priority
  over blockage. Exactly 630 kg is allowed; 631 kg triggers overload.
- `pick_elevator`: chooses the smallest distance plus a five-floor penalty for
  a busy car. A tie keeps the first car. An empty list returns `None`.
- Line tests execute all statements. Branch tests also check alternative
  decisions, precedence, equal scores, and boundaries.

## Capture your actual terminal screenshots

Open PowerShell in this repository folder. The local `.venv` already has the
required tools. On a new machine, first run `python -m venv .venv`, then
`.\.venv\Scripts\python.exe -m pip install pytest coverage`.

Run the line suite:

```powershell
cd lab6
..\.venv\Scripts\python.exe -m coverage run --data-file=.coverage.line --source=elevator_dispatch -m pytest CodeCoverageTest_elevator_dispatch.py
..\.venv\Scripts\python.exe -m coverage report --data-file=.coverage.line -m
```

Take a screenshot showing the passing tests and the 100% report. Save it in
`lab6/screenshots/code_coverage.png` (create the screenshots folder first).
Use a real terminal screenshot; no screenshots have been supplied here.

From `lab6`, make the first commit:

```powershell
git add CodeCoverageTest_elevator_dispatch.py screenshots/code_coverage.png
git commit -m "Add line coverage tests and result screenshot"
```

Then run the branch suite:

```powershell
..\.venv\Scripts\python.exe -m coverage run --branch --data-file=.coverage.branch --source=elevator_dispatch -m pytest BranchCoverageTest_elevator_dispatch.py
..\.venv\Scripts\python.exe -m coverage report --data-file=.coverage.branch -m
```

Take a screenshot showing passing tests, `Branch 28`, `BrPart 0`, and `100%`.
Save it as `lab6/screenshots/branch_coverage.png`.

From `lab6`, make the second commit:

```powershell
git add BranchCoverageTest_elevator_dispatch.py screenshots/branch_coverage.png ../.gitignore ../pytest.ini ../LAB6_GUIDE.md
git commit -m "Add branch coverage tests and result screenshot"
```

Submission status: the two test commits have been created and pushed to
`https://github.com/Ganavi-Purushothama/L6_L7_38_elevator_dispatch`.
The fork is `origin`, and the course repository is `upstream`.
Both actual terminal screenshots have been reviewed and saved in
`lab6/screenshots/code_coverage.png` and `lab6/screenshots/branch_coverage.png`.
They show 14 passing line tests and 35 passing branch tests, with 100% coverage.
The screenshot submission commit includes both files. The commands used from
the repository root are:

```powershell
git add lab6/screenshots/code_coverage.png lab6/screenshots/branch_coverage.png
git commit -m "Add code and branch coverage terminal screenshots"
git push
```

The two commit commands above describe the required stages and have already
been completed for the test files; do not repeat them. Check whether your
instructor expects a particular student identifier in test filenames (the
handout uses `xxxx`); rename the files if required and adjust the commands.

The handout requests screenshots only for results at or above 90%, separate
code and branch test files, and at least two commits. Do not submit baseline
screenshots. Keep the virtual environment and coverage data out of Git.

To run all tests from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pytest
```
