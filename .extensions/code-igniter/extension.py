"""Code Igniter Extension

Downloads, installs and configures Code Igniter
"""
import logging


_log = logging.getLogger('codeigniter')


DEFAULTS = utils.FormattedDict({
    'CODEIGNITER_VERSION': '2.1.4',
    'CODEIGNITER_PACKAGE': 'CodeIgniter_{CODEIGNITER_VERSION}.zip',
    'CODEIGNITER_HASH': '28abc67cfec406c74cb8c64499f1fafb92c6840e',
    'CODEIGNITER_URL': 'http://ellislab.com/asset/ci_download_files'
                       '/CodeIgniter_2.1.3.zip'
})


# Extension Methods
def preprocess_commands(ctx):
    return ()


def service_commands(ctx):
    return {}


def service_environment(ctx):
    return {}


def compile(install):
    print 'Installing Code Igniter %s' % DEFAULTS['CODEIGNITER_VERSION']
    ctx = install.builder._ctx
    inst = install._installer
    workDir = os.path.join(ctx['TMPDIR'], 'code-igniter')
    inst.install_binary_direct(
        DEFAULTS['CODEIGNITER_URL'],
        DEFAULTS['CODEIGNITER_HASH'],
        workDir,
        fileName=DEFAULTS['CODEIGNITER_PACKAGE'],
        strip=True)
    (install.builder
        .move()
        .everything()
        .under(os.path.join(workDir, 'system'))
        .into('BUILD_DIR')
        .done())
    (install.builder
        .move()
        .everything()
        .under(os.path.join(workDir, 'application'))
        .into('BUILD_DIR')
        .done())
    (install.builder
        .move()
        .where_name_is('index.php')
        .under(workDir)
        .into('{BUILD_DIR}/htdocs')
        .done())
    return 0
