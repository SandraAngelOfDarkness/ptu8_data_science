def grazinti_tik_stringus(fn):
    def wrapper(text):
        if type(text) != str:
            raise ValueError("Text must be string")
        result_text = fn(text)
        return result_text(text)
    return wrapper

@grazinti_tik_stringus
def stringu_grazinimas(text):
    return str()