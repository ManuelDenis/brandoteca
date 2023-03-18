from django import forms
from djrichtextfield.widgets import RichTextWidget
import DataChoices.country
from brand.models import Newsletter, Brand
from bt import settings


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']


class BrandForm(forms.ModelForm):
    name = forms.CharField(
        label='Nume brand',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Brand', 'class': 'form-control'}),
        help_text='<ht>Denumirea brandului(Maxim 64 caractere)</ht>'
    )
    type = forms.ChoiceField(
        label='Tip brand',
        choices=settings.BRAND_TYPES,
        widget=forms.Select(attrs={
            'class': 'bootstrap-select',
        }),
        help_text='<ht>Tipul brandului</ht>'
    )
    founding_year = forms.ChoiceField(
        label='An aparitie brand',
        choices=settings.FOUNDING_YEAR,
        help_text='<ht>Anul infiintarii brandului</ht>'
    )
    motto = forms.ChoiceField(
        label='Slogan',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Slogan'}),
        help_text='<ht>Sloganul brandului. Maxim 200 caractere</ht>'
    )
    main_category = forms.ChoiceField(
        label='Categorie principala',
        choices=DataChoices.country.BRAND_CATEGORY,
        widget=forms.Select(attrs={'placeholder': 'Tip brand*'}),
        help_text='<ht>Categoria principala a brandului</ht>'
    )
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=DataChoices.country.BRAND_CATEGORY,
        label='Categorii suplimentare',
        help_text='<ht>Adauga categorii suplimentare</ht>'
    )
    description = forms.CharField(
        widget=RichTextWidget(),
        help_text='<ht>Text ce va fi afișat în pagina brandului. Trebuie să aibă între 300 și 2000 de caractere.</ht>'
    )

    entity = forms.CharField(
        label='Denumirea identitatii juridice*',
        required=True,
        help_text='<ht>Numele complet al firmei. Max 200 caractere.</ht>',
        widget=forms.TextInput(attrs={'placeholder': 'denumire'})
    )
    vat_number = forms.CharField(
        label='Cod unic de inregistrare(CUI)*',
        required=True,
        help_text='<ht>CUI</ht>',
        widget=forms.TextInput(attrs={'placeholder': 'CUI'})
    )
    reg_no = forms.CharField(
        label='Nr. de ordine la Reg. Comertului*',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'numar'}),
        help_text='<ht>Numarul de ordine la Registrul Comertului</ht>'
    )
    euid = forms.CharField(
        label='Identificator unic la nivel european(EUID)',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'EUID'}),
        help_text='<ht>Cod unic european</ht>'
    )
    address = forms.CharField(
        label='Adresa sediului',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'adresa'}),
        help_text='<ht>Adresa sediului social. Max 255 caractere</ht>'
    )
    city = forms.ChoiceField(
        label='Orasul sediului*',
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Alege oras'}),
        choices=DataChoices.country.ORASE,
        help_text='<ht>Orasul in care se afla sediul social</ht>'
    )
    country = forms.ChoiceField(
        label='Tara*',
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Alege tara'}),
        choices=DataChoices.country.COUNTRY,
        help_text='<ht>Tara</ht>'
    )
    email = forms.EmailField(
        label='Adresa de email*',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'email@email.ro'}),
        help_text='<ht>Email de contact. Max 254 caractere</ht>'
    )
    phone = forms.CharField(
        label='Numar de telefon*',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '07...'}),
        help_text='<ht>Telefonul de contact. Fix 10 caractere</ht>'
    )

    website = forms.URLField(
        label='Website',
        widget=forms.URLInput(attrs={'placeholder': 'website-ul brandului'}),
        help_text='<ht>Site web. Maxim 200 caractere</ht>'
    )
    video_url = forms.URLField(
        label='Video de prezentare',
        widget=forms.URLInput(attrs={'placeholder': 'link de pe youtube'}),
        help_text='<ht>Link catre un clip de prezentare a brandului de pe Youtube. Maxim 200 caractere</ht>'
    )
    facebook = forms.URLField(
        label='URL Facebook',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de facebook'}),
        help_text='<ht>Link Facebook. Max 200 caractere</ht>'
    )
    youtube = forms.URLField(
        label='URL YouTube',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de youtube'}),
        help_text='<ht>Un canal Youtube. Max 200 caractere</ht>'
    )
    linkedin = forms.URLField(
        label='URL Linkedin',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de linkedin'}),
        help_text='<ht>Link Linkedin. Max 200 caractere.</ht>'
    )
    instagram = forms.URLField(
        label='URL Instagram',
        widget=forms.URLInput(attrs={'placeholder': 'pagina de instagram'}),
        help_text='<ht>Link Instagram. Max 200 caractere</ht>'
    )






    class Meta:
        model = Brand
        exclude = ['user', 'id', 'is_verified', 'slug', 'created_at', 'updated_at', 'is_active', 'is_verified', 'is_premium', 'is_brand_of_the_month']

