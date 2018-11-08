import setuptools

setup_requires = [
    'wheel',
]

install_requires = [
    'ansible-lint',
]

setuptools.setup(
    name='galaxy-lint-rules',
    author='Red Hat, Inc.',
    author_email='support@ansible.com',
    description='Ansible Lint rules used by Galaxy and Mazer '
                'to evaluate Ansible content',
    license='Apache-2.0',
    url='https://github.com/ansible/galaxy-lint-rules',

    setup_requires=setup_requires,
    install_requires=install_requires,
    packages=setuptools.find_packages(),
)
