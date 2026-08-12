from django.http import HttpResponse

def post_details(request, post_id): 
    return HttpResponse(f"<h1>Post Details page for ID: {post_id}</h1>")
def user_profile(request,username):
    return HttpResponse(f"<h1>User Profile page for Username: {username}</h1>")
def articles_by_year(request,year):
    return HttpResponse(f"<h1>Articles page for year: {year}</h1>")
# def article_details(requst,year,month):
#     return HttpResponse(f'<h1>Articles page for year : {year} and month : {month}</h1>')
def article_details(request,**kwargs):
    return HttpResponse(f'<h1>Data: {kwargs}</h1>')

# We are accepting the arguments in the url 
    