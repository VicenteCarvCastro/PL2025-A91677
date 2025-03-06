import re

token_specification = [
    ('KEYWORD', r'\b(select|where|LIMIT)\b', re.IGNORECASE),
    ('VARIABLE', r'\?[a-zA-Z_][a-zA-Z0-9_]*'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*\b|\ba\b'),
    ('STRING', r'".*?"(@[a-zA-Z]+)?'),
    ('NUMBER', r'\b\d+\b'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('DOT', r'\.'),
    ('WHITESPACE', r'\s+', re.MULTILINE),
    ('MISMATCH', r'.')
]

def lexer(code):
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern, *_ in token_specification)
    pattern = re.compile(token_regex, re.MULTILINE)
    
    tokens = []
    for match in pattern.finditer(code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'WHITESPACE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    return tokens

# Exemplo de uso
query = """
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
"""

for token in lexer(query):
    print(token)
