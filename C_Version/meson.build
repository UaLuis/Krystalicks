project(
  'C_Version',
  'c',
  meson_version : '>= 1.3.0',
  version : '0.1',
  default_options : ['warning_level=3'],
)

dependencies = [
]

sources = [
  'c_version.c',
]

exe = executable(
  'C_Version',
  sources,
  dependencies : dependencies,
  install : false,
)

test('basic', exe)
