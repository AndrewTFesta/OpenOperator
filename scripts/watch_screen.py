"""
@title

@description

"""
import argparse

from open_operator.desktop_screen import DesktopScreen


def main(main_args):
    dt_screen = DesktopScreen()
    dt_screen.start(display=False)

    input('Press any key to continue...')
    dt_screen.stop()
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')

    args = parser.parse_args()
    main(vars(args))
