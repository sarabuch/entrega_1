from django.shortcuts import render
from users.forms import UserEditForm 

# Create your views here.
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid:

            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            #usuario.image = informacion['image']
            usuario.save()

            return render(request, 'index.html')
        
    else:
        form = UserEditForm(initial={'email':usuario.email})

    return render(request, 'auth/editarPerfil.html', {'form':form, 'usuario':usuario})