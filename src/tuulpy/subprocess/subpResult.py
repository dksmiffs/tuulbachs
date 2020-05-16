import subprocess


# -----
def run(command):
  pp = subprocess.Popen(command, stderr=subprocess.STDOUT,
                                 stdout=subprocess.PIPE, shell=True)
  (output, err) = pp.communicate()
  return output


# -----
if '__main__' == __name__:
  print(run('whoami'))
