# Generated by Django 4.1.7 on 2023-03-18 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0028_alter_brand_created_at_alter_brand_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='city',
            field=models.CharField(choices=[('Bucuresti', 'Bucuresti'), ('Abrud', 'Abrud'), ('Adjud', 'Adjud'), ('Agnita', 'Agnita'), ('Aiud', 'Aiud'), ('Alba Iulia', 'Alba Iulia'), ('Alesd', 'Alesd'), ('Alexandria', 'Alexandria'), ('Amara', 'Amara'), ('Anina', 'Anina'), ('Aninoasa', 'Aninoasa'), ('Arad', 'Arad'), ('Ardud', 'Ardud'), ('Avrig', 'Avrig'), ('Azuga', 'Azuga'), ('Babadag', 'Babadag'), ('Babeni', 'Babeni'), ('Bacau', 'Bacau'), ('Baia de Arama', 'Baia de Arama'), ('Baia de Aries', 'Baia de Aries'), ('Baia Mare', 'Baia Mare'), ('Baia Sprie', 'Baia Sprie'), ('Baicoi', 'Baicoi'), ('Baile Govora', 'Baile Govora'), ('Baile Herculane', 'Baile Herculane'), ('Baile Olanesti', 'Baile Olanesti'), ('Bailesti', 'Bailesti'), ('Baile Tusnad', 'Baile Tusnad'), ('Balan', 'Balan'), ('Balcesti', 'Balcesti'), ('Bals', 'Bals'), ('Baneasa', 'Baneasa'), ('Baraolt', 'Baraolt'), ('Barlad', 'Barlad'), ('Bechet', 'Bechet'), ('Beclean', 'Beclean'), ('Beius', 'Beius'), ('Berbesti', 'Berbesti'), ('Beresti', 'Beresti'), ('Bicaz', 'Bicaz'), ('Bistrita', 'Bistrita'), ('Blaj', 'Blaj'), ('Bocsa', 'Bocsa'), ('Boldesti-Scaeni', 'Boldesti-Scaeni'), ('Bolintin-Vale', 'Bolintin-Vale'), ('Borsa', 'Borsa'), ('Borsec', 'Borsec'), ('Botosani', 'Botosani'), ('Brad', 'Brad'), ('Bragadiru', 'Bragadiru'), ('Braila', 'Braila'), ('Brasov', 'Brasov'), ('Breaza', 'Breaza'), ('Brezoi', 'Brezoi'), ('Brosteni', 'Brosteni'), ('Bucecea', 'Bucecea'), ('Bucuresti', 'Bucuresti'), ('Budesti', 'Budesti'), ('Buftea', 'Buftea'), ('Buhusi', 'Buhusi'), ('Bumbesti-Jiu', 'Bumbesti-Jiu'), ('Busteni', 'Busteni'), ('Buzau', 'Buzau'), ('Buzias', 'Buzias'), ('Cajvana', 'Cajvana'), ('Calafat', 'Calafat'), ('Calan', 'Calan'), ('Calarasi', 'Calarasi'), ('Calimanesti', 'Calimanesti'), ('Campeni', 'Campeni'), ('Campia Turzii', 'Campia Turzii'), ('Campina', 'Campina'), ('Campulung', 'Campulung'), ('Campulung Moldovenesc', 'Campulung Moldovenesc'), ('Caracal', 'Caracal'), ('Caransebes', 'Caransebes'), ('Carei', 'Carei'), ('Cavnic', 'Cavnic'), ('Cazanesti', 'Cazanesti'), ('Cehu Silvaniei', 'Cehu Silvaniei'), ('Cernavoda', 'Cernavoda'), ('Chisineu-Cris', 'Chisineu-Cris'), ('Chitila', 'Chitila'), ('Ciacova', 'Ciacova'), ('Cisnadie', 'Cisnadie'), ('Cluj-Napoca', 'Cluj-Napoca'), ('Codlea', 'Codlea'), ('Comanesti', 'Comanesti'), ('Comarnic', 'Comarnic'), ('Constanta', 'Constanta'), ('Copsa Mica', 'Copsa Mica'), ('Corabia', 'Corabia'), ('Costesti', 'Costesti'), ('Covasna', 'Covasna'), ('Craiova', 'Craiova'), ('Cristuru Secuiesc', 'Cristuru Secuiesc'), ('Cugir', 'Cugir'), ('Curtea de Arges', 'Curtea de Arges'), ('Curtici', 'Curtici'), ('Dabuleni', 'Dabuleni'), ('Darabani', 'Darabani'), ('Darmanesti', 'Darmanesti'), ('Dej', 'Dej'), ('Deta', 'Deta'), ('Deva', 'Deva'), ('Dolhasca', 'Dolhasca'), ('Dorohoi', 'Dorohoi'), ('Draganesti-Olt', 'Draganesti-Olt'), ('Dragasani', 'Dragasani'), ('Dragomiresti', 'Dragomiresti'), ('Drobeta-Turnu Severin', 'Drobeta-Turnu Severin'), ('Dumbraveni', 'Dumbraveni'), ('Eforie', 'Eforie'), ('Fagaras', 'Fagaras'), ('Faget', 'Faget'), ('Falticeni', 'Falticeni'), ('Faurei', 'Faurei'), ('Fetesti', 'Fetesti'), ('Fieni', 'Fieni'), ('Fierbinti-Targ', 'Fierbinti-Targ'), ('Filiasi', 'Filiasi'), ('Flamanzi', 'Flamanzi'), ('Focsani', 'Focsani'), ('Frasin', 'Frasin'), ('Fundulea', 'Fundulea'), ('Gaesti', 'Gaesti'), ('Galati', 'Galati'), ('Gataia', 'Gataia'), ('Geoagiu', 'Geoagiu'), ('Gheorgheni', 'Gheorgheni'), ('Gherla', 'Gherla'), ('Ghimbav', 'Ghimbav'), ('Giurgiu', 'Giurgiu'), ('Gura Humorului', 'Gura Humorului'), ('Harlau', 'Harlau'), ('Harsova', 'Harsova'), ('Hateg', 'Hateg'), ('Horezu', 'Horezu'), ('Huedin', 'Huedin'), ('Hunedoara', 'Hunedoara'), ('Husi', 'Husi'), ('Ianca', 'Ianca'), ('Iasi', 'Iasi'), ('Iernut', 'Iernut'), ('Ineu', 'Ineu'), ('Insuratei', 'Insuratei'), ('Intorsura Buzaului', 'Intorsura Buzaului'), ('Isaccea', 'Isaccea'), ('Jibou', 'Jibou'), ('Jimbolia', 'Jimbolia'), ('Lehliu Gara', 'Lehliu Gara'), ('Lipova', 'Lipova'), ('Liteni', 'Liteni'), ('Livada', 'Livada'), ('Ludus', 'Ludus'), ('Lugoj', 'Lugoj'), ('Lupeni', 'Lupeni'), ('Macin', 'Macin'), ('Magurele', 'Magurele'), ('Mangalia', 'Mangalia'), ('Marasesti', 'Marasesti'), ('Marghita', 'Marghita'), ('Medgidia', 'Medgidia'), ('Medias', 'Medias'), ('Miercurea Ciuc', 'Miercurea Ciuc'), ('Miercurea Nirajului', 'Miercurea Nirajului'), ('Miercurea Sibiului', 'Miercurea Sibiului'), ('Mihailesti', 'Mihailesti'), ('Milisauti', 'Milisauti'), ('Mioveni', 'Mioveni'), ('Mizil', 'Mizil'), ('Moinesti', 'Moinesti'), ('Moldova Noua', 'Moldova Noua'), ('Moreni', 'Moreni'), ('Motru', 'Motru'), ('Murfatlar', 'Murfatlar'), ('Murgeni', 'Murgeni'), ('Nadlac', 'Nadlac'), ('Nasaud', 'Nasaud'), ('Navodari', 'Navodari'), ('Negresti', 'Negresti'), ('Negresti-Oas', 'Negresti-Oas'), ('Negru Voda', 'Negru Voda'), ('Nehoiu', 'Nehoiu'), ('Novaci', 'Novaci'), ('Nucet', 'Nucet'), ('Ocna Mures', 'Ocna Mures'), ('Ocna Sibiului', 'Ocna Sibiului'), ('Ocnele Mari', 'Ocnele Mari'), ('Odobesti', 'Odobesti'), ('Odorheiu Secuiesc', 'Odorheiu Secuiesc'), ('Oltenita', 'Oltenita'), ('Onesti', 'Onesti'), ('Oradea', 'Oradea'), ('Orastie', 'Orastie'), ('Oravita', 'Oravita'), ('Orsova', 'Orsova'), ('Otelu Rosu', 'Otelu Rosu'), ('Otopeni', 'Otopeni'), ('Ovidiu', 'Ovidiu'), ('Panciu', 'Panciu'), ('Pancota', 'Pancota'), ('Pantelimon', 'Pantelimon'), ('Pascani', 'Pascani'), ('Patarlagele', 'Patarlagele'), ('Pecica', 'Pecica'), ('Petrila', 'Petrila'), ('Petrosani', 'Petrosani'), ('Piatra-Olt', 'Piatra-Olt'), ('Piatra Neamt', 'Piatra Neamt'), ('Pitesti', 'Pitesti'), ('Ploiesti', 'Ploiesti'), ('Plopeni', 'Plopeni'), ('Podu Iloaiei', 'Podu Iloaiei'), ('Pogoanele', 'Pogoanele'), ('Popesti-Leordeni', 'Popesti-Leordeni'), ('Potcoava', 'Potcoava'), ('Predeal', 'Predeal'), ('Pucioasa', 'Pucioasa'), ('Racari', 'Racari'), ('Radauti', 'Radauti'), ('Ramnicu Sarat', 'Ramnicu Sarat'), ('Ramnicu Valcea', 'Ramnicu Valcea'), ('Rasnov', 'Rasnov'), ('Recas', 'Recas'), ('Reghin', 'Reghin'), ('Resita', 'Resita'), ('Roman', 'Roman'), ('Rosiorii de Vede', 'Rosiorii de Vede'), ('Rovinari', 'Rovinari'), ('Roznov', 'Roznov'), ('Rupea', 'Rupea'), ('Sacele', 'Sacele'), ('Sacueni', 'Sacueni'), ('Salcea', 'Salcea'), ('Saliste', 'Saliste'), ('Salistea de Sus', 'Salistea de Sus'), ('Salonta', 'Salonta'), ('Sangeorgiu de Padure', 'Sangeorgiu de Padure'), ('Sangeorz-Bai', 'Sangeorz-Bai'), ('Sannicolau Mare', 'Sannicolau Mare'), ('Santana', 'Santana'), ('Sarmasu', 'Sarmasu'), ('Satu Mare', 'Satu Mare'), ('Saveni', 'Saveni'), ('Scornicesti', 'Scornicesti'), ('Sebes', 'Sebes'), ('Sebis', 'Sebis'), ('Segarcea', 'Segarcea'), ('Seini', 'Seini'), ('Sfantu Gheorghe', 'Sfantu Gheorghe'), ('Sibiu', 'Sibiu'), ('Sighetu Marmatiei', 'Sighetu Marmatiei'), ('Sighisoara', 'Sighisoara'), ('Simeria', 'Simeria'), ('Sinaia', 'Sinaia'), ('Siret', 'Siret'), ('Slanic', 'Slanic'), ('Slanic-Moldova', 'Slanic-Moldova'), ('Slatina', 'Slatina'), ('Slobozia', 'Slobozia'), ('Solca', 'Solca'), ('Somcuta Mare', 'Somcuta Mare'), ('Sovata', 'Sovata'), ('Stefanesti', 'Stefanesti'), ('Stefanesti', 'Stefanesti'), ('Stei', 'Stei'), ('Strehaia', 'Strehaia'), ('Suceava', 'Suceava'), ('Sulina', 'Sulina'), ('Talmaciu', 'Talmaciu'), ('Tandarei', 'Tandarei'), ('Targoviste', 'Targoviste'), ('Targu Bujor', 'Targu Bujor'), ('Targu Carbunesti', 'Targu Carbunesti'), ('Targu Frumos', 'Targu Frumos'), ('Targu Jiu', 'Targu Jiu'), ('Targu Lapus', 'Targu Lapus'), ('Targu Mures', 'Targu Mures'), ('Targu Neamt', 'Targu Neamt'), ('Targu Ocna', 'Targu Ocna'), ('Targu Secuiesc', 'Targu Secuiesc'), ('Tarnaveni', 'Tarnaveni'), ('Tasnad', 'Tasnad'), ('Tautii-Magheraus', 'Tautii-Magheraus'), ('Techirghiol', 'Techirghiol'), ('Tecuci', 'Tecuci'), ('Teius', 'Teius'), ('Ticleni', 'Ticleni'), ('Timisoara', 'Timisoara'), ('Tismana', 'Tismana'), ('Titu', 'Titu'), ('Toplita', 'Toplita'), ('Topoloveni', 'Topoloveni'), ('Tulcea', 'Tulcea'), ('Turceni', 'Turceni'), ('Turda', 'Turda'), ('Turnu Magurele', 'Turnu Magurele'), ('Ulmeni', 'Ulmeni'), ('Ungheni', 'Ungheni'), ('Uricani', 'Uricani'), ('Urlati', 'Urlati'), ('Urziceni', 'Urziceni'), ('Valea lui Mihai', 'Valea lui Mihai'), ('Valenii de Munte', 'Valenii de Munte'), ('Vanju Mare', 'Vanju Mare'), ('Vascau', 'Vascau'), ('Vaslui', 'Vaslui'), ('Vatra Dornei', 'Vatra Dornei'), ('Vicovu de sus', 'Vicovu de sus'), ('Victoria', 'Victoria'), ('Videle', 'Videle'), ('Viseu de Sus', 'Viseu de Sus'), ('Vlahita', 'Vlahita'), ('Voluntari', 'Voluntari'), ('Vulcan', 'Vulcan'), ('Zalau', 'Zalau'), ('Zarnesti', 'Zarnesti'), ('Zimnicea', 'Zimnicea'), ('Zlatna', 'Zlatna'), ('Simleu Silvaniei', 'Simleu Silvaniei')], default='Bucuresti', max_length=100),
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 19, 23, 22, 77111)),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 19, 23, 22, 77111)),
        ),
    ]
