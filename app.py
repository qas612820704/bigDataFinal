import sys, os
from src.normal import resizeImageDir

RUN_SHORT_CUT = "run"

def print_usage():
  print ("".join((
    "python app.py <cmd>\n",
    "<cmd>\n",
    "\thelp           : print this message\n",
    "\trun            : run project\n",
    '\tresizeImageDir <input_dir> <output_dir>  : BJ4'
  )))

if __name__ == '__main__':
  args = sys.argv[1:]
  args.insert(0, RUN_SHORT_CUT)
  if not args:
    print_usage()
    sys.exit(-1)
  
  if args[0] is "help":
    print_usage()
  elif args[0] is "run":
    print('runscript')
  elif args[0] is "resizeImageDir":
    if len(args) < 3:
      print('Not enough argments')
      print_usage()
      sys.exit(-1)
    resizeImageDir(args[1], args[2])
