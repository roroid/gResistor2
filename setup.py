from distutils.core import setup
setup(name='gresistor2',
      version='0.0.1',
      description      = 'Aici intra descrierea',
      author           = 'Pop Gheorghe',
      author_email     = 'pop.gheorghe@rgmail.com',
      url              = 'http://www.roroid.ro',
      license          = 'GPL',
      scripts=['gresistor2'],
      data_files = [('share/applications',
                       ['gresistor2.desktop']),('share/gresistor2',
                       ['icon.png'])],
      )
