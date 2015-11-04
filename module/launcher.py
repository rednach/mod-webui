from module import Webui_broker

from shinken.log import logger
logger.setLevel('DEBUG')

class ModConf(object):
    properties = {}

    def __init__(self):
        self.port = 7767
        self.company_logo = 'my_company'
        self.config_dir = '/var/lib/shinken/config/'
        self.share_dir = '/var/lib/shinken/share/'
        self.photos_dir = '/var/lib/shinken/share/photos/'

    def get_name(self):
        return 'tflk'

kui = Webui_broker(ModConf())
kui.main()