from optparse import OptionParser as op

def init_parser():
  parser = op()
  parser.add_option('-i', '--input', dest='audio_dir', help='use audio pieces in SRC_DIRECTORY', metavar='SRC_DIRECTORY')
  parser.add_option('-s', '--seed', dest='seed', help='starts track list with SEED', metavar='SEED')
  return parser.parse_args()

if __name__ == '__main__':
  (options, args) = init_parser()