from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

text='''<form action="/hw/formsubmit/" method="post"> 
     <input type="text" name="your_name" /><br />
	<select multiple="multiple" name="bands"> 
		<option value='Beatles'>The Beatles</option> 	
		<option value='Who'>The Who</option> 
		<option value='Zombies'>The Zombies</option>
    </select>  <br/>	<input type="submit" />  </form>  <br/>
    <input type="text" value="%s ; %s" width="400"/>'''

@csrf_exempt

def index(request):
    return HttpResponse(text%(request.POST['your_name'],request.POST.getlist('bands')))
