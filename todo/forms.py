from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):  # 新的網頁 新的URL 新的def方法(函式)
    # 表單綁定資料模型
    class Meta:
        model = Todo
        # fields = "__all__"  # 哪些欄位需要給使用者填充(__all__ 全部都要)
        fields = ["title", "text", "important", "completed"]
