from django import forms
from ckeditor.widgets import CKEditorWidget
import DataChoices.country
from brand.models import Newsletter, Brand, Categories
from cloudinary.forms import CloudinaryFileField


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']


class BrandForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        max_length=64,
        label='Nume brand',
        widget=forms.TextInput(attrs={'placeholder': 'Brand', 'class': 'form-control'}),
        help_text='<ht>Denumirea brandului(Maxim 64 caractere)</ht>',
    )

    type = forms.ChoiceField(
        required=False,
        label='Tip brand',
        choices=DataChoices.country.BRAND_TYPES,
        widget=forms.Select(attrs={
            'class': 'bootstrap-select',
        }),
        help_text='<ht>Tipul brandului</ht>'
    )
    founding_year = forms.ChoiceField(
        required=False,
        label='An aparitie brand',
        choices=DataChoices.country.FOUNDING_YEAR,
        help_text='<ht>Anul infiintarii brandului</ht>'
    )
    motto = forms.CharField(
        required=False,
        label='Slogan',
        widget=forms.TextInput(attrs={'placeholder': 'Slogan'}),
        help_text='<ht>Sloganul brandului. Maxim 200 caractere</ht>'
    )
    main_category = forms.ChoiceField(
        required=False,
        label='Categorie principala',
        choices=DataChoices.country.BRAND_CATEGORY,
        widget=forms.Select(attrs={'placeholder': 'Tip brand*'}),
        help_text='<ht>Categoria principala a brandului</ht>'
    )
    categories = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        queryset=Categories.objects.all(),
        label='Categorii suplimentare',
        help_text='<ht>Adauga categorii suplimentare</ht>'
    )
    description = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label='',
        help_text='<ht>Text ce va fi afișat în pagina brandului. Trebuie să aibă între 300 și 2000 de caractere.</ht>'
    )

    entity = forms.CharField(
        required=False,
        label='Denumirea identitatii juridice',
        help_text='<ht>Numele complet al firmei. Max 200 caractere.</ht>',
        widget=forms.TextInput(attrs={'placeholder': 'denumire'})
    )
    vat_number = forms.CharField(
        required=False,
        label='Cod unic de inregistrare(CUI)',
        help_text='<ht>CUI</ht>',
        widget=forms.TextInput(attrs={'placeholder': 'CUI'})
    )
    reg_no = forms.CharField(
        required=False,
        label='Nr. de ordine la Reg. Comertului',
        widget=forms.TextInput(attrs={'placeholder': 'numar'}),
        help_text='<ht>Numarul de ordine la Registrul Comertului</ht>'
    )
    euid = forms.CharField(
        required=False,
        label='Identificator unic la nivel european(EUID)',
        widget=forms.TextInput(attrs={'placeholder': 'EUID'}),
        help_text='<ht>Cod unic european</ht>'
    )
    address = forms.CharField(
        required=False,
        label='Adresa sediului',
        widget=forms.TextInput(attrs={'placeholder': 'adresa'}),
        help_text='<ht>Adresa sediului social. Max 255 caractere</ht>'
    )
    city = forms.ChoiceField(
        required=False,
        label='Orasul sediului',
        widget=forms.Select(attrs={'placeholder': 'Alege oras'}),
        choices=DataChoices.country.ORASE,
        help_text='<ht>Orasul in care se afla sediul social</ht>'
    )
    country = forms.ChoiceField(
        required=False,
        label='Tara',
        widget=forms.Select(attrs={'placeholder': 'Alege tara'}),
        choices=DataChoices.country.COUNTRY,
        help_text='<ht>Tara</ht>'
    )
    email = forms.EmailField(
        required=False,
        label='Adresa de email',
        widget=forms.EmailInput(attrs={'placeholder': 'email@email.ro'}),
        help_text='<ht>Email de contact. Max 254 caractere</ht>'
    )
    phone = forms.CharField(
        required=False,
        label='Numar de telefon',
        widget=forms.TextInput(attrs={'placeholder': '07...'}),
        help_text='<ht>Telefonul de contact. Fix 10 caractere</ht>'
    )

    website = forms.URLField(
        required=False,
        label='Website',
        widget=forms.URLInput(attrs={'placeholder': 'website-ul brandului'}),
        help_text='<ht>Site web. Maxim 200 caractere</ht>'
    )
    video_url = forms.URLField(
        required=False,
        label='Video de prezentare',
        widget=forms.URLInput(attrs={'placeholder': 'link de pe youtube'}),
        help_text='<ht>Link catre un clip de prezentare a brandului de pe Youtube. Maxim 200 caractere</ht>'
    )
    facebook = forms.URLField(
        required=False,
        label='URL Facebook',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de facebook'}),
        help_text='<ht>Link Facebook. Max 200 caractere</ht>'
    )
    youtube = forms.URLField(
        required=False,
        label='URL YouTube',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de youtube'}),
        help_text='<ht>Un canal Youtube. Max 200 caractere</ht>'
    )
    linkedin = forms.URLField(
        required=False,
        label='URL Linkedin',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de linkedin'}),
        help_text='<ht>Link Linkedin. Max 200 caractere.</ht>'
    )
    instagram = forms.URLField(
        required=False,
        label='URL Instagram',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de instagram'}),
        help_text='<ht>Link Instagram. Max 200 caractere</ht>'
    )
    cover = CloudinaryFileField(
        required=False,
    )
    logo = CloudinaryFileField(
        required=False,
    )

    terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = Brand
        fields = ['name', 'motto', 'founding_year',
                  'address', 'email', 'phone', 'entity', 'vat_number', 'reg_no', 'euid',
                  'website', 'video_url', 'facebook', 'youtube', 'linkedin', 'instagram',
                  'type', 'main_category', 'categories', 'country', 'city', 'terms',
                  'cover', 'logo', 'description']
