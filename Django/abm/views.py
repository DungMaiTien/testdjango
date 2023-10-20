from django.shortcuts import render


# Create your views here.
def abm(request):
    return render(request, 'abm/abm.html')

def news_post(request, pk):
    context = {
            "title": f"Tieu de bai viet {pk}",
            "summary": f"Tom tat bai viet {pk}",
            "Content": f"Noi dung chi tiet bai viet {pk}",
    }
    return render(request, 'abm/news_post.html', context)
