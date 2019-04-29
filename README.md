# Django Test-Driven Development (TDD)

## Why test-driven development?

When creating a new application, at first you may not need tests. Tests can be difficult to write at first and they take time, but they can save an enormous amount of manual troubleshooting time.

As your application grows, it becomes more difficult to grow and to refactor your code. There’s always the risk that a change in one part of your application will break another part. A good collection of automated tests that go along with an application can verify that changes you make to one part of the software do not break another.


## Installing requirements

	$ pip install -r requirements.txt

## How to perform TDD Test 

Following steps define how to perform TDD test:

	1. Add a test.
	2. Run all tests and see if any new test fails.
	3. Write some code.
	4. Run tests and Refactor code.
	5. Repeat.	


## TDD cycle defines

	* Write a test.
	* Make it run.
	* Change the code to make it right i.e. Refactor.
	* Repeat process.	


#### Some clarifications about TDD:

	* TDD is neither about "Testing" nor about "Design".
	* TDD does not mean "write some of the tests, then build a system that passes the tests.
	* TDD does not mean "do lots of Testing."

![TDD cycle window](https://github.com/vickymax/django-test-driven-development/blob/master/TestDrivenDevelopment.png)


### Let’s first create a test demonstrating the behavior we’d like to see.

**_All the tests for app is written in the_** `blog/tests.py`.

### Now run the tests using:

	$ python manage.py test blog

#### sample of failed & passed test :

 Failed test :
~~~
Creating test database for alias 'default'...
...EEE....
======================================================================
ERROR: test_basic_view (blog.tests.EntryViewTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
django.template.base.TemplateDoesNotExist: blog/entry_detail.html

======================================================================
ERROR: test_body_in_entry (blog.tests.EntryViewTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
django.template.base.TemplateDoesNotExist: blog/entry_detail.html

======================================================================
ERROR: test_title_in_entry (blog.tests.EntryViewTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  ...
django.template.base.TemplateDoesNotExist: blog/entry_detail.html

----------------------------------------------------------------------
Ran 10 tests in 0.136s

FAILED (errors=3)
Destroying test database for alias 'default'...
~~~

Passed test : 
~~~
Creating test database for alias 'default'...
..........
----------------------------------------------------------------------
Ran 10 tests in 0.139s

OK
Destroying test database for alias 'default'...
~~~

## Test Coverage

It’s important to test all your code. Code coverage is frequently used as a measuring stick for a developer’s success in creating quality tests. The basic rule of thumb is comprehensive tests should execute every line of code.

[Coverage](https://coverage.readthedocs.io/en/latest/), a tool that measures code coverage for Python code, will be used to check what percentage of the code is being tested.


### Installing & usage of Coverage :

	$ pip install coverage


Now let’s run our tests. As we run our tests from the command line, `coverage` records and creates a coverage report:

	$ coverage run --include='./*' manage.py test

output : 
~~~
Creating test database for alias 'default'...
....................
----------------------------------------------------------------------
Ran 20 tests in 0.163s

OK
Destroying test database for alias 'default'...
~~~

Let’s take a look at our code coverage report:

~~~
$ coverage report
Name                                      Stmts   Miss  Cover
-------------------------------------------------------------
blog/__init__                                 0      0   100%
blog/admin                                    4      0   100%
blog/forms                                   14      0   100%
blog/migrations/0001_initial                  6      0   100%
blog/migrations/0002_auto_20141019_0232       5      0   100%
blog/migrations/__init__                      0      0   100%
blog/models                                  23      0   100%
blog/tests                                  101      0   100%
blog/urls                                     3      0   100%
blog/views                                   18      0   100%
manage                                        6      0   100%
tdd_django/__init__                           0      0   100%
tdd_django/settings                           19     0   100%
tdd_django/urls                                5     0   100%
tdd_django/views                               5     0   100%
-------------------------------------------------------------
TOTAL                                       209      0   100%
~~~

HTML Coverage Report:

	$ coverage html

This command will create a `htmlcov` directory containing our test coverage. The `index.html` is the overview file which links to the other files. Let’s open up our `htmlcov/index.html` in our web browser.


## APP structure

~~~
 django-test-driven-development/
 |-- tdd_django/
 |    |-- blog/
 |    |    |-- migrations/
 |    |    |-- __init__.py
 |    |    |-- admin.py
 |    |    |-- apps.py
 |    |    |-- models.py
 |    |    |-- tasks.py
 |    |    |-- tests.py
 |    |    |-- urls.py
 |    |    +-- views.py
 |    |-- __init__.py
 |    |-- settings.py
 |    |-- urls.py
 |    +-- wsgi.py
 |-- static/
 |-- tddvenv/
 |-- templates/
 |-- .gitignore
 |-- db.sqlite3
 |-- manage.py
 |-- README.md
 +-- requirements.txt
 +-- TestDrivenDevelopment.png

~~~

## Still look wrong? 

Contact the developer and tell me what you tried to do that didn’t work.

- [Reporting an issue](https://github.com/vickymax/django-test-driven-development/issues/new).