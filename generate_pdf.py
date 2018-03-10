#!/usr/bin/python
import subprocess
import os
code_dir = "code"
title = "Liyun Dai Notebook"
        

def get_sections(filename1):
    
    sections = []
    section_name = None
    with open(filename1, 'r') as f:
        for line in f:
            if '#' in line: line = line[:line.find('#')]
            line = line.strip()
            if len(line) == 0: continue
            if line[0] == '[':
                section_name = line[1:-1]
                subsections = []
                if section_name is not None:
                    sections.append((section_name, subsections))
            else:
                tmp = line.split(':', 1)
                if len(tmp) == 1:
                    raise ValueError('Subsection parse error: %s' % line)
                filename = tmp[0]
                filename.replace(" ","")
                subsection_name = tmp[1]
                if subsection_name is None:
                    raise ValueError('Subsection given without section')
                subsections.append((filename, subsection_name))
    return sections


def get_style(filename):
    filename= filename.strip()
    ext = filename.lower().split('.')[-1]
    if ext in ['c', 'cc', 'cpp', 'h', 'hpp']:
        return 'cpp'
    elif ext in ['java']:
        return 'java'
    elif ext in ['py']:
        return 'py'
    elif ext in ['sh']:
        return 'sh'
    elif ext in ['tex']:
        return 'tex'
    else:
        return 'txt'

# TODO: check if this is everything we need
def texify(s):
    #s = s.replace('\'', '\\\'')
    #s = s.replace('\"', '\\\"')
    return s

def get_tex(sections):
    tex = ''
    for (section_name, subsections) in sections:
        tex += '\\subsection{%s}\n' % texify(section_name)
        for (filename, subsection_name) in subsections:
            tex += '\\subsubsection{%s}\n' % texify(subsection_name)
            tex += '\\raggedbottom\\lstinputlisting[style=%s]{%s/%s}\n' % (get_style(filename), code_dir, filename)
            tex += '\\hrulefill\n'
        tex += '\n'
    return tex


def get_allConttent():
    allContent=''
    fileList=os.listdir("contents")
    fileList.sort()
    preNum=0
    for filename in fileList:
        if 'note' == filename[0:4]:
            d=filename[4:14]

            filename="contents/"+filename
            
            b=os.path.getsize(filename)


            if b > 0:
                preNum=preNum+1
                sections = get_sections(filename)
                tex = get_tex(sections)
                allContent+='\\section{%s}\n' % texify(d)
                allContent+=tex
    tempNum=0
    for filename in fileList:
        if 'note' == filename[0:4]:
            d=filename[4:14]

            filename="contents/"+filename
            
            b=os.path.getsize(filename)

            if b > 0:
                tempNum=tempNum+1
            else:
                os.remove(filename)
            if tempNum>=preNum:
                break

    return allContent
if __name__ == "__main__":
    tex=get_allConttent()
    # sections = get_sections()
    # tex = get_tex(sections)

    with open('contents.tex', 'w') as f:
        f.write(tex)
    latexmk_options = ["latexmk", "-pdf", "notebook.tex"]
    subprocess.call(latexmk_options)
    os.system("git add  code/* ")
    os.system('git commit -a -m "oK"')
    os.system('git push')
