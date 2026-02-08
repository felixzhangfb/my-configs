import re
import subprocess
from pathlib import Path
from typing import Literal, get_args

CONFIG = Literal[
    'console',
    'lab',
    'notebook',
    'server',
]
CONFIGS = get_args(CONFIG)


def extract_config(config: CONFIG):
    home_config_file = Path('~/.jupyter').expanduser() / f'jupyter_{config}_config.py'
    print(f'Extracting {config} config from {home_config_file}...')
    if not home_config_file.exists():
        cmd = ['jupyter', config, '--generate-config']
        subprocess.run(cmd, shell=False)
    with open(home_config_file) as f:
        content = f.read()

    pattern = re.compile(
        r'c\s=\sget_config\(\).*$'
        r'|\n#\s*-+\n#\s[A-Z].*\sconfiguration\n#\s*-+$'
        r'|^#\s{,1}c\.[A-Z].*\s=\s.*$'
        r'|^c\.[A-Z].*\s=\s.*$',
        flags=re.MULTILINE,
    )
    matches = pattern.findall(content)
    clean_content = '\n'.join(matches)
    clean_content = re.sub(r'#\s*noqa', '# type: ignore', clean_content)

    with open(Path('./full') / f'jupyter_{config}_config.py', 'w') as f:
        f.write(clean_content)


if __name__ == '__main__':
    for config in CONFIGS:
        print(f'Extracting {config} config...')
        extract_config(config)
