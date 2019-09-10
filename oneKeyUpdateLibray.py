import pip
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
for dist in get_installed_distributions():
	if dist.project_name=='pip':
		continue	
	# 	call("python -m pip install --upgrade pip",shell=True)
	call("pip install --upgrade -i https://pypi.douban.com/simple "+dist.project_name,shell=True)
	# print(dist.project_name)