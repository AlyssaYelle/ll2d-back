from django.shortcuts import redirect, render
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.
from postcards.models import Postcard



def create_letter(request):
    letters = Postcard.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        dog_img_url = request.POST.get('dog_img_url')
        author = request.POST.get('author')
        author = author if len(author) > 0 else 'Anonymous'
        letter = request.POST.get('letter')

        response_data['dog_img_url'] = dog_img_url
        response_data['author'] = author
        response_data['letter'] = letter
      
        Postcard.objects.create(
            dog_img_url = dog_img_url,
            author = author,
            letter = letter,
            )
        return HttpResponseRedirect('/postcards')

    return render(request, 'index.html') 

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_postcards = Postcard.objects.all().count()

    
    # Number of Approved postcards
    num_postcards_approved = Postcard.objects.filter(approved=True).count()
    
    
    context = {
        'num_postcards': num_postcards,
        'num_postcards_approved': num_postcards_approved,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def form(request):
    return render(request, 'luv_letter_form.html')

from django.views import generic

class ApprovedPostcardListView(generic.ListView):
    model = Postcard

    def get_queryset(self):
        return Postcard.objects.filter(approved=True).all()


class PostcardListView(generic.ListView):
    model = Postcard

    def get_queryset(self):
        return Postcard.objects.all()