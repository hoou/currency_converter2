import coverage as coverage
import pytest
from flask.cli import FlaskGroup

from project import create_app

cov = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py'
    ]
)
cov.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def test():
    return pytest.main(['project/tests'])


@cli.command()
def coverage():
    result = pytest.main(['project/tests'])
    if result == 0:
        cov.stop()
        cov.save()
        print('Coverage Summary:')
        cov.report()
        cov.html_report()
        cov.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
