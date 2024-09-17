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
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bill7',
    maintainer_email='gabiecarvalho15@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main", #informa ao ros que está criando um execuável para executar a funcao main
            "radiostation = my_py_pkg.radiostation:main",
            "radioreceiver = my_py_pkg.radioreceiver:main",
            "radiostationam = my_py_pkg.radiostationam:main",
            "radiostationfm = my_py_pkg.radiostationfm:main",
            "radio_do_interior_node = my_py_pkg.radio_do_interior_node:main",
            "radio_educadora_node = my_py_pkg.radio_educadora_node:main",
            "calculator_server = my_py_pkg.calculator_server:main",
            "calculator_client = my_py_pkg.calculator_client:main"


            
            # a cada nó é necessario colocar os executaveis aqui
            #do pacote X no caminho my_py_pkg , o X no main
        ],
    },
)
