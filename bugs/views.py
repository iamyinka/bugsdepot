from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Bug, BugScreenshot
from .forms import BugForm, BugScreenshotForm


def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/bug_list.html', {'bugs': bugs})


@login_required(login_url='login')
def bug_create(request):
    if request.method == 'POST':
        bug_form = BugForm(request.POST)
        files = request.FILES.getlist('screenshots')
        if bug_form.is_valid():
            bug = bug_form.save()
            for file in files:
                screenshot_form = BugScreenshotForm({'image': file}, {'image': file})
                if screenshot_form.is_valid():
                    BugScreenshot.objects.create(bug=bug, image=file)
                else:
                    bug.delete()  # Rollback if any file is invalid
                    return render(request, 'bugs/bug_form.html', {
                        'form': bug_form,
                        'error': "Invalid file format. Only .jpg, .jpeg, and .png are allowed.",
                    })
            return redirect('bug_list')
    else:
        bug_form = BugForm()
    return render(request, 'bugs/bug_form.html', {'form': bug_form})


@login_required(login_url='login')
def bug_detail(request, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)
    return render(request, 'bugs/bug_detail.html', {'bug': bug})