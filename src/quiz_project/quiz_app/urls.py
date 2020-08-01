from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, quizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index
from accounts.views import login, logout, register
from django.urls import path


urlpatterns = [
    url('^$', view=index, name='index'),
    url('^login/$', view=login, name='login'),
    url('^register/$', view=register, name='register'),
    url('^logout/$', view=logout, name='logout'),
    url('^quizzes/$', view=QuizListView.as_view(), name='quiz_index'),
    url('^category/$', view=CategoriesListView.as_view(), name='quiz_category_list_all'),
    url('^category/(?P<category_name>[\w|\W-]+)/$', view=ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    url('^progress/$', view=quizUserProgressView, name='quiz_progress'),
    url('^marking/$', view=QuizMarkingList.as_view(), name='quiz_marking'),
    url('^marking/(?P<pk>[\d.]+)/$', view=QuizMarkingDetail.as_view(), name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    url('^(?P<slug>[\w-]+)/$', view=QuizDetailView.as_view(), name='quiz_start_page'),
    url('^(?P<quiz_name>[\w-]+)/take/$', view=QuizTake.as_view(), name='quiz_question'),

]