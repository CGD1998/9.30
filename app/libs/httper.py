
import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json格式
        # r不是最终结果，其中还包含了状态码，http头等东西
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
