## Running test / tests

You can run a single test, a set of tests or all tests. Tests can be run 
on one browser or multiple browsers. By default tests are run in a headless 
manner meaning no browser window will be opened while running the tests 
and results will be seen in the terminal. If you prefer you can run your 
tests in headed mode by using the `--headed` flag.

- Running tests on chromium

```
pytest
```

- Running a single test file

```
pytest test_login.py
```

- Running a set of test files

```
pytest tests/todo-page/ tests/landing-page/
```

- Running the test with a function name

```
pytest -k "test_add_a_todo_item"
```

- Running tests in headed mode

```
pytest --headed test_login.py
```

- Running tests on specific browsers

```
pytest test_login.py --browser webkit
```

- Running tests on multiple browsers

```
pytest test_login.py --browser webkit --browser firefox
```

- Running tests in parallel

```
pytest --numprocesses auto
```