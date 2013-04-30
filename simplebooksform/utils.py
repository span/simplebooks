
class type_converter():
    def string_to_int(s):
        try:
            x = int(s)
        except ValueError:
            x = 0
        return x

    def int_to_str(i):
        try:
            s = str(i)
        except ValueError:
            s = ''
        return s
    
    def xstr(s):
        return '0' if s is None else str(s)
