import os


def _gen_setup_file(project_name):
    content = """\
from setuptools import setup, find_packages

setup(
    name='%s',
    description='App description.',
    version='1.0',
    packages=find_packages(),
    # package_data={'package': ['subfolder/*']},
    # install_requires=[
    #     'numpy',
    #     'Pillow'
    # ],
    # entry_points='''
    #     [console_scripts]
    #     cmd=package.module:cmd_fun
    # '''
)
""" % project_name
    return content


def _gen_main_module():
    content = """\


def hello():
    print('Hello world')


if __name__ == '__main__':
    hello()

"""
    return content


def make_project(project_name):
    pth = os.path.join(os.getcwd(), project_name, project_name)
    print(str(pth))
    os.makedirs(pth)
    setup_content = _gen_setup_file(project_name)
    with open(os.path.join(project_name, 'setup.py'), 'w') as f:
        f.write(setup_content)

    src_content = _gen_main_module()
    with open(os.path.join(project_name, project_name, '%s.py' % project_name), 'w') as f:
        f.write(src_content)
