# Contributing

All are welcome to make Pull Requests to the repo, we ask that you follow these steps to make it easier for everybody to understand the request.

1. If you don't have direct access, make a fork of the repository.
2. Make branch for change
    - Preferably prefixed with the type of change, or present-tense verb
    - Some examples:
      - `feature/new-thing`
      - `fix/broken-thing`
      - `docs/fix-typo`
3. Attempt to run tests/linters
    - It's not required, but would be helpful
4. Add and commit changes
    - Preferably persent-tensed, and if you're referencing or closing an issue, include it at the end of your commit message:
      - `Close #0`
      - `Contribute to #0`
5. Push branch to GitHub
6. Make Pull Request from branch to master branch of this repository
7. Make any requested changes from reviewers - if any.

## Linting & Testing

For now, they are manually-ran commands.

Automation for these are coming soon - perhaps you could be the one to add them?

- [Unittest](https://docs.python.org/3/library/unittest.html) tests
  - `python3 -m unittest **/*_test.py`
- [Coverage.py](https://coverage.readthedocs.io) Tests
  - `coverage run --omit "**/*_test.py" -m unittest **/*_test.py`
  - `coverage report`
  - `coverage html`
- [pylint](https://www.pylint.org/) linting:
  - `python3 -m pylint --disable=mixed-indentation,line-too-long,too-many-ancestors --indent-string='\t' --indent-after-paren=1 --good-names='fg,bg' **/*.py`
