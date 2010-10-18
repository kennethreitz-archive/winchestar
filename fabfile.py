from fabric.api import *

env['host_string'] = 'root@git.kennethreitz.com'

def push():
	""" Pushes the application to the server """

	print('Compressing application')
	local('tar -czf /tmp/winchestar.tar . ')

	print('Uploading application to server')
	put('/tmp/winchestar.tar', '/tmp/')

	print('Extraction application')
	with cd('/var/www/winchestar'):
		# run('rm -fr *')
		run('tar xzf /tmp/winchestar.tar')
		run('rm -fr /tmp/winchestar.tar')
		
		print('Restarting Apache.')
		run('/etc/init.d/apache2 stop')
		run('/etc/init.d/apache2 start')
		
		print('Application Pushed.')
