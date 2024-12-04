import pathlib
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.ci != "circleci" %}.circleci{% endif %}',
    '{% if cookiecutter.ci != "github" %}.github{% endif %}',
]

for path in REMOVE_PATHS:
    if path:
        path = pathlib.Path(path)
    else:
        continue

    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
