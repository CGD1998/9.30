from flask import jsonify, request
from app.forms.book import SearchFrom

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
# 蓝图 blueprint


@web.route('/book/search')
def search():
    """
    q:普通关键字 or isbn(一组数字）--如何鉴别
    page:strat count
    ?q=金庸&page=1
    :return:
    """
    form = SearchFrom(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
