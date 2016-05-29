from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


##
# Provides a catchall which directs users to the correct endpoint.
# If logged in, it redirects users to their homepage;
# if not, they are presented with a login page
def routing(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user_portal'))
    else:
        return HttpResponseRedirect(reverse('gate'))


##
# Provides prompt for user to log in, and redirects to the user's destination
# if a next link is specified in the GET parameters
def gate(request):
    user_info_form = UserInformationForm()
    next_url = request.GET.get('next', None)
    if next_url is not None:
        return render(request, 'volunteers/gate.html', {'form': user_info_form, 'next': next_url, })
    return render(request, 'volunteers/gate.html', {'form': user_info_form, })
