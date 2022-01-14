from spider_sku import tb_sku_title_
from spider_sku import tb_sku_prcie_
from spider_sku import tb_nick_
from spider_sku import tb_innerText_
from spider_sku import tb_view_sales_
from spider_sku import tb_comment_count_
from spider_sku import tb_item_loc_
from spider_sku import raw_

# print(len(amz_sku_title))
# for i in range(len(amz_sku_title)):
#     aa = amz_sku_title[i].text
#     print(aa)

#格式化淘宝SKU数据
print(len(tb_comment_count_), len(tb_sku_title_))
for i in range(len(tb_sku_title_)):
    tb_sku_title = tb_sku_title_[i]
    tb_sku_prcie = tb_sku_prcie_[i]
    tb_nick = tb_nick_[i]
    tb_innerText = tb_innerText_[i]
    tb_view_sales = tb_view_sales_[i]
    # tb_comment_count = tb_comment_count_[i]
    tb_item_loc = tb_item_loc_[i]
    raw = raw_[i]
    print(raw)