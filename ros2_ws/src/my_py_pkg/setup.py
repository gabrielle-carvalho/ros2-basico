from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/CalcService.srv']),  # Adicionando o serviço
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabi',
    maintainer_email='gabiecarvalho15@gmail.com',
    description='Basic Calculator Service Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'terminal_node = my_py_pkg.terminal_node:main',  # Registrando o terminal node
            'basic_calculator = my_py_pkg.basic_calculator:main',  # Registrando o nó do serviço
        ],
    },
)
