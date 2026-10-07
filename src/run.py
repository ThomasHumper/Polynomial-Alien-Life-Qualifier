pip install -e ".[dev]"
python examples/basic_example.py
pytest
julia --project=. examples/basic_example.jljulia --project=. -e 'using Pkg; Pkg.test()'
