compile:
	python3 setup.py bdist_wheel

install:
	python3 -m pip install --force-reinstall dist/gvpp-1.1.1-py3-none-any.whl

upload-pip:
	python3 -m twine upload -r pypi dist/*
