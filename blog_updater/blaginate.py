import os.path, time, glob, operator, markdown, sys, optparse, codecs
from collections import OrderedDict

# helper functions
def convert_file(header, footer, md_text, new_path):
    body = markdown.markdown(md_text)
    page = header + body + footer

    new_file = codecs.open(new_path, mode="w", encoding="ISO-8859-1", errors="xmlcharrefreplace")
    new_file.write(page)
    print "Created: " + new_path
    new_file.close()

def create_new_file_path(orig_file_path):
    new_name = os.path.basename(orig_file_path)
    new_name = new_name.split(".")
    new_name = new_name[0]
    new_name += '.html'
    new_path = os.path.dirname(orig_file_path) + '\\' + new_name
    return new_path

def get_title_and_filename(file):
    print file
    # get the title of the doc (based off the url)
    new_name = os.path.basename(file)
    new_name = new_name.split(".")
    new_name = new_name[0]

    words = new_name.split("-")
    title = ''

    ct = 0
    for w in words:
        if (ct == 0):
            title += w
        else:
            title = title + ' ' + w
        ct += 1
    return [title, new_name]


msg = "usage: %prog [options] <markdown file/dir>"
parser = optparse.OptionParser(usage=msg)
parser.add_option("-n", metavar="NEW FILE/DIR", help="path for the converted html file or a directory for all converted files [optional]")
parser.add_option("-t", metavar="TOC", help="path for the table of contents html file [optional]")
parser.add_option("-c", metavar="CONFIG", help="path of the config file [optional]")

opts, args = parser.parse_args()

# vars
header = ""
footer = ""
body = ""
toc_docs = OrderedDict()  # toc_doc[title] = path_to_doc_on_server
toc_files_time_created = OrderedDict() # toc_files_time_created[title] = datetime
toc_files_time_updated = OrderedDict() # toc_files_time_updated[title] = datetime

if (len(sys.argv) < 2):
    parser.print_help()
    sys.exit()

# check if markdown file exists
md_file_path = sys.argv[1]
if (not os.path.exists(md_file_path)):
    print "Error: " + md_file_path + " does not exist."
    sys.exit()

# check if config file is exists
if (opts.c):
    if (not os.path.exists(opts.c)):
        print "Error: " + opts.c + " does not exist."
        sys.exit()
    config_file = open(opts.c)
    flag = False
    for line in config_file:
        if (line == "footer:\n"):
            flag = True
        if (line != "header:\n" and not flag):
            header += line
        elif (line != "header:\n" and line != "footer:\n"):
            footer += line

# if we're reading a directory, iterate through all .md files in sorder created
if (os.path.isdir(sys.argv[1])):
    md_dir_path = sys.argv[1]
    files = glob.glob(os.path.join(md_dir_path, '*.md'))
    files.sort(key=lambda x: os.path.getmtime(x))
    for file in files:
        # get the title of the doc (based off the url)
        tf = get_title_and_filename(file)
        title = tf[0]
        new_name = tf[1]

        # did user specify a new file/directory?
        if (opts.n):
            t_new_name = new_name + '.html'
            new_path = opts.n + '\\' + t_new_name
        else:
            new_path = create_new_file_path(file)

        # write new file
        md_file = codecs.open(file, mode="r", encoding="utf-8")
        md_text = md_file.read()
        convert_file(header, footer, md_text, new_path)
        
        # add file to the dictionaries (used for building table of contents)
        toc_docs[title] = new_path

        md_file.close()
else:
    new_path = ""
    # assume the new file is a valid location
    if (opts.n):
        new_path = opts.n
    else:
        new_path = create_new_file_path(md_file_path)
    
    md_file = codecs.open(md_file_path, mode="r", encoding="utf-8")
    md_text = md_file.read()
    convert_file(header, footer, md_text, new_path)
    tf = get_title_and_filename(md_file_path)
    title = tf[0]
    new_name = tf[1]

    toc_docs[title] = new_path

    md_file.close()

# build table of contents if desired
if (opts.t):
    toc_body = ''
    for t in toc_docs:
        toc_body += '<a href="./'+ toc_docs[t] +'" title="'+ toc_docs[t] +'">'+ t +'</a></br>'
    page = header + toc_body + footer

    toc_file = open(opts.t, 'w')
    toc_file.write(page)
    toc_file.close
    
    print "Created Table of Contents: " + opts.t