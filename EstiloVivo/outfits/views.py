from django.shortcuts import render, redirect, get_object_or_404
from .forms import OutfitForm
from .models import Outfit, Comentario
from django.http import HttpResponseRedirect


def outfits(request):
    outfits = Outfit.objects.all()

    if request.method == 'POST':
        form = OutfitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outfits')  # Redirigir a la misma página para mostrar la tabla
    else:
        form = OutfitForm()

    return render(request, 'outfits.html', {'form': form, 'outfits': outfits})

def index(request):
    outfits = Outfit.objects.all()
    return render(request, 'index.html', {'index': index})

def comofunciona(request):
    comofunciona = Outfit.objects.all()
    return render(request, "comofunciona.html", {"comofunciona": comofunciona})

def comunidad(request):
    comunidad_masculino = Outfit.objects.filter(genero='Masculino').order_by('-cantidad_corazones')
    comunidad_femenino = Outfit.objects.filter(genero='Femenino').order_by('-cantidad_corazones')

    return render(request, "comunidad.html", {"comunidad_masculino": comunidad_masculino, "comunidad_femenino": comunidad_femenino})

def cameron(request):
    cameron = Outfit.objects.all()
    return render(request, "cameron.html", {"cameron": cameron})

def resultados_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        genero = request.POST.get('genero')
        estilo_prenda = request.POST.get('estilo_prenda')
        color_prenda = request.POST.get('color_prenda')

        # Realiza la búsqueda en la base de datos
        resultados = Outfit.objects.filter(
            genero=genero,
            estilo_prenda=estilo_prenda,
            color_prenda=color_prenda
        )

        return render(request, 'prendasescogidas.html', {'resultados': resultados})

    return render(request, 'formulario.html')  # Ajusta el nombre del archivo HTML según tu estructura de carpetas

def prendaindividual(request):
    prendaindividual = Outfit.objects.all()
    return render(request, "prendaindividual.html", {"prendaindividual": prendaindividual})

def prendasEscogidas(request):
    prendasEscogidas = Outfit.objects.all()
    return render(request, "prendasEscogidas.html", {"prendasEscogidas": prendasEscogidas})

def prendaindividual_view(request, outfit_id):
    outfit = get_object_or_404(Outfit, pk=outfit_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'comentario':
            comentario_texto = request.POST.get('comentario')

            if comentario_texto:
                comentario = Comentario.objects.create(outfit=outfit, usuario=request.user, texto=comentario_texto)


        elif action == 'corazon':
            if request.user in outfit.usuarios_que_dieron_corazon.all():
                # User has given a heart, remove it
                outfit.cantidad_corazones -= 1
                outfit.usuarios_que_dieron_corazon.remove(request.user)
            else:
                # User hasn't given a heart, add it
                outfit.cantidad_corazones += 1
                outfit.usuarios_que_dieron_corazon.add(request.user)

            outfit.save()

    return render(request, 'prendaindividual.html', {'outfit': outfit})