from setuptools import setup

package_name = 'good_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pratham',
    maintainer_email='test@example.com',
    description='Good ROS 2 package for checker testing',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'simple_publisher = good_package.simple_publisher:main',
        ],
    },
)

