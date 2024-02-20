from setuptools import find_packages, setup

package_name = 'picar_pro'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/Car_launch.py']),
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
                'publisher = picar_pro.publisher:main',
                'servo_handler_car = picar_pro.servo_handler_car:main',
                'wheels_motor = picar_pro.wheels_motor:main',
                'car_arm_communication = picar_pro.car_arm_communication:main',
                'claw_motor_car = picar_pro.claw_motor_car:main',
        ],
    },
)
