# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin


class DryBoxPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")


__plugin_name__ = "DryBoX"
__plugin_pythoncompat__ = ">=3.6,<4"
__plugin_implementation__ = DryBoxPlugin()