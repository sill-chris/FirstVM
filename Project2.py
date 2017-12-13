from webbrowser import open_new as on
import time


def my_break(break_info=None):
    """
    Function to keep track of breaks
    :param break_info: a dictionary with the following keys:
        t_break <int> default is 3
        url <string> default "https://youtu.be/uSD4vsh1zDA"
        t_sleep <int> is seconds, default = 3
    :return:
    """

    if break_info is None:
        # Default info
        break_info = {}
        break_info["t_breaks"] = 3
        break_info["url"] = "https://youtu.be/uSD4vsh1zDA"
        break_info["t_sleep"] = 60 * 60  # one hours
        # TODO: test for individual keys

        break_count = 0

        while break_count < break_info["t_breaks"]:
            # url = "https://youtu.be/uSD4vsh1zDA"
            on(break_info["url"])
            # time.sleep(3)
            time.sleep(break_info['t_sleep'])
            break_count += 1


if __name__ == '__main__':
    info = {}
    # my_break(info)
    my_break()
