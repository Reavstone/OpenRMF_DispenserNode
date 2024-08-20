from setuptools import find_packages, setup

package_name = 'dispenser_result_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maximilian Maritschnigg',
    maintainer_email='maximilian.maritschnigg@tdk.com',
    description='simulate dispenser result',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dispenser_result = dispenser_result_publisher.dispenser_result_publisher:main',
        ],
    },
)
