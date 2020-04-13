from tuulpy.subprocess import subpResult


# -----
def is_clean_working_tree():
  dirty = subpResult.run('git status --porcelain')
  return not dirty  


# -----
def main():
  if is_clean_working_tree():
    print('clean')
  else:
    print('NOT clean')


# -----
if '__main__' == __name__:
  main()
