# main.py
#
# Copyright 2021 Aurnytoraink
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi

from gi.repository import Gtk, Gio, Adw

from .window import HangmanWindow


class Application(Adw.Application):
    def __init__(self, version, application_id):
        super().__init__(application_id=application_id,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.version = version

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = HangmanWindow(application=self)
            if self.props.application_id.endswith('Devel'):
                win.get_style_context().add_class('devel')
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        win.present()

    def on_about_action(self, widget, *param):
        about = Gtk.AboutDialog()
        about.set_transient_for(self.props.active_window)
        about.set_modal(True)
        about.set_version(self.version)
        about.set_program_name("HangMan")
        about.set_logo_icon_name(self.props.application_id)
        about.set_authors(["Mathieu Heurtevin"])
        about.set_comments(_("Play the famous HangMan game"))
        about.set_wrap_license(True)
        about.set_license_type(Gtk.License.GPL_3_0)
        about.set_copyright(_("Copyright 2021 Mathieu Heurtevin"))
        about.set_website_label(_("GitHub"))
        about.set_website("https://github.com/Aurnytoraink/Hangman/")
        about.present()

    def on_preferences_action(self, widget, _):
        print('app.preferences action activated')

    def create_action(self, name, callback):
        """ Add an Action and connect to a callback """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        
