# Generated by Django 4.1.7 on 2023-03-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0011_alter_brand_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='city',
            field=models.CharField(choices=[('Alba, Abrud', 'Alba, Abrud'), ('Alba, Abrud-Sat', 'Alba, Abrud-Sat'), ('Alba, Achimetesti', 'Alba, Achimetesti'), ('Alba, Acmariu', 'Alba, Acmariu'), ('Alba, Aiud', 'Alba, Aiud'), ('Alba, Aiudul-de-Sus', 'Alba, Aiudul-de-Sus'), ('Alba, Albac', 'Alba, Albac'), ('Alba, Alba-Iulia', 'Alba, Alba-Iulia'), ('Alba, Alecus', 'Alba, Alecus'), ('Alba, Almasu-de-Mijloc', 'Alba, Almasu-de-Mijloc'), ('Alba, Almasu-Mare', 'Alba, Almasu-Mare'), ('Alba, Ampoita', 'Alba, Ampoita'), ('Alba, Anghelesti', 'Alba, Anghelesti'), ('Alba, Arieseni', 'Alba, Arieseni'), ('Alba, Aronesti', 'Alba, Aronesti'), ('Alba, Arti', 'Alba, Arti'), ('Alba, Asinip', 'Alba, Asinip'), ('Alba, Avramesti-Arieseni', 'Alba, Avramesti-Arieseni'), ('Alba, Avramesti', 'Alba, Avramesti')], max_length=100),
        ),
        migrations.AlterField(
            model_name='brand',
            name='country',
            field=models.CharField(choices=[('Andorra', 'Andorra'), ('Emiratele', 'Emiratele'), ('Afganistan', 'Afganistan'), ('Antigua', 'Antigua'), ('Anguilla', 'Anguilla'), ('Albania', 'Albania'), ('Armenia', 'Armenia'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('Argentina', 'Argentina'), ('Samoa', 'Samoa'), ('Austria', 'Austria'), ('Australia', 'Australia'), ('Aruba', 'Aruba'), ('Insulele', 'Insulele'), ('Azerbaidjan', 'Azerbaidjan'), ('Bosnia', 'Bosnia'), ('Barbados', 'Barbados'), ('Bangladesh', 'Bangladesh'), ('Belgia', 'Belgia'), ('Burkina', 'Burkina'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Saint-Barthélemy', 'Saint-Barthélemy'), ('Bermuda', 'Bermuda'), ('Brunei', 'Brunei'), ('Bolivia', 'Bolivia'), ('Brazilia', 'Brazilia'), ('Bahamas', 'Bahamas'), ('Bhutan', 'Bhutan'), ('Insula', 'Insula'), ('Botswana', 'Botswana'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Canada', 'Canada'), ('Insulele', 'Insulele'), ('Republica', 'Republica'), ('Republica', 'Republica'), ('Congo', 'Congo'), ('Elveția', 'Elveția'), ('Côte', 'Côte'), ('Insulele', 'Insulele'), ('Chile', 'Chile'), ('Camerun', 'Camerun'), ('China', 'China'), ('Columbia', 'Columbia'), ('Clipperton', 'Clipperton'), ('Costa', 'Costa'), ('Cuba', 'Cuba'), ('Cabo', 'Cabo'), ('Curaçao', 'Curaçao'), ('Insula', 'Insula'), ('Cipru', 'Cipru'), ('Cehia', 'Cehia'), ('Germania', 'Germania'), ('Djibouti', 'Djibouti'), ('Danemarca', 'Danemarca'), ('Dominica', 'Dominica'), ('Republica', 'Republica'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Estonia', 'Estonia'), ('Egipt', 'Egipt'), ('Sahara', 'Sahara'), ('Grecia', 'Grecia'), ('Eritreea', 'Eritreea'), ('Spania', 'Spania'), ('Etiopia', 'Etiopia'), ('Finlanda', 'Finlanda'), ('Fiji', 'Fiji'), ('Insulele', 'Insulele'), ('Micronezia', 'Micronezia'), ('Insulele', 'Insulele'), ('Franța', 'Franța'), ('Gabon', 'Gabon'), ('Grenada', 'Grenada'), ('Georgia', 'Georgia'), ('Guyana', 'Guyana'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Groenlanda', 'Groenlanda'), ('Gambia', 'Gambia'), ('Guineea', 'Guineea'), ('Guadelupa', 'Guadelupa'), ('Guineea', 'Guineea'), ('Georgia', 'Georgia'), ('Guatemala', 'Guatemala'), ('Guam', 'Guam'), ('Guineea-Bissau', 'Guineea-Bissau'), ('Guyana', 'Guyana'), ('Hong', 'Hong'), ('Insula', 'Insula'), ('Honduras', 'Honduras'), ('Croația', 'Croația'), ('Haiti', 'Haiti'), ('Ungaria', 'Ungaria'), ('Indonezia', 'Indonezia'), ('Irlanda', 'Irlanda'), ('Israel', 'Israel'), ('Insula', 'Insula'), ('India', 'India'), ('Teritoriul', 'Teritoriul'), ('Irak', 'Irak'), ('Iran', 'Iran'), ('Islanda', 'Islanda'), ('Italia', 'Italia'), ('Jersey', 'Jersey'), ('Jamaica', 'Jamaica'), ('Iordania', 'Iordania'), ('Japonia', 'Japonia'), ('Kenya', 'Kenya'), ('Kârgâzstan', 'Kârgâzstan'), ('Cambodgia', 'Cambodgia'), ('Kiribati', 'Kiribati'), ('Comore', 'Comore'), ('Saint', 'Saint'), ('Coreea', 'Coreea'), ('Coreea', 'Coreea'), ('Kuweit', 'Kuweit'), ('Insulele', 'Insulele'), ('Kazahstan', 'Kazahstan'), ('Laos', 'Laos'), ('Liban', 'Liban'), ('Saint', 'Saint'), ('Liechtenstein', 'Liechtenstein'), ('Sri', 'Sri'), ('Liberia', 'Liberia'), ('Lesotho', 'Lesotho'), ('Lituania', 'Lituania'), ('Luxemburg', 'Luxemburg'), ('Letonia', 'Letonia'), ('Libia', 'Libia'), ('Maroc', 'Maroc'), ('Monaco', 'Monaco'), ('Moldova', 'Moldova'), ('Muntenegru', 'Muntenegru'), ('Saint-Martin', 'Saint-Martin'), ('Madagascar', 'Madagascar'), ('Insulele', 'Insulele'), ('Macedonia', 'Macedonia'), ('Mali', 'Mali'), ('Myanmar/Birmania', 'Myanmar/Birmania'), ('Mongolia', 'Mongolia'), ('Macao', 'Macao'), ('Insulele', 'Insulele'), ('Martinica', 'Martinica'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Malta', 'Malta'), ('Mauritius', 'Mauritius'), ('Maldive', 'Maldive'), ('Malawi', 'Malawi'), ('Mexic', 'Mexic'), ('Malaysia', 'Malaysia'), ('Mozambic', 'Mozambic'), ('Namibia', 'Namibia'), ('Noua', 'Noua'), ('Niger', 'Niger'), ('Insula', 'Insula'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Țările', 'Țările'), ('Norvegia', 'Norvegia'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('Noua', 'Noua'), ('Oman', 'Oman'), ('Panama', 'Panama'), ('Peru', 'Peru'), ('Polinezia', 'Polinezia'), ('Papua-Noua', 'Papua-Noua'), ('Filipine', 'Filipine'), ('Pakistan', 'Pakistan'), ('Polonia', 'Polonia'), ('Saint-Pierre', 'Saint-Pierre'), ('Insulele', 'Insulele'), ('Puerto', 'Puerto'), ('Portugalia', 'Portugalia'), ('Palau', 'Palau'), ('Paraguay', 'Paraguay'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Serbia', 'Serbia'), ('Rusia', 'Rusia'), ('Rwanda', 'Rwanda'), ('Arabia', 'Arabia'), ('Insulele', 'Insulele'), ('Seychelles', 'Seychelles'), ('Sudan', 'Sudan'), ('Suedia', 'Suedia'), ('Singapore', 'Singapore'), ('Sfânta', 'Sfânta'), ('Slovenia', 'Slovenia'), ('Svalbard', 'Svalbard'), ('Slovacia', 'Slovacia'), ('Sierra', 'Sierra'), ('San', 'San'), ('Senegal', 'Senegal'), ('Somalia', 'Somalia'), ('Suriname', 'Suriname'), ('Sudanul', 'Sudanul'), ('São', 'São'), ('El', 'El'), ('Sint-Maarten', 'Sint-Maarten'), ('Siria', 'Siria'), ('Eswatini', 'Eswatini'), ('Insulele', 'Insulele'), ('Ciad', 'Ciad'), ('Teritoriile', 'Teritoriile'), ('Togo', 'Togo'), ('Thailanda', 'Thailanda'), ('Tadjikistan', 'Tadjikistan'), ('Tokelau', 'Tokelau'), ('Timorul', 'Timorul'), ('Turkmenistan', 'Turkmenistan'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('Turcia', 'Turcia'), ('Trinidad', 'Trinidad'), ('Tuvalu', 'Tuvalu'), ('Taiwan', 'Taiwan'), ('Tanzania', 'Tanzania'), ('Ucraina', 'Ucraina'), ('Uganda', 'Uganda'), ('Regatul', 'Regatul'), ('Insulele', 'Insulele'), ('Statele', 'Statele'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Sfântul', 'Sfântul'), ('Saint', 'Saint'), ('Venezuela', 'Venezuela'), ('Insulele', 'Insulele'), ('Insulele', 'Insulele'), ('Vietnam', 'Vietnam'), ('Vanuatu', 'Vanuatu'), ('Wallis', 'Wallis'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('Mayotte', 'Mayotte'), ('Africa', 'Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50),
        ),
    ]