import sys
import inspect

# version 3
def check():

	# old style, works for 2x and 3x
	print("you are running %s" % sys.version)


if __name__ == "__main__":
	check()
else:
	temp = inspect.stack()[0]
	filename= temp[1][0:-3]
	print "type '%s.%s to run program'" % (filename,'check()')