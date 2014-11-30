from gi.repository import GObject, Gtk, Gio
from functools import partial
import logging

TITLE = "Debate Timer"
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE)
        self.set_default_size(400, 200)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = TITLE
        self.set_titlebar(hb)

        for t in (4, 3, 2):
            button = Gtk.Button(" {} ".format(t))
            button.connect('clicked', partial(self.reset_time, t * 60))
            hb.pack_start(button)

        reset_prep_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="edit-clear-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        reset_prep_button.add(image)
        hb.pack_end(reset_prep_button)

    def reset_time(self, seconds, button):
        print("You ressetted the time to {} seconds".format(seconds))

    def reset_prep(self, button):
        print("You resetted the prep")

class TimerButton(Gtk.ToggleButton):
    def __init__(self, minutes, seconds, countdown=False):
        Gtk.ToggleButton.__init__(self)
        self.countdown = countdown
        self.minutes = minutes
        self.seconds = seconds
        self.id = None
        self.connect('toggled', self._handle_toggled)

    def _handle_toggled(self):
        if self.get_active():
            self.id = GObject.timeout_add(1000, self._handle_second_elapsed)
        else:
            GObject.source_remove(self.id)

    def _handle_second_elapsed(self):
        pass

    def _update_text(self):
        self.set_label("{}:{}".format(self.minutes, self.seconds))

    def reset(self, second):
        pass


def second_elapse():
    print("A second has elapsed.")
    return True

def main():
    #GObject.timeout_add(1000, second_elapse)
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
