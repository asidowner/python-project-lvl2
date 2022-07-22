# Install project
install:
	poetry install

# Run brain-games locally, work after install
gendiff:
	poetry run gendiff

# build project and make package on dist folder
build:
	poetry build

# Test publish project
publish:
	poetry publish --dry-run

# Install package
package-install:
	python3 -m pip install --user dist/*.whl

# Install package if use project venv
package-install-local-venv:
	python3 -m pip install dist/*.whl

# Remove package
package-remove:
	python3 -m pip uninstall hexlet-code

# Check lint by flake8, see setup.cfg
lint:
	poetry run flake8 gendiff