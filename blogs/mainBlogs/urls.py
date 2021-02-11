from django.conf.urls import url

from . import views as main_view

urlpatterns = [
    url(r'^blogs/$', main_view.blogs, name='blogs'),
    url('profiles/profile', main_view.get_profile, name='get_profile'),
    url(r'^profile/blogs/$', main_view.get_blogs_for_profile, name='get_profile_blogs'),
    url(r'^profile/categories/$', main_view.get_categories, name='get_categories'),
    url('add/blog', main_view.addBlog, name='addBlog'),
    url(r'^add/category/$', main_view.addCategory, name='add_category'),
    url('register', main_view.register, name='register')
]
