# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/1/31 下午 03:45
*  @Project :   demo01
*  @FileName:   Pagination.py
**************************************
程式用途:自定义分页组件

后端使用
data_list = models.yourTable.objects.all().order_by("id")
page_object = Pagination(request, data_list)
page_queryset = page_object.page_queryset
page_string = page_object.html()
context = {'data_list': page_queryset, "page_string": page_string}
return render(request, 'depart_list.html',context)
html使用
<nav aria-label="Page navigation">
    <ul class="pagination">
        {{ page_string }}
    </ul>
</nav>
"""
import json

from django.utils.http import urlencode
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=3):
        """
        分页工具类
        :param request: 请求对象 get请求
        :param queryset: 查找到的所有数据
        :param page_size: 每页数据条数
        :param page_param: 获取第几页的参数 camList?page=1
        :param plus: 每页显示plus个页码
        """
        query_dict = dict(request.args)
        # query_dict._mutable = True
        self.query_dict = query_dict
        page = request.args.get(page_param, "1")
        name = request.form.get(page_param, '1')
        self.name = name
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page_param = page_param
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        # 具体的数据内容
        self.page_queryset = queryset[self.start:self.end]
        total_count = len(queryset)
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus  # 每页显示10个页码写死

    def html(self):
        """
        :return: 页码html生成
        """
        # 计算出显示当前页前5页后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库的数据比较少，没有达到2*plus+1页
            page_start = 1
            page_end = self.total_page_count
        else:
            # 数据较多超出2*plus+1页
            # 当前页小于plus时
            if self.page <= self.plus:
                page_start = 1
                page_end = 2 * self.plus + 1
            else:
                # 当前页大于plus时
                # 当前页+plus>总页数
                if (self.page + self.plus) > self.total_page_count:
                    page_start = self.total_page_count - 2 * self.plus
                    page_end = self.total_page_count
                else:
                    page_start = self.page - self.plus
                    page_end = self.page + self.plus

        # 页码
        page_str_list = []
        # 首页
        self.query_dict[self.page_param] = 1
        page_str_list.append(
            '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>'.format(
                urlencode(self.query_dict)))
        # 上一页
        if self.page > 1:
            self.query_dict[self.page_param] = self.page - 1
            prev = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(
                urlencode(self.query_dict))
            # else:
            #     self.query_dict[self.page_param] = 1
            #     prev = '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(
            #         urlencode(self.query_dict))
            page_str_list.append(prev)
        for i in range(page_start, page_end + 1):
            self.query_dict['page'] = i
            if i == self.page:
                ele = ' <li class="page-item active"><a class="page-link" href="?{}">{}</a></li>'.format(
                    urlencode(self.query_dict), i)
            else:
                ele = ' <li class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(
                    urlencode(self.query_dict), i)
            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            self.query_dict[self.page_param] = self.page + 1
            next = '<li class="page-item"> <a class="page-link" href="?{}" aria-label="Next"> <span aria-hidden="true">»</span> </a> </li>'.format(
                urlencode(self.query_dict))
            # else:
            #     self.query_dict[self.page_param] = self.total_page_count
            #     next = '<li class="page-item"> <a class="page-link" href="?{}" aria-label="Next"> <span aria-hidden="true">»</span> </a> </li>'.format(
            #         urlencode(self.query_dict))
            page_str_list.append(next)
        # 尾页
        self.query_dict[self.page_param] = self.total_page_count
        page_str_list.append(
            '<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span aria-hidden="true">尾页</span></a></li>'.format(
                urlencode(self.query_dict)))
        # 输入页码跳转
        # self.query_dict[self.page_param] = self.name
        search_string = """
           <li>
               <form style="float:left;margin-left: -1px" method="get">
               <input name="page" type="text" class="form-control" placeholder="页码"
               style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0">
                   <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
               </form>
           </li>
           """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string
