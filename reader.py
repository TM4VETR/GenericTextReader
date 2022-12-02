from optparse import OptionParser
import logging
from cassis import *

# option parser object is constructed, allowing us to create custom options for the cmdline application.
parser = OptionParser()

# we add the option '-f' or '--file', to give the user the option to pass a textfile to the pipeline.
# the filename is stored in the variable 'filename'
parser.add_option("-f", "--file", dest="filename",default="", action="store", type="string",
                  help="The input file", metavar="filename")

# we read the options and arguments from the sdtin. (we expect the options to contain a filename)
(options, args) = parser.parse_args()

# the file with filename 'filename' is opened, the content is stored in an IO object.
f = open(str(options.filename),'r')

# the IO object is read, its contents are stored in the variable 'text'
text = f.read()

# open our sample typesystem and create a Typesystem instance from it.
with open('sample_typesystem.xml', 'rb') as f:
    sample_typesystem = load_typesystem(f)

merged_typesystem = merge_typesystems(sample_typesystem, load_dkpro_core_typesystem())

# We load the default typesystem of dkpro core and create a Common Analysis System (CAS) - object.
cas = Cas(typesystem=merged_typesystem)

# we set the Subject of Analysis (sofa) to the text we just read in from the file.
cas.sofa_string = text

# we specify the contenttype (or mime) as plain text
cas.sofa_mime = "text/plain"

# we send a string representation of the XML Metadata interchange (XMI) corresponding ot our CAS to the stdout.
print (cas.to_xmi())


