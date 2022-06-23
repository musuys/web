from django.contrib.auth.models import User
from django.db import models

from board.models import Post


# 사용자와 댓글의 관계=> 일대다
# 게시물과 댓글의 관계 => 일대다
# 다측에 관계설정
class Reply(models.Model):
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    #관계 맺어주기
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
