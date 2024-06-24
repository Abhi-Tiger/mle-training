from setuptools import setup, find_packaages

setup(
    name="your_package",
    version="0.1",
    package=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[
	# list your dependencies here, e.g.,
	# "numoy>=1.18.0",
	# "pandas>=1.0.0"

    ],
    entry_points={
	'console_scripts': [
	#Define scripts to be installed as command-line tools
	'your-script=your_package.your_module:main_function'

	],
    },
    include_package_data=True,
    zip_safe=False,
)
