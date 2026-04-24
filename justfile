src_dir := "src"

default:
    just --list

format:
    uv run ruff format {{src_dir}} tests

lint:
    uv run ruff check {{src_dir}} tests main.py --fix
    uv run ty check main.py
    uv run ty check {{src_dir}}
    uv run ty check tests

test:
    uv run pytest --verbose --color=yes --cov={{src_dir}} --exitfirst -n auto

run:
    uv run main.py
