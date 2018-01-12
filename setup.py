from setuptools import setup

setup(
    name='another_neural_net',
    description='Packaged fully connected, multilayer neural network written in numpy with data_recipes for testing with sklearn datasets.',
    url='https://github.com/Ianphorsman/AnotherNeuralNetwork',
    author='Ian Horsman',
    author_email='ianphorsman@gmail.com',
    license='MIT',
    version='0.1',
    packages=['neural_net'],
    install_requires=['numpy', 'scikit-learn', 'seaborn']
)