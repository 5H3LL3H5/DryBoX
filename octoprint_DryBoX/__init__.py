# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin


class DryBoxPlugin(octoprint.plugin.StartupPlugin,
                   octoprint.plugin.TemplatePlugin,
                   octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("DryBoX (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://github.com/5H3LL3H5/DryBoX")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]


__plugin_name__ = "DryBoX"
__plugin_pythoncompat__ = ">=3.6,<4"
__plugin_implementation__ = DryBoxPlugin()
