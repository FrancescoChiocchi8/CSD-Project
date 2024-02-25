from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        #Node(
        #    package='smart_arm',
        #    namespace='smart_arm',
        #    executable='publisher_node',
        #    name='main',
        #),
        Node(
            package='smart_arm',
            namespace='smart_arm',
            executable='comm_handler',
            name='main',
        ),
        Node(
            package='smart_arm',
            namespace='smart_arm',
            executable='arm_handler',
            name='main',
        ),
        Node(
            package='smart_arm',
            namespace='smart_arm',
            executable='servo_handler',
            name='main',
        ),
    ])