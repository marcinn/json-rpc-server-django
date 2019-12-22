.DEFAULT_GOAL = install
.PHONY = install

env:
	python -m venv env

install: env
	source env/bin/activate && pip install -U pip
	source env/bin/activate && pip install .[dev]

package:
	@rm -rf dist/
	@mkdir dist
	@source env/bin/activate && python -m build


upload: package
	source env/bin/activate && twine upload dist/*


