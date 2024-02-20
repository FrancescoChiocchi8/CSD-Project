from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='publisher',
            name='main',
        ),  
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='servo_handler_car',
            name='main',
        ),  
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='wheels_motor',
            name='main',
        ),
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='car_arm_communication',
            name='main',
        ),
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='claw_motor_car',
            name='main',
        ),
 ])