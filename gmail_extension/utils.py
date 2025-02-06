def successfull_response(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        if not res.ok:
            raise Exception(f'An error occured on url:{res.url}, error: {res.text}')
        
        return res
    return wrapper