import sys
import subprocess
import string
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from fileTransfer.models import Document, User

from .forms import UserForm
from fileTransfer.forms import DocumentForm
from django.views.generic import DetailView
from django import template


def main(request):
    return render(request, 'fileTransfer/main.html', {})

def list(request):
    # File upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            #redirect to list/main
            return HttpResponseRedirect(reverse('fileTransfer.views.list'))
    else:
        form = DocumentForm()

    #all documents beings populated...
    documents = Document.objects.all()

    # Render main page
    return render(request, 'fileTransfer/list.html', {'documents':documents, 'form': form})

def create(request):
	form=UserForm()

	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			def checkLength(password):
			    if (len(password) >= 8):
			        return 1
			    else:
			        print("Your password is not sufficiently long enough.  Please make it at least 8 characters.\n")
			        return 0

			def checkTop(password):
			    list = ["123456","password","12345678","1234","pussy","12345","dragon","qwerty","696969","mustang","letmein","baseball","master","michael","football","shadow","monkey","abc123","pass","fuckme","6969","jordan","harley","ranger","iwantu","jennifer","hunter","fuck","2000","test","batman","trustno1","thomas","tigger","robert","access","love","buster","1234567","soccer","hockey","killer","george","sexy","andrew","charlie","superman","asshole","fuckyou","dallas","jessica","panties","pepper","1111","austin","william","daniel","golfer","summer","heather","hammer","yankees","joshua","maggie","biteme","enter","ashley","thunder","cowboy","silver","richard","fucker","orange","merlin","michelle","corvette","bigdog","cheese","matthew","121212","patrick","martin","freedom","ginger","blowjob","nicole","sparky","yellow","camaro","secret","dick","falcon","taylor","111111","131313","123123","bitch","hello","scooter","please","porsche","guitar","chelsea","black","diamond","nascar","jackson","cameron","654321","computer","amanda","wizard","xxxxxxxx","money","phoenix","mickey","bailey","knight","iceman","tigers","purple","andrea","horny","dakota","aaaaaa","player","sunshine","morgan","starwars","boomer","cowboys","edward","charles","girls","booboo","coffee","xxxxxx","bulldog","ncc1701","rabbit","peanut","john","johnny","gandalf","spanky","winter","brandy","compaq","carlos","tennis","james","mike","brandon","fender","anthony","blowme","ferrari","cookie","chicken","maverick","chicago","joseph","diablo","sexsex","hardcore","666666","willie","welcome","chris","panther","yamaha","justin","banana","driver","marine","angels","fishing","david","maddog","hooters","wilson","butthead","dennis","fucking","captain","bigdick","chester","smokey","xavier","steven","viking","snoopy","blue","eagles","winner","samantha","house","miller","flower","jack","firebird","butter","united","turtle","steelers","tiffany","zxcvbn","tomcat","golf","bond007","bear","tiger","doctor","gateway","gators","angel","junior","thx1138","porno","badboy","debbie","spider","melissa","booger","1212","flyers","fish","porn","matrix","teens","scooby","jason","walter","cumshot","boston","braves","yankee","lover","barney","victor","tucker","princess","mercedes","5150","doggie","zzzzzz","gunner","horney","bubba","2112","fred","johnson","xxxxx","tits","member","boobs","donald","bigdaddy","bronco","penis","voyager","rangers","birdie","trouble","white","topgun","bigtits","bitches","green","super","qazwsx","magic","lakers","rachel","slayer","scott","2222","asdf","video","london","7777","marlboro","srinivas","internet","action","carter","jasper","monster","teresa","jeremy","11111111","bill","crystal","peter","pussies","cock","beer","rocket","theman","oliver","prince","beach","amateur","7777777","muffin","redsox","star","testing","shannon","murphy","frank","hannah","dave","eagle1","11111","mother","nathan","raiders","steve","forever","angela","viper","ou812","jake","lovers","suckit","gregory","buddy","whatever","young","nicholas","lucky","helpme","jackie","monica","midnight","college","baby","cunt","brian","mark","startrek","sierra","leather","232323","4444","beavis","bigcock","happy","sophie","ladies","naughty","giants","booty","blonde","fucked","golden","0","fire","sandra","pookie","packers","einstein","dolphins","0","chevy","winston","warrior","sammy","slut","8675309","zxcvbnm","nipples","power","victoria","asdfgh","vagina","toyota","travis","hotdog","paris","rock","xxxx","extreme","redskins","erotic","dirty","ford","freddy","arsenal","access14","wolf","nipple","iloveyou","alex","florida","eric","legend","movie","success","rosebud","jaguar","great","cool","cooper","1313","scorpio","mountain","madison","987654","brazil","lauren","japan","naked","squirt","stars","apple","alexis","aaaa","bonnie","peaches","jasmine","kevin","matt","qwertyui","danielle","beaver","4321","4128","runner","swimming","dolphin","gordon","casper","stupid","shit","saturn","gemini","apples","august","3333","canada","blazer","cumming","hunting","kitty","rainbow","112233","arthur","cream","calvin","shaved","surfer","samson","kelly","paul","mine","king","racing","5555","eagle","hentai","newyork","little","redwings","smith","sticky","cocacola","animal","broncos","private","skippy","marvin","blondes","enjoy","girl","apollo","parker","qwert","time","sydney","women","voodoo","magnum","juice","abgrtyu","777777","dreams","maxwell","music","rush2112","russia","scorpion","rebecca","tester","mistress","phantom","billy","6666","albert"]
			    if (password in list):
			        print("Your password is too common")
			        return 0
			    return 1

			def checkMix(password):
			    num, punct, letter = False, False, False
			    for i in range(0, len(password)):
			        if password[i].isalpha():
			            letter = True
			        elif password[i].isdigit():
			            num = True
			        elif ispunct(password[i]):
			            punct = True
			    if (letter & num & punct):
			        return 1
			    else:
			        print("Your pass does not fulfill the requirements of a good password")
			        return 0

			def ispunct(c):
			    return c in string.punctuation
			score = 0
			password = user.password
			score += checkLength(password);
			score += checkTop(password)
			score += checkMix(password);
			if (score != 3): #pass not valid
				print("A good password will be required to have at least 8 characters, 1 number, one letter, and one punctuation symbol.")
				return HttpResponseRedirect('/fileTransfer/wrongPassword/')
			else: #pass is valid
				print("Your password is good!\n")
				user.save()
				form.save_m2m()
				return HttpResponseRedirect('/fileTransfer/')
	return render(request, 'fileTransfer/create.html', {'form':form})

def about(request):
    return render(request, 'fileTransfer/about.html', {})


def wrongPassword(request):
	return render(request, 'fileTransfer/wrongPassword.html', {})


''' transfer handling '''

def send(request):
    # get the current user
    current_user_name = "dea"                               # TODO testing *****
    user = User.objects.get(name = current_user_name)
    # select a friend
    friend_name = "dead"                                    # TODO testing *****
    friend = User.objects.get(name = friend_name)
    # select the file to be sent
    doc_id = "27_-_5BLDnqz_u0BDp95.jpg"                                 # TODO testing ****
    transfer_file = Document(docfile = doc_id) 
    # call the model User method
    user.send_file(friend, transfer_file)
    # return the view
    form = DocumentForm()
    documents = Document.objects.all()
    return render(request, 'fileTransfer/transfer.html', {'documents': documents, 'form': form})

def receive(request):
    # get the current userme 
    current_user="dea"                                      # TODO testing *****
    user = User.objects.get(name = current_user)
    # call the model User method
    user.receive_file()
    # return the view
    form = DocumentForm()
    documents = Document.objects.all()
    return render(request, 'fileTransfer/transfer.html', {'documents': documents, 'form': form})



class TransferView(DetailView):

    model = User
    template_name = 'fileTransfer/transfer.html'

    def get(self, request, *args, **kwargs):
        form = DocumentForm()
        documents = Document.objects.all()
        return render(self.request, self.template_name, {'documents':documents, 'form': form})

    def post(self, request, *args, **kwargs):
        # File upload
        if self.request.method == 'POST':
            form = DocumentForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                open_file = Document(docfile = self.request.FILES['docfile'])
                open_file.save()

                print(open_file.id)
                
                return HttpResponseRedirect('.')
        else:
            form = DocumentForm()
        #all documents beings populated...
        documents = Document.objects.all()
        # Render main page
        return render(self.request, self.template_name, {'documents':documents, 'form': form})


