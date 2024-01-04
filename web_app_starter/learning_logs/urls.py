"""定义learning_logs的URL模式"""

from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # 主页
    path("", views.index, name="index"),
    # 显示单个主题
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # 显示所有主题
    path("topics/", views.topics, name="topics"),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
]
