from PIL import Image
from Xlib.display import Display, X


def printWindowHierrarchy(window, indent):
    children = window.query_tree().children
    for w in children:
        # print(indent, window.get_wm_class())
        try:
            raw = w.get_image(0, 0, 500, 500, X.ZPixmap, 0xffffffff)
            image = Image.frombytes("RGB", (500, 500), raw.data, "raw", "BGRX")
            image.show()
            return
        except Exception as e:
            pass
            # print(e)
        printWindowHierrarchy(w, indent + '-')


display = Display()
root = display.screen().root
printWindowHierrarchy(root, '-')

# from PIL import Image
# from Xlib.display import Display, X
#
#
# def find_window_hierarchy(window):
#     children = window.query_tree().children
#     for w in children:
#         try:
#             raw = w.get_image(0, 0, 500, 500, X.ZPixmap, 0xffffffff)
#             image = Image.frombytes("RGB", (500, 500), raw.data, "raw", "BGRX")
#             image.save()
#             print('saved ', window.window.get_wm_name())
#             return
#         except:
#             print('Exception')
#         find_window_hierarchy(w)
#
#
# if __name__ == '__main__':
#     display = Display()
#     root = display.screen().root
#     find_window_hierarchy(root)
