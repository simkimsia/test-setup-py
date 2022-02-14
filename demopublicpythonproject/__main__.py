"""Entry point when invoked with python -m demopublicpythonproject."""  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    import sys

    from demopublicpythonproject.framework import main

    if sys.argv[0].endswith("__main__.py"):
        sys.argv[0] = "python -m demopublicpythonproject"
    main()
