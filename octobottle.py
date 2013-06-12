import threading
import logging
from octo.plugin import OctoPlugin
from bottle import run


class OctoBottle(OctoPlugin):
	"""A plugin for Octo, embedding the Bottle micro web-framework"""
	def on_activation(self):
		logger = logging.getLogger(__name__)
		config = self.plugin_config
		logger.info("Starting up Bottle webserver")
		t = threading.Thread(target=run,
		                     name="Bottle Webserver Thread",
		                     kwargs={
		                         'host': config.get('Config', 'Host', fallback='localhost'),
		                         'port': config.get('Config', 'Port', fallback=8080),
		                         'server': config.get('Config', 'Server', fallback='wsgiref'),
		                     }
		                    )
		t.daemon = True
		t.start()
