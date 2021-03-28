"""Constants used by AnsibleLint."""
import os.path
import sys

# mypy/pylint idiom for py36-py38 compatibility
# https://github.com/python/typeshed/issues/3500#issuecomment-560958608
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal

DEFAULT_RULESDIR = os.path.join(os.path.dirname(__file__), 'rules')
CUSTOM_RULESDIR_ENVVAR = "ANSIBLE_LINT_CUSTOM_RULESDIR"

INVALID_CONFIG_RC = 2
ANSIBLE_FAILURE_RC = 3
ANSIBLE_MISSING_RC = 4
INVALID_PREREQUISITES_RC = 10
EXIT_CONTROL_C_RC = 130

# Minimal version of Ansible we support for runtime
ANSIBLE_MIN_VERSION = "2.9"

# Based on https://docs.ansible.com/ansible/latest/reference_appendices/config.html
ANSIBLE_DEFAULT_ROLES_PATH = (
    "~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles"
)

ANSIBLE_MOCKED_MODULE = """\
# This is a mocked Ansible module generated by ansible-lint
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
module: {name}

short_description: Mocked
version_added: "1.0.0"
description: Mocked

author:
    - ansible-lint (@nobody)
'''
EXAMPLES = '''mocked'''
RETURN = '''mocked'''


def main():
    result = dict(
        changed=False,
        original_message='',
        message='')

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
"""

FileType = Literal[
    "playbook",
    "meta",  # role meta
    "tasks",  # includes pre_tasks, post_tasks
    "handlers",  # very similar to tasks but with some specificts
    # https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-roles-and-collections-from-the-same-requirements-yml-file
    "requirements",
    "role",  # that is a folder!
    "yaml",  # generic yaml file, previously reported as unknown file type
    "",  # unknown file type
]


# odict is the base class used to represent data model of Ansible
# playbooks and tasks.
odict = dict
if sys.version_info[:2] < (3, 7):
    try:
        # pylint: disable=unused-import
        from collections import OrderedDict as odict  # noqa: 401
    except ImportError:
        pass

# Deprecated tags/ids and their newer names
RENAMED_TAGS = {
    '102': 'no-jinja-when',
    '104': 'deprecated-bare-vars',
    '105': 'deprecated-module',
    '106': 'role-name',
    '202': 'risky-octal',
    '203': 'no-tabs',
    '205': 'playbook-extension',
    '206': 'var-spacing',
    '207': 'no-jinja-nesting',
    '208': 'risky-file-permissions',
    '301': 'no-changed-when',
    '302': 'deprecated-command-syntax',
    '303': 'command-instead-of-module',
    '304': 'inline-env-var',
    '305': 'command-instead-of-shell',
    '306': 'risky-shell-pipe',
    '401': 'git-latest',
    '402': 'hg-latest',
    '403': 'package-latest',
    '404': 'no-relative-paths',
    '501': 'partial-become',
    '502': 'unnamed-task',
    '503': 'no-handler',
    '504': 'deprecated-local-action',
    '505': 'missing-import',
    '601': 'literal-compare',
    '602': 'empty-string-compare',
    '701': 'meta-no-info',
    '702': 'meta-no-tags',
    '703': 'meta-incorrect',
    '704': 'meta-video-links',
    '911': 'syntax-check',
}
