import re

f = open("textoMD.md")
outfile = open("saida.html", "w", encoding="utf-8")

def convert_headers(line):
    line = re.sub(r'^### (.+)$', r'<h3>\1</h3>', line)
    line = re.sub(r'^## (.+)$', r'<h2>\1</h2>', line)
    line = re.sub(r'^# (.+)$', r'<h1>\1</h1>', line)
    return line

def convert_bold(line):
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)

def convert_italic(line):
    return re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)

def convert_links(line):
    return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

def convert_images(line):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

def convert_list_items(line):
    return re.sub(r'^\d+\.\s+(.+)$', r'<li>\1</li>', line)

list_buffer = []
for line in f:
    line = line.rstrip()
    
    if re.match(r'^\d+\.\s+', line):
        list_buffer.append(convert_list_items(line))
    else:
        if list_buffer:
            outfile.write('<ol>\n' + '\n'.join(list_buffer) + '\n</ol>\n')
            list_buffer = []
        line = convert_headers(line)
        line = convert_bold(line)
        line = convert_italic(line)
        line = convert_links(line)
        line = convert_images(line)
        outfile.write(line + '\n')

if list_buffer:
    outfile.write('<ol>\n' + '\n'.join(list_buffer) + '\n</ol>\n')

f.close()
outfile.close()
