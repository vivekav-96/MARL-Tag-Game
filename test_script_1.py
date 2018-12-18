from PIL import Image
from Xlib.display import Display, X


def printWindowHierrarchy(window, indent):
    children = window.query_tree().children
    for w in children:
        cl = window.get_wm_name()
        if cl == 'MARL Tag':
            try:
                raw = w.get_image(0, 0, 750, 750, X.ZPixmap, 0xffffffff)
                image = Image.frombytes("RGB", (750, 750), raw.data, "raw", "BGRX")
                image.show()
            except Exception as e:
                print(e)

        printWindowHierrarchy(w, indent + '-')

        # try:
        #     raw = w.get_image(0, 0, 750, 750, X.ZPixmap, 0xffffffff)
        #     image = Image.frombytes("RGB", (750, 750), raw.data, "raw", "BGRX")
        #     image.show()
        # except Exception as e:
        #     pass
        #     print(indent, window.get_wm_class(), e)
        # printWindowHierrarchy(w, indent + '-')


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
