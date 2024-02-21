from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='picar_handler',
            name='main',
        ),
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='analysis_handler',
            name='main',
        ),  
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='camera_handler',
            name='main',
        ),  
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='comm_handler',
            name='main',
        ),
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='servo_handler',
            name='main',
        ),
        Node(
            package='picar_pro',
            namespace='smart_car',
            executable='wheels_handler',
            name='main',
        ),
 ])