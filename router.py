#!python3
#-*-encoding:utf-8-*-


class Router:
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

    def __init__(self):
        self.list ={}
        self.path_list = set('')

    def __getattr__(self, attr):
        if attr.upper() in self.http_methods:
            return lambda path: self.request(attr.upper(), path)
        return (f'method {attr} is not defined for {self}')

    def add_path(self, path, method, func):
        self.path_list.add(path)
        if (method, path) in self.list.keys():
            if ((method, path), func) in self.list.items():
                return f"path {path} alredy associated with method {method}"
            else:
                self.list.update([((method, path), func)])
                return f'method {method} added for path {path}'
        else:
            self.list.update([((method, path), func)])
            return f'method {method} added for path {path}'


    def request(self, method, path):
        if (method, path) not in self.list.keys():
            if path not in self.path_list:
                return f'Error 404, path {path} not found'
            else:
                return f'Error 405, Method {method} not allowed'
        else:
            func = self.list[(method, path)]
            return func(path, method)


def my_info(path, method):
    return 200, {"me": "Joanne"}


def update_me(path, method):
    return 200, "OK"


if __name__ == '__main__':
    router = Router()

    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'PATCH', update_me))


    print(router.request('GET', '/me'))
    print(router.get('/me'))

    print(router.post( '/me'))
    print(router.get('/us'))
