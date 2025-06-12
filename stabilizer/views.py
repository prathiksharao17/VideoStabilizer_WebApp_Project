import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .forms import VideoUploadForm
from .stabilize import stabilize_video

def home_view(request):
    return render(request, 'stabilizer/home.html')
def upload_view(request):
    form = VideoUploadForm()
    return render(request, 'stabilizer/upload.html', {'form': form})

def processing_page(request):
    return render(request, 'stabilizer/processing.html')

def stabilize_api(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video_file = request.FILES['video']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
        filename = fs.save(video_file.name, video_file)
        uploaded_path = fs.path(filename)

        output_path = os.path.join(settings.MEDIA_ROOT, 'results', f'stabilized_{filename}')
        side_by_side_path = os.path.join(settings.MEDIA_ROOT, 'results', f'side_by_side_{filename}')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        stabilize_video(uploaded_path, output_path, side_by_side_path)

        # Save to session
        request.session['stabilized_file'] = f'results/stabilized_{filename}'
        request.session['side_by_side_file'] = f'results/side_by_side_{filename}'

        return JsonResponse({'status': 'done'})
    return JsonResponse({'status': 'error'}, status=400)

def result_view(request):
    side_by_side_file = request.session.get('side_by_side_file')
    stabilized_file = request.session.get('stabilized_file')

    if not side_by_side_file or not stabilized_file:
        return redirect('upload')

    return render(request, 'stabilizer/result.html', {
        'side_by_side_url': settings.MEDIA_URL + side_by_side_file,
        'stabilized_url': settings.MEDIA_URL + stabilized_file,
    })
