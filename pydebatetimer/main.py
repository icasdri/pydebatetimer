from gi.repository import GObject, Gtk, Gio, Pango
from functools import partial

TITLE = "Debate Timer"
TIMER_FONT = Pango.FontDescription("Sans 32")
PREP_FONT = Pango.FontDescription("Sans 24")


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE)
        self.set_default_size(300, 300)

        # Header bar
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = TITLE
        self.set_titlebar(hb)

        for t in (4, 3, 2):
            button = Gtk.Button(" {} ".format(t))
            button.connect('clicked', partial(self.reset_time, t, 0))
            hb.pack_start(button)

        reset_prep_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="edit-clear-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        reset_prep_button.add(image)
        reset_prep_button.connect('clicked', self.reset_prep)
        hb.pack_end(reset_prep_button)

        # Main area
        table = Gtk.Table(2, 2, True)
        self.add(table)

        self.timer_button = TimerButton(4, 0, countdown=True)
        self.timer_button.modify_font(TIMER_FONT)
        table.attach(self.timer_button, 0, 2, 1, 2)

        self.prep_button_a = TimerButton(2, 0, countdown=True)
        self.prep_button_a.modify_font(PREP_FONT)
        table.attach(self.prep_button_a, 0, 1, 0, 1)

        self.prep_button_b = TimerButton(2, 0, countdown=True)
        self.prep_button_b.modify_font(PREP_FONT)
        table.attach(self.prep_button_b, 1, 2, 0, 1)

    def reset_time(self, minutes, seconds, button):
        self.timer_button.reset(minutes, seconds)

    def reset_prep(self, button):
        self.prep_button_a.reset(2, 0)
        self.prep_button_b.reset(2, 0)


class TimerButton(Gtk.ToggleButton):
    def __init__(self, minutes, seconds, countdown=False):
        Gtk.ToggleButton.__init__(self)
        self.reset(minutes, seconds, countdown)
        self.id = None
        self.connect('toggled', self._handle_toggled)

    def reset(self, minutes, seconds, countdown=None):
        self.set_active(False)
        if countdown is not None:
            self.countdown = countdown
        self.minutes = minutes
        self.seconds = seconds
        self._update_text()

    def _handle_toggled(self, button):
        if self.get_active():
            self.id = GObject.timeout_add(1000, self._handle_second_elapsed)
        else:
            GObject.source_remove(self.id)

    def _handle_second_elapsed(self):
        if self.get_active():
            if self.countdown:
                if self.seconds == 0:
                    if self.minutes != 0:
                        self.seconds = 59
                        self.minutes -= 1
                        self._update_text()
                else:
                    self.seconds -= 1
                    self._update_text()
            else:
                if self.seconds == 59:
                    self.seconds = 0
                    self.minutes += 1
                    self._update_text()
                else:
                    self.seconds += 1
                    self._update_text()
        return True

    def _update_text(self):
        self.set_label("%d:%02d" % (self.minutes, self.seconds))


def main():
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
