import core.ui.app
def main():
    try:

        core.ui.app.GameApp().run()
    except KeyboardInterrupt:
        print("")

if __name__ == "__main__":
    main()