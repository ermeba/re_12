from django.contrib import admin
# from django.forms import forms
from django import forms
from django.contrib.admin import display
from django.contrib.sites import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path, include, reverse
from django.utils.html import format_html

from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View

from django_admin_listfilter_dropdown.filters import (DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter,
                                                      RelatedOnlyDropdownFilter)
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter
from rest_framework.generics import get_object_or_404
from viya1.functions import handle_uploaded_file
from viya1.models import City, Division, District, SubDistrict, Address, Type, Status, Property, Sours, PropertySingle, \
    Partner, Project, Client, ClientContact, FamilyMember, References, FamilyDocuments, ClientDocuments, Offers, \
    OfferPhotos, OfferDescription, OfferPrice, OfferSqm, OfferProject, OfferCompany, OfferType, OfferRoomTypeExpression, \
    OfferProjectPhotos, OfferProjectPhotosS, OfferProjectRoomType, OfferProjectVideosS, OfferProjectMapsS
from django.shortcuts import render
# Property, Type, Status, PropertySingle

import pdfkit
from django.http import HttpResponse
from django.template import loader

import re



class StatusInline(admin.TabularInline):
    model = Status
    max_num = 1

    def has_delete_permission(self, request, obj=None):
        return False


class TypeInline(admin.TabularInline):
    model = Type
    max_num = 1

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request, obj):
    #     return False


class SoursInline(admin.TabularInline):
    model = Sours
    max_num = 1

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request, obj):
    #     return False


class PropertySingleInline(admin.TabularInline):
    model = PropertySingle
    extra = 5


class AddressInline(admin.TabularInline):
    model = Type
    max_num = 1

    class Media:
        js = ("viya1/selectajax.js",)

    def has_delete_permission(self, request, obj=None):
        return False

    # def has_add_permission(self, request, obj):
    #     return False


# templates/admin/viya1/adding_property/change_form.html

class ScrapData(forms.Form):
    scrap_data = forms.FileField()


class NameForm(forms.Form):
    get_link1 = forms.CharField(label='Your name', max_length=100)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/viya1/property/change_list.html'
    actions = ('make_offers_available',)
    inlines = [StatusInline, TypeInline, SoursInline, PropertySingleInline]
    list_display = ['image_preview',
                    'offer',
                    'name',
                    # 'price_dollar',
                    'price',
                    'nr_of_rooms',
                    'brut_case_net',
                    'city_case_division',
                    'link',
                    'pdf1',
                    'edit',
                    # 'active',
                    'status']
    search_fields = ['offer', 'advert_no']
    list_editable = []
    list_display_links = ('image_preview', 'offer')
    list_per_page = 20

    def custom_titled_filter(title):
        class Wrapper(admin.FieldListFilter):
            def __new__(cls, *args, **kwargs):
                instance = admin.FieldListFilter.create(*args, **kwargs)
                instance.title = title
                return instance

        return Wrapper

    list_filter = [
        ("name", custom_titled_filter('')),
        "nr_of_rooms",
        ("city", RelatedOnlyDropdownFilter),
        ("division", RelatedOnlyDropdownFilter),
        ("price", RangeNumericFilter),
        ("square_meter_brut", RangeNumericFilter),
        'status',
        'sours',
        'created_on',
    ]

    #
    # def xml(self, obj):
    #     return format_html('<input type="button" onclick="location.href="/admin/viya1/my_model/{}/change/" '
    #                        'value="xml" />'
    #                        , obj.id)

    @admin.display(description='PDF')
    def pdf1(self, obj):
        return format_html('<input type="button" onclick="window.open(`/media/{}`,`_blank`)"'
                           'value="pdf" />'
                           , obj.pdf)

    # onclick="window.location.href=`/media/{}`"
    def edit(self, obj):
        prop = Property.objects.all()
        return format_html('<input type="button" onclick="window.open(`/admin/viya1/property/{}/change/`,`_blank`)"'
                           'value="edit" />'
                           , obj.id)

    # def active(self, obj):
    #     prop = Property.objects.all()
    #     return format_html('<input type="button" onclick="window.open(`/admin/viya1/property/{}/change/`,`_blank`)"'
    #                        'value="Check the status" />'
    #                        , obj.id)

    # def delete_button(self, obj):
    #     return format_html('<input type="button" onclick="location.href="/admin/viya1/my_model/{}/change/" '
    #                        'value="Delete" />'
    #                        , obj.id)

    # def delete(self, obj):
    #     view_name = "admin:{}_{}_delete".format(obj._meta.app_label, obj._meta.model_name)
    #     link = reverse(view_name, args=[property])
    #     html = '<input type="button" onclick="location.href=\'{}\'" value="Delete" />'.format(link)

    def make_offers_available(self, modeladmin, request, queryset):
        queryset.update(is_available=True)

    make_offers_available.short_description = "Mark selected offers as available"

    @admin.display(description='Location')
    def city_case_division(self, obj):
        return ("%s / %s" % (obj.city, obj.division))

    # @admin.display(description='Price in $')
    # def price_dollar(self, obj):
    #     return ("$ %s " % ( '{:,}'.format(obj.price)))

    @admin.display(description='Brut - Net m2')
    def brut_case_net(self, obj):
        return "%s - %sm2" % (obj.square_meter_brut, obj.square_meter_net)

    # def get_type_of_property(self, obj):
    #     return obj.type.type_of_property

    # @display(ordering='type_of_property', description='Type')
    # def get_type(self, obj):
    #     return obj.property.type_of_property

    # def status_of_property_n(self, obj):

    class Media:
        js = ("viya1/selectajax.js",)



# @admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/viya1/property/change_list.html'

    inlines = []
    list_display = ['name_of_company', 'year_of_establishment', 'address', 'phone_number', 'number_of_project',
                    'show_firm_url', 'image_preview']
    # search_fields = ['advert_no', 'city', 'division' ]
    # list_filter = ['nr_of_rooms', 'nr_of_bathrooms', 'city', 'division' ]
    list_editable = ['number_of_project']
    list_per_page = 25

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.website)


admin.site.register(Partner, PartnerAdmin)


class ProjectAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/viya1/property/change_list.html'

    inlines = []
    list_display = ['project', 'name_of_project', 'year_of_completion', 'type_of_project',
                    'address', 'phone_number', 'show_firm_url', 'image_preview']
    # search_fields = ['advert_no', 'city', 'division' ]
    # list_filter = ['nr_of_rooms', 'nr_of_bathrooms', 'city', 'division' ]
    # list_editable = ['number_of_project']
    list_per_page = 25

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.website)

    # @admin.display(description='Completed on')
    # def completation_case_year(self, obj):
    #     return ("%s/%s" % (obj.status_of_project, obj.year_of_completion))


admin.site.register(Project, ProjectAdmin)


class ClientContactInline(admin.TabularInline):
    model = ClientContact
    extra = 1


class ClientDocumentsInline(admin.TabularInline):
    model = ClientDocuments
    extra = 1


class ReferencesInline(admin.TabularInline):
    model = References
    extra = 1


#
# class RelationshipsInline(admin.TabularInline):
#     model = Relationships
#     max_num = 1


class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1


class FamilyDocumentsInline(admin.TabularInline):
    model = FamilyDocuments
    extra = 1


class OpenProfile(forms.Form):
    open_profile = forms.FileField()


from django.shortcuts import render
from django.http import HttpResponse
from viya1.functions import handle_uploaded_file
from viya1.forms import ClientDocumentsForm


class ClientAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/viya1/property/change_list.html'

    inlines = [ClientContactInline, ClientDocumentsInline, ReferencesInline, FamilyMemberInline,
               FamilyDocumentsInline, ]
    list_display = ['image_preview', 'name', 'surname', 'birthday', 'address', 'edit', 'profil']
    # search_fields = ['advert_no', 'city', 'division' ]
    # list_filter = ['nr_of_rooms', 'nr_of_bathrooms', 'city', 'division' ]
    # list_editable = ['number_of_project']
    list_per_page = 25



    def edit(self, obj):
        prop = Property.objects.all()
        return format_html('<input type="button" onclick="window.open(`/admin/viya1/client/{}/change/`,`_blank`)"'
                           'value="edit" />'
                           , obj.id)

    def profil(self, obj):
        prop = Property.objects.all()
        return format_html('<input type="button" onclick="window.open(`open_profile/{}/change/` )"'
                           'value="show profil" />'
                           , obj.slug1)

    # { % url
    # 'productsingle'
    # product.slug1 %}

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('open_profile/<slug:slug>/change/', self.open_profile),
        ]
        return my_urls + urls  # <int:post_id>

    def open_profile(self, request, slug):  # post_id
        clientdata = Client.objects.all()
        slug_1 = Client.objects.get(slug1=slug)
        phone = ClientContact.objects.filter(client_key=slug_1.id)
        reference = References.objects.filter(client_key=slug_1.id)
        client_document = ClientDocuments.objects.filter(client_key=slug_1.id)
        family_document = FamilyDocuments.objects.filter(client_key=slug_1.id)

        # slug_1 = Client.objects.get(slug1=slug)
        # members = FamilyMember.objects.get(client_key=slug_1.id)
        # print(members)

        if request.method == 'POST':
            student = ClientDocumentsForm(request.POST, request.FILES)
            if student.is_valid():
                handle_uploaded_file(request.FILES['client_dokument'])
                model_instance = student.save(commit=False)
                model_instance.save()
                # return HttpResponse("File uploaded successfully")
            student = ClientDocumentsForm()
            context = {
                'slug_1': slug_1,
                # 'posts': posts,
                'phone': phone,
                'reference': reference,
                'client_document': client_document,
                'form': student,
                # 'family_document': family_document
            }

            # print("print context", context)
            return render(request, 'admin/viya1/client/profil.html', context)


        # posts = get_object_or_404(Client, id=post_id)
        # posts = Client.objects.get(pk=pk)
        # if request.method == "POST":
        #      link = 'jjj'
        #     csv_file = request.FILES["csv_file"]
        #     reader = csv.reader(csv_file)
        #
        #     self.message_user(request, "Your csv file has been imported")
        #     return redirect("..")
        # form = ScrapData()
        # data = {"form": form}
        # print("data", data)

        else:
            student = ClientDocumentsForm()
            context = {
                'slug_1': slug_1,
                # 'posts': posts,
                'phone': phone,
                'reference': reference,
                'client_document': client_document,
                'form': student
                # 'family_document': family_document
            }

            # print("print context", context)
            return render(request, 'admin/viya1/client/profil.html', context)


# templates/admin/viya1/client/projects.html
# (`/media/{}`,`_blank`)


admin.site.register(Client, ClientAdmin)


#
# class StudentEnrollmentInline(admin.TabularInline):
#     model = Enrollment
#     readonly_fields=('id',)


# class StudentEnrollmentInline(admin.TabularInline):
#     model = Enrollment
#     readonly_fields=('student_enrollment_id',)
#
#     def student_enrollment_id(self, obj):
#         return obj.id


#
# clientdata = Client.objects.all()
# # slug_1 = Client.objects.get(slug1=slug
# # posts = Client.objects.get(pk=pk)
#
# print (clientdata)


class OfferPhotosInline(admin.TabularInline):
    model = OfferPhotos
    extra = 1


class OfferDescriptionInline(admin.TabularInline):
    model = OfferDescription
    max_num = 1


class OfferPriceInline(admin.TabularInline):
    model = OfferPrice
    max_num = 1


class OfferSqmInline(admin.TabularInline):
    model = OfferSqm
    max_num = 1


class OffersAdmin(admin.ModelAdmin):
    inlines = [OfferPhotosInline, OfferDescriptionInline, OfferPriceInline, OfferSqmInline]
    list_display = ['image_preview', 'offer_type', 'city', 'division', 'project',
                    'company']  # 'profile_foo', 'room_type'
    # list_display = ['offer_name',  'offer_type',  'city', 'division', 'district', 'subdistrict',
    #                 'price', 'sqm', 'sqm','room_type', 'contact', 'description', 'features', 'address' ]
    # search_fields = ['advert_no', 'city', 'division' ]
    # list_filter = ['nr_of_rooms', 'nr_of_bathrooms', 'city', 'division' ]
    # list_editable = ['offer_name']
    # raw_id_fields = ['offer_type','project','company' ]
    list_display_links = ('image_preview', 'offer_type')
    list_per_page = 25

    class Media:
        js = ("viya1/selectajax.js",)


admin.site.register(Offers, OffersAdmin)


class OfferProjectPhotosSInline(admin.TabularInline):
    model = OfferProjectPhotosS
    extra = 6


class OfferProjectVideosSInline(admin.TabularInline):
    model = OfferProjectVideosS
    extra = 1


class OfferProjectRoomTypeInline(admin.TabularInline):
    model = OfferProjectRoomType
    extra = 1


class OfferProjectMapsSInline(admin.TabularInline):
    model = OfferProjectMapsS
    extra = 1


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",
    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
}


# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('app/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    # Automaticly downloads to PDF file
    class DownloadPDF(View):
        def get(self, request, *args, **kwargs):
            pdf = render_to_pdf('app/pdf_template.html', data)

            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response

        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """
        """ PROJECT OF VIYA """


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper

class OfferProjectAdmin(admin.ModelAdmin, View):
    inlines = [OfferProjectPhotosSInline, OfferProjectRoomTypeInline, OfferProjectVideosSInline,
               OfferProjectMapsSInline]
    list_display = ['image_preview', 'city_case_division', 'name_of_project', 'price_in_dollar',
                    'citizenship', 'residence_permit', 'view',
                    'year_of_completion',
                    'type_of_project', 'details', 'pdf_converter']
                    #'status_of_project', 'pdf_downloader'



    list_filter = [

        ("city", RelatedOnlyDropdownFilter),
        ("division", RelatedOnlyDropdownFilter),
        ("name_of_project", DropdownFilter),
        # ("name_of_project", RelatedOnlyDropdownFilter),
        ("starting_price", RangeNumericFilter),
        # (("type_of_project", ChoiceDropdownFilter), custom_titled_filter("Status")),
        ("type_of_project", custom_titled_filter("Type")),
        ("year_of_completion", custom_titled_filter("Year")),
        ("status_of_project", custom_titled_filter("Status")),
    ]
    #

    list_per_page = 25

    @admin.display(description='Starting Price')  # '{:,}'.format(price)+ ""+ "$"
    def price_in_dollar(self, obj):
        if obj.starting_price:
            return ('{:,}'.format(obj.starting_price) + "" + "$")
        else:
            return ("None")

    @admin.display(description='Location')  # return ("%s \n %s" % (city, division))
    def city_case_division(self, obj):
        city = str(obj.city)
        division = str(obj.division)
        line = (city + " " + division)
        line2 = re.sub(r' ', '\n', line)
        return (line2)

    def details(self, obj):
        return format_html('<input type="button" onclick="window.open(`open_project/{}/change/` )"'
                           'value="show details" />', obj.slug2)

    def pdf_converter(self, obj):
        return format_html('<input type="button" onclick="window.open(`convert_project/{}/change/` )"'
                           'value="show pdf" />', obj.slug2)

    def pdf_downloader(self, obj):
        return format_html('<input type="button" onclick="window.open(`download_pdf/{}/change/` )"'
                           'value="get pdf" />', obj.slug2)

    class Media:
        js = ("viya1/selectajax.js",)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('open_project/<slug:slug>/change/', self.open_project),
                   path('convert_project/<slug:slug>/change/', self.convert_project),
                   path('download_pdf/<slug:slug>/change/', self.download_pdf),
                   # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
                   ]
        return my_urls + urls

    def open_project(self, request, slug):
        slug_2 = OfferProject.objects.get(slug2=slug)
        photo = OfferProjectPhotosS.objects.filter(offer_project_key=slug_2.id)
        types = OfferProjectRoomType.objects.filter(foreign_key=slug_2.id)
        videos = OfferProjectVideosS.objects.filter(offer_project_key=slug_2.id)
        maps = OfferProjectMapsS.objects.filter(offer_project_key=slug_2.id)

        context = {
            'slug_2': slug_2,
            'photo': photo,
            'types': types,
            'videos': videos,
            'maps': maps,
        }
        return render(request, 'admin/viya1/projects/projects.html', context)
        #  return render(request, 'admin/viya1/projects/blog.html', context)

        # Opens up page as PDF

    def index(request):
        context = {}
        return render(request, 'app/index.html', context)

    def convert_project(self, request, slug, *args, **kwargs):
        slug_2 = OfferProject.objects.get(slug2=slug)
        photo = OfferProjectPhotosS.objects.filter(offer_project_key=slug_2.id)
        types = OfferProjectRoomType.objects.filter(foreign_key=slug_2.id)
        videos = OfferProjectVideosS.objects.filter(offer_project_key=slug_2.id)
        maps = OfferProjectMapsS.objects.filter(offer_project_key=slug_2.id)

        context = {
            'slug_2': slug_2,
            'photo': photo,
            'types': types,
            'videos': videos,
            'maps': maps,
        }

        # pdf =  pdfkit.from_url('http://google.com', 'out.pdf')
        # pdf = pdfkit.from_file('templates/admin/viya1/projects/invoice.html', 'out.pdf')
        # pdf =  pdfkit.from_string('Hello!', 'out.pdf')
        # options = {
        #     "enable-local-file-access": ""
        # }
        options = {
            "enable-local-file-access": "",
            # 'user-style-sheet': css,
            'encoding': 'UTF-8',
            'margin-left': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-top': '0mm'
        }
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        html = loader.render_to_string('admin/viya1/projects/invoice.html', {})  # invoice.html
        output = pdfkit.from_string(html, output_path=False, options=options, configuration=config)
        response = HttpResponse(content_type="application/pdf")
        response.write(output)
        return response

        # pdf = pdfkit.from_url('admin/viya1/projects/invoice.html', context)
        # return HttpResponse(content_type='application/pdf')

        # pdf = render_to_pdf('admin/viya1/projects/pdfs.html', context)
        # return render(request, 'admin/viya1/projects/projects.html', context)

        # pdf = render_to_pdf('admin/viya1/projects/blog.html', context)
        # return HttpResponse(pdf, content_type='application/pdf')

    def download_pdf(self, request, slug, *args, **kwargs):
        slug_2 = OfferProject.objects.get(slug2=slug)
        photo = OfferProjectPhotosS.objects.filter(offer_project_key=slug_2.id)
        types = OfferProjectRoomType.objects.filter(foreign_key=slug_2.id)
        videos = OfferProjectVideosS.objects.filter(offer_project_key=slug_2.id)
        maps = OfferProjectMapsS.objects.filter(offer_project_key=slug_2.id)

        context = {
            'slug_2': slug_2,
            'photo': photo,
            'types': types,
            'videos': videos,
            'maps': maps,
        }

        return render(request, 'admin/viya1/projects/invoice.html', context)


admin.site.register(OfferProject, OfferProjectAdmin)


class OfferCompanyAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['status_of_partner', 'name_of_company', 'year_of_establishment', 'address', 'number_of_project',
                    'description', 'logo', 'website']
    list_per_page = 25


admin.site.register(OfferCompany, OfferCompanyAdmin)


class OfferTypeAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['type_name']


admin.site.register(OfferType, OfferTypeAdmin)
