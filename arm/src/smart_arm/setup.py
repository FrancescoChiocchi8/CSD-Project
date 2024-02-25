from setuptools import find_packages, setup

package_name = 'smart_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/smart_arm.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='csd',
    maintainer_email='csd@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = smart_arm.publisher_node:main',
            'comm_handler = smart_arm.comm_handler:main',
            'arm_handler = smart_arm.arm_handler:main',
            'servo_handler = smart_arm.servo_handler:main',
        ],
    },
)
