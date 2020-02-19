#!/usr/bin/python3

import sys
import yaml



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



def adapt_path(path, langcode):

    # assuming that `path` starts with a `/`
    if path.startswith('/en/'):
        result = "/" + langcode + "/" + path[4:]
    else:
        result = "/" + langcode + path
    return result



def merge_yfm(orig_yfm, trl_yfm, langcode):

    # general copy
    result_yfm = orig_yfm.copy()

    # keys
    result_keys = set(result_yfm)
    trl_keys = set(trl_yfm)
    if (result_keys != trl_keys):
        sys.stderr.write("Warning: Keys in YAML front matters do not match! Adapting only matching keys ...\n")
    keys = result_keys.intersection(set(trl_keys))

    # title
    if 'title' in keys:
        result_yfm['title'] = trl_yfm['title']

    # permalink
    if 'permalink' in keys:
        result_yfm['permalink'] = adapt_path(result_yfm['permalink'], langcode)

    # redirect_from
    if 'redirect_from' in keys:
        result_yfm['redirect_from'] = [adapt_path(p, langcode) for p in result_yfm['redirect_from']]

    # redirect_to
    if 'redirect_to' in keys:
        result_yfm['redirect_to'] = [adapt_path(p, langcode) for p in result_yfm['redirect_to']]

    return result_yfm



def merge_gfm_files(orig_gfm_lines, trl_gfm_lines, langcode):

    # get yaml front matter from orig
    orig_yaml_front_matter, start, end = get_yaml_front_matter(orig_gfm_lines)
    orig_yaml_front_matter_as_single_doc = orig_yaml_front_matter[1:-1] # removes '---\n' lines
    orig_yfm_string = ''.join(orig_yaml_front_matter_as_single_doc)
    orig_yfm = yaml.safe_load(orig_yfm_string)

    # get yaml front matter from trl
    trl_yaml_front_matter = trl_gfm_lines[start:end]
    trl_yaml_front_matter_as_single_doc = trl_yaml_front_matter[1:-1] # removes '---\n' lines
    trl_yfm_string = ''.join(trl_yaml_front_matter_as_single_doc)
    trl_yfm = yaml.safe_load(trl_yfm_string)

    # get body from trl
    trl_body = trl_gfm_lines[end:]

    # merge yaml front matters
    result_yfm = merge_yfm(orig_yfm, trl_yfm, langcode)

    # dump result yaml front matter
    result_yfm_dump = yaml.dump(result_yfm)

    # create translated document with adapted yaml front matter
    result_trl_gfm = '---\n' + ''.join(result_yfm_dump) + '---\n' + ''.join(trl_body)

    return result_trl_gfm



def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    # read original file
    orig_gfm_lines = []
    with open(sys.argv[1], 'r') as file:
        orig_gfm_lines = file.readlines()

    # read translated file
    trl_gfm_lines = []
    with open(sys.argv[2], 'r') as file:
        trl_gfm_lines = file.readlines()

    # read langcode
    langcode = sys.argv[3]

    # merge
    result = merge_gfm_files(orig_gfm_lines, trl_gfm_lines, langcode)

    # print result
    print(result)



if __name__ == '__main__':
    main()

