"""Comprueba referencias e imágenes del perfil: python3 scripts/check-profile.py."""

from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class ProfileImages(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            assert attrs.get('alt', '').strip(), 'Imagen sin texto alternativo'
        if tag in ('img', 'source'):
            source = attrs.get('src') or attrs.get('srcset')
            assert source, f'Imagen sin archivo: {tag}'
            if source.startswith('./'):
                path = ROOT / source
                assert path.is_file(), f'Archivo ausente: {source}'
                if path.suffix == '.svg':
                    root = ET.parse(path).getroot()
                    assert root.tag == '{http://www.w3.org/2000/svg}svg', source
                    assert not root.findall('.//{http://www.w3.org/2000/svg}script'), source
                else:
                    data = path.read_bytes()
                    assert path.suffix == '.jpg' and data.startswith(b'\xff\xd8\xff'), source
                    assert data.endswith(b'\xff\xd9'), f'JPEG incompleto: {source}'


if __name__ == '__main__':
    readme = (ROOT / 'README.md').read_text()
    ProfileImages().feed(readme)
    for component in ('stats', 'languages', 'streak', 'snake'):
        for theme in ('light', 'dark'):
            path = ROOT / f'assets/github-{component}-{theme}.svg'
            root = ET.parse(path).getroot()
            text = ''.join(root.itertext()).lower()
            for error in ('something went wrong', 'could not fetch', 'rate limit exceeded'):
                assert error not in text, f'Tarjeta con error: {path.name}'
    workflow = (ROOT / '.github/workflows/profile-cards.yml').read_text()
    for action in re.findall(r'uses: (\S+)', workflow):
        assert re.fullmatch(r'[^@]+@[0-9a-f]{40}', action), action
    print('Perfil válido: referencias completas, SVG y JPEG válidos, acciones fijadas por SHA.')
