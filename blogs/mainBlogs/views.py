from django.http import JsonResponse
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from .models import Blog, User, Category
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.contrib.auth.hashers import make_password
from .decorators import hasRole
from datetime import date
from .DTO import BlogDTO, CategoryDTO


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def blogs(request):
    return_courses = Blog.objects.select_related().all()
    return_courses_dto = []
    for return_course in return_courses:
        return_courses_dto.append(BlogDTO(return_course).data)
    return JsonResponse(status=200, data=return_courses_dto, safe=False)


@api_view(['POST'])
@hasRole("ADMIN")
def addBlog(request):
    blog = Blog(text=request.data["text"], title=request.data["title"], date_created=date.today(), writer=request.user,
                category_id=1)
    blog.save()
    return JsonResponse(status=200, data={"blog_id": blog.id}, safe=False)


@api_view(['POST'])
@hasRole("ADMIN")
def addCategory(request):

    category = Category(name=request.data["name"])
    category.save()
    return JsonResponse(status=200, data={"category_id": category.id}, safe=False)


@api_view(['GET'])
@hasRole("ADMIN")
def get_profile(request):
    return JsonResponse(status=200, data={"first_name": request.user.first_name, "last_name": request.user.last_name},
                        safe=False)


@api_view(['GET'])
@hasRole("ADMIN")
def get_categories(request):
    categories = Category.objects.all()
    returning_blog = []
    for blog in categories:
        returning_blog.append(CategoryDTO(blog).data)
    return JsonResponse(status=200, data=returning_blog,
                        safe=False)


@api_view(['GET'])
@hasRole("ADMIN")
def get_blogs_for_profile(request):
    user = User.objects.get(pk=request.user.id)
    returning_blog = []
    for blog in user.blogs.all():
        returning_blog.append({"id": blog.id, "title": blog.title})
    return JsonResponse(status=200, data=returning_blog, safe=False)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['username']
    password = make_password(password)
    user = User(password=password, first_name=first_name, last_name=last_name,
                email=email)
    user.save()
    return JsonResponse(status=200, data={"User_id": user.user_id}, safe=False)