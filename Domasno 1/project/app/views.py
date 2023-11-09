import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .services.upsert import upsert
from .services.pipelines.cleanup import cleanup_pipeline


@require_http_methods(["GET"])
def home(request):
    context = {
        "asd": "nesto tuka",
        "bdc": "dr nesto tuka",
    }

    return render(request, "app/homescreen.html", context)


@require_http_methods(["GET"])
def upsert_view(request):
    data = cleanup_pipeline()
    upsert(data)

    response_data = {
        "is_successfull": True,
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
