pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'hangman')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)
conf.set('APP_ID', application_id)

configure_file(
  input: 'hangman.in',
  output: 'hangman',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

hangman_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(hangman_sources, install_dir: moduledir)
