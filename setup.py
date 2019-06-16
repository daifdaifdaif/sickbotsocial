from setuptools import setup


import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] 
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

with open("README.md", 'r') as f:
    long_description = f.read()



setup(name='sickbotsocial',
      version='0.1',
      description='Jessica Jurassica Bot',
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='textgeneration jessicajurassica dieyungenhurendothiv markov',
      url='https://github.com/daifdaifdaif/sickbotsocial',
      author='DAIF',
      author_email='daif@dieyungenhuren.hiv',
      license='MIT',
      packages = ['sickbotsocial'],
      install_requires=install_requires,
      include_package_data=True,
      zip_safe=False)
    
old_name = os.path.join(thelibFolder, "sickbotsocial/config-example.py")
new_name = os.path.join(thelibFolder, "sickbotsocial/config.py")  
os.rename(old_name, new_name)
open("printed.txt", 'a').close()
