#encoding:utf-8
import argparse
import sys
import readline

def output(message):
	#sys.stdout.write(message + '\n')
	#sys.stdout.flush()
	print(message)

class config(object):
	access_key=''
	secret_key=''
	keepalive=True
	_instance=None
	def __new__(cls, *args,**kwargs):
		if cls._instance == None:
			cls._instance = object.__new__(cls)
		return cls._instance
	def __init__(self):
		pass
		#print('init')

def run_configure():
	cfg = config()
	options = [
		("access_key", "Access Key", "Access key and Secret key are your identifiers for WCS"),
		("secret_key", "Secret Key"),
		("keepalive", "keepalive", "request to use keepalive mode")
	]
	try:
		while True:
			output(u"Enter new values or accept defaults in brackets with Enter")
			output(u"Refer to user manual for detailed description of all options")
			for option in options:
				prompt = option[1]
				try:

					val = getattr(cfg, option[0])
					if type(val) is bool:
						val = val and "Yes" or "No"
					if val not in (None, ""):
						prompt += " [%s]" % val
						print(prompt)
				except AttributeError:
						pass

				if len(option) >= 3:
					output(u"\n%s" % option[2])
				val = input(prompt + ": ")
				if val != "":
					if type(getattr(cfg, option[0])) is bool:
						val = val.lower().startswith('y')
					setattr(cfg, option[0], val)
			output(u"\nNew settings:")
			for option in options:
				output(u"  %s: %s" % (option[0], getattr(cfg, option[0])))
			val = input("\nSave settings? [y/N] ")
			if val.lower().startswith("y"):
				break
			val = input("Retry configuration? [Y/n] ")
			if val.lower().startswith("n"):
				raise EOFError()
	except (EOFError, KeyboardInterrupt):
		#output(u"\nConfiguration aborted. Changes were NOT saved.")
		output(u"\nConfiguration aborted. Changes were NOT saved.")
		return
	except IOError as e:
		output(u"\nConfiguration aborted. Changes were NOT saved.")
		#print(u"Writing config file failed: %s: %s" % (config_file, e.strerror))
		sys.exit()

PARSER = argparse.ArgumentParser()
# Input Arguments
PARSER.add_argument('--configure',dest='runconfig',help='GCS file or local paths to training data',nargs='+',default='/home/adult.data.csv')
ARGUMENTS, _ = PARSER.parse_known_args()

if ARGUMENTS.runconfig:
	run_configure()
	sys.exit()

