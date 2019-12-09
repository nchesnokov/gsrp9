from serviceloader import Service
from configparser import ConfigParser
from serviceloader.tools.common import configManager

gsrp5 = default_service_loader('gsrp5','serviceloader.tools.common','Dummy',config_file='conf/gsrp5.conf')
