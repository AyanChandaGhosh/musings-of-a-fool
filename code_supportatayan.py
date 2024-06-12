def get_executable_and_file(lang, code) -> Tuple(str, str):
    assert code
    FILE = "temp.script"
    open(FILE, 'w').write(code)
    if lang == 'python':
        return "python", FILE
    elif lang == 'r':
        return "Rscript", FILE
    else:
        pass
