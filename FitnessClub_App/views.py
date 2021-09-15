from django.shortcuts import render
from .forms import SignupFORMS, cardFORMS, Category, cardDetailsFORMS
from .models import TrainingSlotCard, TrainingCardDetail, UsersPaymentHistory, UploadClassVideos, UserAccount
from django.views import generic 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta



# create slot...
def cardVIEW(request):  
  if request.method == 'POST':
    form = cardFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = TrainingSlotCard(Trainee_Name = request.user, Heading=request.POST['HeadingF'], Training_period=request.POST['Training_periodF'], Category=request.POST['CategoryF'], Image=request.FILES['Images'])
      new_req.save()
      return HttpResponseRedirect('home')

  else:
    form = cardFORMS()
  
  htmlcode = True
  context = {'form': form}
  return render(request,'programs.html', context)



# home page...
def detailsVIEW(request, id):
  Card_key = TrainingSlotCard.objects.filter(id=id)
  idl = int(id) 

  #if paid then go to class room page
  if request.user.is_authenticated:
    classU = UsersPaymentHistory.objects.filter(Trainer_play = id).filter(User_Name = request.user)
       
    if classU:
      return HttpResponseRedirect(reverse('tclass', args=[str(id)])) 
  #endif


  # Payment page for Trainers ['Rate setUP']
  if request.method == 'POST':
    form = cardDetailsFORMS(request.POST, request.FILES)
    if form.is_valid():
      card_id_local_var = TrainingSlotCard.objects.get(id=id)
      new_req = TrainingCardDetail(Trainer_Name = request.user, Trainer_play=card_id_local_var, Seven_Day_Rate=request.POST['SevenF'], One_Month_Rate=request.POST['OneF'], Three_Months_Rate=request.POST['ThreeMF'], One_year_Rate =request.POST['OneYF'], Two_year_Rate =request.POST['TwoYF'], Video=request.FILES['Video'])
      new_req.save()
      return HttpResponseRedirect(reverse('home'))

  else:
    form = cardDetailsFORMS()
  # Payment Rate setup page close


  #paymentgateway page open for user [History Page]         (https://www.jquery-az.com/python-timedelta/#:~:text=%20Python%20timedelta%20class%20%201%20The%20syntax,the%20current%20date%20by%20today%20%28%29...%20More%20)
  if request.method == 'POST':
    card_id_local_var = TrainingSlotCard.objects.get(id=id)
    FREE = 'NULL'
    FREE = request.POST.get('flexRadioDefault')
    time_diff = timedelta(
                    days = int(FREE),
                  )
    date_time = date.today()
    
    if FREE != 'NULL':
      request_T = date_time + time_diff
    elif FREE == 'NULL':
      return HttpResponseRedirect(reverse('home'))

    new_req = UsersPaymentHistory( Trainer_Name=card_id_local_var.Trainee_Name, User_Name = request.user, Trainer_play=card_id_local_var, imageURL=card_id_local_var.Image , active=True , CardId = idl, expire_date= request_T)
    new_req.save()
    return HttpResponseRedirect(reverse('tclass', args=[str(id)]))    
  #payment page close
  details = TrainingCardDetail.objects.filter(Trainer_play = id)

  return render(request, 'proposel.html', {'form': form, 'ID_Card':Card_key, 'Details': details, 'classU': classU})



# home page...
def homeVIEW(request):
  return render(request, 'index.html')


def enrollsVIEW(request):
  if request.user.is_authenticated:
    classU = UsersPaymentHistory.objects.filter(User_Name = request.user)
    card = TrainingSlotCard.objects.all()
    return render(request, 'enrolls.html',{'classU': classU, 'card':card})


def accountVIEW(request):
  if request.user.is_authenticated:
    info = UserAccount.objects.filter(User_Name = request.user)
    classU = TrainingSlotCard.objects.filter(Trainee_Name = request.user)
    enrolls = UsersPaymentHistory.objects.filter(User_Name = request.user)
    return render(request, 'Account.html',{'classU': classU, 'info':info, 'enrolls': enrolls})


def classmetarialVIEW(request, id):
  card_id_local_var = TrainingSlotCard.objects.get(id=id)
  card = TrainingSlotCard.objects.all().filter(id=id)
  videos = UploadClassVideos.objects.order_by('-id').filter(Trainer_play = card_id_local_var.Heading)
  
  if request.method == "POST":
    Card_key = TrainingSlotCard.objects.filter(id=id)
    Heading = TrainingSlotCard.objects.get(id=id)
    name = request.POST.get("filename")
    myfile = request.FILES.getlist("uploadfoles")
        
    # multiple video storage
    for f in myfile:
      UploadClassVideos(Trainer=request.user,Trainer_play= Heading,f_name=name,myfiles=f).save()
    return HttpResponseRedirect(reverse('tclass', args=[str(id)])) 

  return render(request, 'class.html',{'videos':videos, 'local': card})
  
  


# livehome...
def livehomeVIEW(request):
  All_ICONS = Category.objects.all().order_by('id')
  Gym_All_cards = TrainingSlotCard.objects.filter(Category='GYM Training').order_by('id')
  Fitness_All_cards = TrainingSlotCard.objects.filter(Category='Fitness Training').order_by('id')
  meditation_All_cards = TrainingSlotCard.objects.filter(Category='meditation').order_by('id')
  YOGA_All_cards = TrainingSlotCard.objects.filter(Category='YOGA').order_by('id')
  Diet_All_cards = TrainingSlotCard.objects.filter(Category='Diet Plans & Recipes').order_by('id')
  Boxing_All_cards = TrainingSlotCard.objects.filter(Category='Boxing').order_by('id')
  Dancing_All_cards = TrainingSlotCard.objects.filter(Category='Dancing').order_by('id')
  Running_All_cards = TrainingSlotCard.objects.filter(Category='Running').order_by('id')
  judo_All_cards = TrainingSlotCard.objects.filter(Category='judo karate').order_by('id')
  return render(request, 'livehome.html',{'icons':All_ICONS, 'Gym_cards': Gym_All_cards, 'Fitness_cards': Fitness_All_cards,'meditation_cards': meditation_All_cards, 'YOGA_cards': YOGA_All_cards, 'Diet_cards': Diet_All_cards, 'Boxing_cards': Boxing_All_cards, 'Dancing_cards': Dancing_All_cards, 'Running_cards': Running_All_cards, 'judo_cards': judo_All_cards})



# SignUP...
class UserRegisterView(generic.CreateView):
  form_class = SignupFORMS
  template_name  = 'registration/register.html'
  success_url = reverse_lazy('login')