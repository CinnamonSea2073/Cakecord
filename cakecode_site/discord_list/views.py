from django.shortcuts import render

# Create your views here.
def home(request):
    """
    folder = get_object_or_404(Folder, pk=folder_id)
    user_data = get_object_or_404(UserData, user=request.user)
    local_folder = get_object_or_404(LocalFolder, folder=folder, user=user_data)
    obj = Folder.objects.get(id=1)
    for vocabulary in obj.vocabulary_set.all():
        print(vocabulary.word)
    """
    return render(request, 'discord_list/home.html')