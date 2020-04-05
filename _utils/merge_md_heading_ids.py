#!/usr/bin/python3

import sys
import re
import subprocess



def get_yaml_front_matter(gfm_lines):
    counter = 0
    start = 0
    end = 0
    for i in range(len(gfm_lines)):
        if gfm_lines[i] == '---\n':
            counter += 1
            if counter == 1:
                start = i
            elif counter == 2:
                end = i + 1
                return gfm_lines[start:end], start, end
    if counter == 1:
        return gfm_lines[start:], start, len(gfm_lines)
    # case counter == 0:
    return [], 0, 0



def line_only_made_of(line, char):
    length = len(line)
    for i in range(length - 1):
        if line[i] != char:
            return False
    return line[length - 1] == '\n'



def render(gfm_lines):
    p = subprocess.run(['kramdown'], stdout=subprocess.PIPE, input=''.join(gfm_lines), encoding='utf8')
    if p.returncode != 0:
        return None
    return p.stdout.splitlines(1)



def look_for_headline(rendered_html_lines, headline_id):
    for l in range(len(rendered_html_lines)):
        x = re.search('<h\\d id="' + headline_id + '">', rendered_html_lines[l])
        if x is None:
            continue
        c = x.start()
        if c is None:
            continue
        else:
            return l, c
    return None



def extract_headline_id(rendered_html_lines, l, c):
    line = rendered_html_lines[l]
    line = line[c:]
    x = re.search('<h\\d id="', line)
    if x is None:
        return None
    col = x.start()
    if col is None:
        return None
    elif col > 0:
        return None
    line = line[8:]   # len('<h1 id="') == 8
    end = line.find('"')
    line = line[:end]
    return line



def try_create_id(gfm_lines, line_number, this_line, next_line, rendered_html_lines, placeholder):
    # save headline
    saved_headline = gfm_lines[line_number]

    hl = None

    if this_line.startswith('#'):
        # headline starting with '#'
        gfm_lines[line_number] = '# ' + placeholder + '\n'
        hl = look_for_headline(render(gfm_lines), placeholder)
    elif len(next_line) >= 3 and (line_only_made_of(next_line, '=') or line_only_made_of(next_line, '-')):
        # headline starting with '===' or '---'
        gfm_lines[line_number] = placeholder + '\n'
        hl = look_for_headline(render(gfm_lines), placeholder)

    # revert headline
    gfm_lines[line_number] = saved_headline

    if hl is None:
        return None

    hl_line, hl_col = hl
    return extract_headline_id(rendered_html_lines, hl_line, hl_col)



def generate_unique_placeholder(rendered_html_lines):
    number = 0
    PREFIX = 'xq'
    SUFFIX = 'z'
    while True:
        solution_found = True
        for line in rendered_html_lines:
            x = re.search('id\\s*=\\s*"' + PREFIX + str(number) + SUFFIX + '"', line)
            if x is None:
                continue
            else:
                number += 1
                solution_found = False
                break
        if solution_found:
            break
    # we assume that there will be at least one solution
    return PREFIX + str(number) + SUFFIX



def create_line_to_id_map(gfm_lines):
    result = {}
    gfm_lines2 = gfm_lines[:]
    rendered_html_lines = render(gfm_lines)

    placeholder = generate_unique_placeholder(rendered_html_lines)

    # line-by-line: assume a headline
    n = len(gfm_lines2)
    for i in range(n):
        this_line = gfm_lines2[i]
        next_line = ''
        if i < n - 1:
            next_line = gfm_lines2[i + 1]
        hid = try_create_id(gfm_lines2, i, this_line, next_line, rendered_html_lines, placeholder)
        if hid is not None:
            result[i] = hid

    return result



def insert_ids_to_gfm_file(line_to_id_map, gfm_lines):
    result = gfm_lines[:]
    for key, value in line_to_id_map.items():
        str_to_insert = '<a id="' + value + '"></a>'
        line = result[key]
        if line.startswith('#'):
            result[key + 1] = str_to_insert + result[key + 1]
        else:
            result[key + 2] = str_to_insert + result[key + 2]
    return result



def merge_ids_in_gfm_files(orig_gfm_lines, trl_gfm_lines):
    # assuming that both files match line by line such that matching headlines are in the same lines

    # get yaml front matter from orig
    orig_yaml_front_matter, orig_start, orig_end = get_yaml_front_matter(orig_gfm_lines)

    # get yaml front matter from trl
    trl_yaml_front_matter, trl_start, trl_end = get_yaml_front_matter(trl_gfm_lines)

    # get body from trl
    trl_body = trl_gfm_lines[trl_end:]

    # get body from orig
    orig_body = orig_gfm_lines[orig_end:]

    # create line-to-id map
    orig_line_to_id_map = create_line_to_id_map(orig_body)

    # insert ids
    preresult = insert_ids_to_gfm_file(orig_line_to_id_map, trl_body)

    # create translated document with adapted body
    result_trl_gfm = ''.join(trl_yaml_front_matter) + ''.join(preresult)

    return result_trl_gfm



def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    # read original file
    orig_gfm_lines = []
    with open(sys.argv[1], 'r') as file:
        orig_gfm_lines = file.readlines()

    # read translated file
    trl_gfm_lines = []
    with open(sys.argv[2], 'r') as file:
        trl_gfm_lines = file.readlines()

    # merge ids in gfm files
    result = merge_ids_in_gfm_files(orig_gfm_lines, trl_gfm_lines)

    # print result
    print(result, end='')



if __name__ == '__main__':
    main()

