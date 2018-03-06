from setuptools import setup, find_packages

setup(
    name='sampledb',
    version='0.1.1',
    packages=find_packages(),
    package_data={'sampledb': ['*.xsh']},
    entry_points={
        'console_scripts': [
            'publish_samples=sampledb.reader:publish_samples',
            'download_samples=sampledb.reader:download_samples',
            'clean=sampledb.generate_qr:clean',
        ],
    },
    description='database search and publish',
    zip_safe=False,
)
