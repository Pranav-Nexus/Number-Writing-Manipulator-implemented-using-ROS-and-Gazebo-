from setuptools import setup

package_name = 'cougerbot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jettysowmith',
    maintainer_email='jettysowmith@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'spawn_cougerbot=cougerbot.cougerbot_spawn_client:main',
        'bot_node=cougerbot.beta:main'
        ],
    },
)
