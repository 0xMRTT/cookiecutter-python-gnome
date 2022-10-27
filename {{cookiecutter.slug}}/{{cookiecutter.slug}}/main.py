import sys

from gi.repository import Gtk, Gio, Adw

from {{cookiecutter.slug}}.constants import (
    rootdir,
    app_id,
    rel_ver,
    version,
    bugtracker_url,
    help_url,
    project_url,
)

class Application(Adw.Application):
    """The main application singleton class."""

    __gtype_name__ = "Application"
    
    settings = Gio.Settings.new(app_id)

    def __init__(self):
        super().__init__(application_id=app_id, flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.set_resource_base_path(rootdir)
    
def main():
    """The application's entry point."""
    app = Application()
    return app.run(sys.argv)