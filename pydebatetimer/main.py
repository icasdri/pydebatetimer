from gi.repository import GObject, Gtk

def second_elapse():
    print("A second has elapsed.")
    return True

def main():
    GObject.timeout_add(1000, second_elapse)
    GObject.MainLoop().run()

if __name__ == "__main__":
    main()
