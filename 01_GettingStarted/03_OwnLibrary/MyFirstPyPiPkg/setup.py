from setuptools import setup, find_packages

setup(
    name="pip-pkg-demo",
    version="1.0.0",
    author="Thong Hua",
    author_email="some_dummy@email.com",
    description="A demo pip package for gitlab ci",
    license="MIT",
    packages=find_packages(),
    classifiers=["Python 3.9", "Gitlab Demo", "Cross Platform"],
    python_requires='>=3.5',
    entry_points={
    'console_scripts': [
        'start-example=MicroserviceBase.ServiceRegistry.main:main',
    ]
)