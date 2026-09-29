from django.shortcuts import render, redirect, get_object_or_404
from .forms import EnquiryForm
from .models import Enquiry


def home(request):
    return render(request, "enquiry/home.html")


def about(request):
    return render(request, "enquiry/about.html")


def contact(request):
    return render(request, "enquiry/contact.html")


# CREATE
def enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = EnquiryForm()

    return render(request, "enquiry/enquiry_form.html", {"form": form})


# READ
def enquiry_list(request):
    enquiries = Enquiry.objects.all().order_by("-created_at")
    return render(request, "enquiry/enquiry_list.html", {"enquiries": enquiries})


# UPDATE
def edit_enquiry(request, id):
    enquiry = get_object_or_404(Enquiry, id=id)

    if request.method == "POST":
        form = EnquiryForm(request.POST, instance=enquiry)

        if form.is_valid():
            form.save()
            return redirect("list")

    else:
        form = EnquiryForm(instance=enquiry)

    return render(request, "enquiry/enquiry_form.html", {"form": form})


# DELETE
def delete_enquiry(request, id):
    enquiry = get_object_or_404(Enquiry, id=id)

    if request.method == "POST":
        enquiry.delete()
        return redirect("list")

    return render(request, "enquiry/delete.html", {"enquiry": enquiry})


def success(request):
    return render(request, "enquiry/success.html")