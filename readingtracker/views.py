import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .forms import ReadingSessionForm
from .models import ReadingSession
from .utils import *
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = ReadingSessionForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                validate_file_type(file)
                session = form.save(commit=False)
                session.user = request.user
                session.save()
                return redirect('reading_time:reading_session', session.id)
            except ValidationError as e:
                form.add_error('file', e)
    else:
        form = ReadingSessionForm()
    return render(request, 'tracker/upload.html', {'form': form})


def reading_session(request, session_id):
    session = ReadingSession.objects.get(id=session_id)

    # Process the file and extract text
    file_path = os.path.join(settings.MEDIA_ROOT, session.file.name)

    if session.file.name.endswith('.pdf'):
        content = extract_text_from_pdf(file_path)
    elif session.file.name.endswith('.docx'):
        content = extract_text_from_docx(file_path)
    else:
        content = "Unsupported file type."

    # Set up a timer for reading time

    if request.method == 'POST':
        session.end_time = timezone.now()
        session.reading_time = session.end_time - session.start_time
        session.save()
        return redirect('reading_time:summary', session.id)

    return render(request, 'tracker/reading_session.html', {'session': session, 'content': content})

def summary(request, session_id):
    session = ReadingSession.objects.get(id=session_id)
    if request.method == 'POST':
        reading_duration = request.body
        reading_duration = json.loads(reading_duration).get('reading_duration')
        
        # Update reading_time and end_time
        session.reading_time = timezone.timedelta(seconds=reading_duration)
        session.end_time = timezone.now()
        session.save()
        return JsonResponse({'status': 'success'})

    return render(request, 'tracker/summary.html', {'session': session})
