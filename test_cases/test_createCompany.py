"""
1.启动浏览器，打开URL


"""
import pytest

class CreateCompany:

    test_user_data = ["admin1", "admin2"]       # 数据改为读取excel文件
    @pytest.mark.parametrize("login", test_user_data, indirect=True)
    @pytest.mark.login
    def test_reate_company(login):
        print("到了到了")











