run:
	python manage.py runserver
format:
	isort .
	black .
	autopep8 --in-place --recursive .
lint:
	flake8 .
	pylint $(find . -name "*.py")
type-check:
	mypy .
	bandit -r .
test:
	pytest
test-matching:
	pytest -s -rx -k $(K) --pdb ./tests/
startproject:
	django-admin startproject $(K)
startapp:
	python manage.py startapp $(K)
migrate:
	python manage.py migrate
migrate_version:
	python manage.py migrate $(K) $(N)
makemigrations:
	python manage.py makemigrations $(K)
makemigrations_full:
	python manage.py makemigrations
sqlmigrate:
	python manage.py sqlmigrate $(K) $(N)
shell:
	python manage.py shell
add_dev:
	poetry add '$(K)=*' --group dev
add:
	poetry add '$(K)=*'
shell_i:
	python manage.py shell -i ipython
shell_plus:
	python manage.py shell_plus
createsuperuser:
	python manage.py createsuperuser
run_gunicorn:
	poetry run gunicorn mysite.wsgi:application