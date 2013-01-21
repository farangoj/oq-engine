from setuptools import setup, find_packages

version = "0.9.0"
url = "http://openquake.org/"

README = """
OpenQuake is an open source application that allows users to
compute seismic hazard and seismic risk of earthquakes on a global scale.

Please note: the /usr/bin/openquake script requires a celeryconfig.py
file in the PYTHONPATH.  Please make sure this is the case and that your
celeryconfig.py file works with your python-celery setup.

Feel free to copy /usr/openquake/celeryconfig.py and revise it as needed.
"""

PY_MODULES = ['openquake.bin.cache_gc', 'openquake.bin.oqscript']

setup(
    entry_points={
        "console_scripts": [
            "openquake = openquake.bin.oqscript:main",
            "oq_cache_gc = openquake.bin.cache_gc:main",
            "oq_monitor = openquake.bin.openquake_supervisor:main",
            ]},
    name="openquake",
    version=version,
    author="The OpenQuake team",
    author_email="devops@openquake.org",
    description=("Computes hazard, risk and socio-economic impact of "
                 "earthquakes."),
    license="AGPL3",
    keywords="earthquake seismic hazard risk",
    url=url,
    long_description=README,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        ],
    packages=find_packages(exclude=["qa_tests", "qa_tests.*",
                                    "tools", "tests", "tests.*",
                                    "openquake.bin",
                                    "openquake.bin.*"]),
    py_modules=PY_MODULES,

    include_package_data=True,
    package_data={"openquake": [
            "db/schema/*", "openquake.cfg", "README", "LICENSE"]},
    exclude_package_data={"": ["bin/oqpath.py", "bin/oq_check_monitors",
                               "bin/oq_log_sink"]},
    scripts=["openquake/bin/oq_create_db", "openquake/bin/oq_restart_workers"]
    )