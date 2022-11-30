from optparse import OptionParser
import logging
from cassis import *

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",default="", action="store", type="string",
                  help="The input file", metavar="filename")
args = parser.parse_args()

(options, args) = parser.parse_args()

f = open(str(options.filename),'r')
text = f.read()

# Default Typesystem
cas = Cas(typesystem=load_dkpro_core_typesystem())

cas.sofa_string = text
cas.sofa_mime = "text/plain"

print (cas.to_xmi())


