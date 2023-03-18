# Generated by Django 4.1.7 on 2023-03-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0014_brand_categories_alter_brand_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='categories',
            field=models.CharField(blank=True, choices=[('Agricultura, vanatoare si servicii anexe', 'Agricultura, vanatoare si servicii anexe'), ('Silvicultura, exploatare forestiera si servicii anexe', 'Silvicultura, exploatare forestiera si servicii anexe'), ('Pescuitul, piscicultura si serviciile anexe', 'Pescuitul, piscicultura si serviciile anexe'), ('Extractia si prepararea carbunelui', 'Extractia si prepararea carbunelui'), ('Extractia hidrocarburilor si servicii anexe', 'Extractia hidrocarburilor si servicii anexe'), ('Extractia si prepararea minereurilor radioactive', 'Extractia si prepararea minereurilor radioactive'), ('Extractia si prepararea minereurilor metalifere', 'Extractia si prepararea minereurilor metalifere'), ('Alte activitati extractive', 'Alte activitati extractive'), ('Industria alimentara si a bauturilor', 'Industria alimentara si a bauturilor'), ('Fabricarea produselor din tutun', 'Fabricarea produselor din tutun'), ('Fabricarea produselor textile', 'Fabricarea produselor textile'), ('Fabricarea articolelor de imbracaminte; aranjarea si vopsirea blanurilor', 'Fabricarea articolelor de imbracaminte; aranjarea si vopsirea blanurilor'), ('Tabacirea si finisarea pieilor; fabricarea articolelor de voiaj si marochinarie, a harnasamentelor ...', 'Tabacirea si finisarea pieilor; fabricarea articolelor de voiaj si marochinarie, a harnasamentelor ...'), ('Fabricarea lemnului si a produselor din lemn si pluta, cu exceptia mobilei; fabricarea articolelor ...', 'Fabricarea lemnului si a produselor din lemn si pluta, cu exceptia mobilei; fabricarea articolelor ...'), ('Fabricarea celulozei, hartiei si a produselor din hartie', 'Fabricarea celulozei, hartiei si a produselor din hartie'), ('Edituri, poligrafie si reproducerea pe suporti a inregistrarilor', 'Edituri, poligrafie si reproducerea pe suporti a inregistrarilor'), ('Industria de prelucrare a titeiului, cocsificarea carbunelui si tratarea combustibililor nucleari', 'Industria de prelucrare a titeiului, cocsificarea carbunelui si tratarea combustibililor nucleari'), ('Fabricarea substantelor si a produselor chimice', 'Fabricarea substantelor si a produselor chimice'), ('Fabricarea produselor din cauciuc si mase plastice', 'Fabricarea produselor din cauciuc si mase plastice'), ('Fabricarea altor produse din minerale nemetalice', 'Fabricarea altor produse din minerale nemetalice'), ('Industria metalurgica', 'Industria metalurgica'), ('Industria constructiilor metalice si a produselor din metal (exclusiv masini, utilaje si instalatii)', 'Industria constructiilor metalice si a produselor din metal (exclusiv masini, utilaje si instalatii)'), ('Industria de masini si echipamente', 'Industria de masini si echipamente'), ('Industria de mijloace ale tehnicii de calcul si de birou', 'Industria de mijloace ale tehnicii de calcul si de birou'), ('Industria de masini si aparate electrice', 'Industria de masini si aparate electrice'), ('Industria de echipamente pentru radio, televiziune si comunicatii', 'Industria de echipamente pentru radio, televiziune si comunicatii'), ('Industria de aparatura si instrumente medicale, de precizie, optice si fotografice, ceasornicarie', 'Industria de aparatura si instrumente medicale, de precizie, optice si fotografice, ceasornicarie'), ('Industria mijloacelor de transport rutier', 'Industria mijloacelor de transport rutier'), ('Industria altor mijloace de transport n.c.a.', 'Industria altor mijloace de transport n.c.a.'), ('Productia de mobilier si alte activitati industriale n.c.a.', 'Productia de mobilier si alte activitati industriale n.c.a.'), ('Recuperarea deseurilor si resturilor de materiale reciclabile', 'Recuperarea deseurilor si resturilor de materiale reciclabile'), ('Productia si furnizarea de energie electrica si termica, gaze si apa', 'Productia si furnizarea de energie electrica si termica, gaze si apa'), ('Captarea, tratarea si distributia apei', 'Captarea, tratarea si distributia apei'), ('Constructii', 'Constructii'), ('Comert cu ridicata si cu amanuntul, intretinerea si repararea autovehiculelor si a motocicletelor; ...', 'Comert cu ridicata si cu amanuntul, intretinerea si repararea autovehiculelor si a motocicletelor; ...'), ('Comert cu ridicata si servicii de intermediere in comertul cu ridicata (cu exceptia autovehiculelor ...', 'Comert cu ridicata si servicii de intermediere in comertul cu ridicata (cu exceptia autovehiculelor ...'), ('Comert cu amanuntul (cu exceptia autovehiculelor si motocicletelor); repararea bunurilor personale ...', 'Comert cu amanuntul (cu exceptia autovehiculelor si motocicletelor); repararea bunurilor personale ...'), ('Hoteluri si restaurante', 'Hoteluri si restaurante'), ('Transporturi terestre; transporturi prin conducte', 'Transporturi terestre; transporturi prin conducte'), ('Transporturi pe apa', 'Transporturi pe apa'), ('Transporturi aeriene', 'Transporturi aeriene'), ('Activitati anexe si auxiliare de transport, activitati ale agentiilor de turism', 'Activitati anexe si auxiliare de transport, activitati ale agentiilor de turism'), ('Posta si telecomunicatii', 'Posta si telecomunicatii'), ('Intermedieri financiare (cu exceptia activitatilor de asigurari si ale caselor de pensii)', 'Intermedieri financiare (cu exceptia activitatilor de asigurari si ale caselor de pensii)'), ('Activitati de asigurari si ale caselor de pensii (cu exceptia celor din sistemul public de ...', 'Activitati de asigurari si ale caselor de pensii (cu exceptia celor din sistemul public de ...'), ('Activitati auxiliare intermedierilor financiare', 'Activitati auxiliare intermedierilor financiare'), ('Tranzactii imobiliare', 'Tranzactii imobiliare'), ('Inchirierea masinilor si echipamentelor, fara operator si a bunurilor personale si gospodaresti', 'Inchirierea masinilor si echipamentelor, fara operator si a bunurilor personale si gospodaresti'), ('Informatica si activitati conexe', 'Informatica si activitati conexe'), ('Cercetare-dezvoltare', 'Cercetare-dezvoltare'), ('Alte activitati de servicii prestate in principal intreprinderilor', 'Alte activitati de servicii prestate in principal intreprinderilor'), ('Administratie publica si aparare; asigurari sociale din sistemul public', 'Administratie publica si aparare; asigurari sociale din sistemul public'), ('Invatamant', 'Invatamant'), ('Sanatate si asistenta sociala', 'Sanatate si asistenta sociala'), ('Eliminarea deseurilor si a apelor uzate; salubritate si activitati similare', 'Eliminarea deseurilor si a apelor uzate; salubritate si activitati similare'), ('Activitati asociative diverse', 'Activitati asociative diverse'), ('Activitati recreative, culturale si sportive', 'Activitati recreative, culturale si sportive'), ('Alte activitati de servicii personale', 'Alte activitati de servicii personale'), ('Activitati ale personalului angajat in gospodarii personale', 'Activitati ale personalului angajat in gospodarii personale'), ('Activitati desfasurate in gospodarii private, de producere a bunurilor destinate consumului propriu', 'Activitati desfasurate in gospodarii private, de producere a bunurilor destinate consumului propriu'), ('Activitati ale gospodariilor private, de servicii pentru scopuri proprii', 'Activitati ale gospodariilor private, de servicii pentru scopuri proprii'), ('Activitati ale organizatiilor si organismelor extrateritoriale', 'Activitati ale organizatiilor si organismelor extrateritoriale')], max_length=105, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='main_category',
            field=models.CharField(choices=[('Agricultura, vanatoare si servicii anexe', 'Agricultura, vanatoare si servicii anexe'), ('Silvicultura, exploatare forestiera si servicii anexe', 'Silvicultura, exploatare forestiera si servicii anexe'), ('Pescuitul, piscicultura si serviciile anexe', 'Pescuitul, piscicultura si serviciile anexe'), ('Extractia si prepararea carbunelui', 'Extractia si prepararea carbunelui'), ('Extractia hidrocarburilor si servicii anexe', 'Extractia hidrocarburilor si servicii anexe'), ('Extractia si prepararea minereurilor radioactive', 'Extractia si prepararea minereurilor radioactive'), ('Extractia si prepararea minereurilor metalifere', 'Extractia si prepararea minereurilor metalifere'), ('Alte activitati extractive', 'Alte activitati extractive'), ('Industria alimentara si a bauturilor', 'Industria alimentara si a bauturilor'), ('Fabricarea produselor din tutun', 'Fabricarea produselor din tutun'), ('Fabricarea produselor textile', 'Fabricarea produselor textile'), ('Fabricarea articolelor de imbracaminte; aranjarea si vopsirea blanurilor', 'Fabricarea articolelor de imbracaminte; aranjarea si vopsirea blanurilor'), ('Tabacirea si finisarea pieilor; fabricarea articolelor de voiaj si marochinarie, a harnasamentelor ...', 'Tabacirea si finisarea pieilor; fabricarea articolelor de voiaj si marochinarie, a harnasamentelor ...'), ('Fabricarea lemnului si a produselor din lemn si pluta, cu exceptia mobilei; fabricarea articolelor ...', 'Fabricarea lemnului si a produselor din lemn si pluta, cu exceptia mobilei; fabricarea articolelor ...'), ('Fabricarea celulozei, hartiei si a produselor din hartie', 'Fabricarea celulozei, hartiei si a produselor din hartie'), ('Edituri, poligrafie si reproducerea pe suporti a inregistrarilor', 'Edituri, poligrafie si reproducerea pe suporti a inregistrarilor'), ('Industria de prelucrare a titeiului, cocsificarea carbunelui si tratarea combustibililor nucleari', 'Industria de prelucrare a titeiului, cocsificarea carbunelui si tratarea combustibililor nucleari'), ('Fabricarea substantelor si a produselor chimice', 'Fabricarea substantelor si a produselor chimice'), ('Fabricarea produselor din cauciuc si mase plastice', 'Fabricarea produselor din cauciuc si mase plastice'), ('Fabricarea altor produse din minerale nemetalice', 'Fabricarea altor produse din minerale nemetalice'), ('Industria metalurgica', 'Industria metalurgica'), ('Industria constructiilor metalice si a produselor din metal (exclusiv masini, utilaje si instalatii)', 'Industria constructiilor metalice si a produselor din metal (exclusiv masini, utilaje si instalatii)'), ('Industria de masini si echipamente', 'Industria de masini si echipamente'), ('Industria de mijloace ale tehnicii de calcul si de birou', 'Industria de mijloace ale tehnicii de calcul si de birou'), ('Industria de masini si aparate electrice', 'Industria de masini si aparate electrice'), ('Industria de echipamente pentru radio, televiziune si comunicatii', 'Industria de echipamente pentru radio, televiziune si comunicatii'), ('Industria de aparatura si instrumente medicale, de precizie, optice si fotografice, ceasornicarie', 'Industria de aparatura si instrumente medicale, de precizie, optice si fotografice, ceasornicarie'), ('Industria mijloacelor de transport rutier', 'Industria mijloacelor de transport rutier'), ('Industria altor mijloace de transport n.c.a.', 'Industria altor mijloace de transport n.c.a.'), ('Productia de mobilier si alte activitati industriale n.c.a.', 'Productia de mobilier si alte activitati industriale n.c.a.'), ('Recuperarea deseurilor si resturilor de materiale reciclabile', 'Recuperarea deseurilor si resturilor de materiale reciclabile'), ('Productia si furnizarea de energie electrica si termica, gaze si apa', 'Productia si furnizarea de energie electrica si termica, gaze si apa'), ('Captarea, tratarea si distributia apei', 'Captarea, tratarea si distributia apei'), ('Constructii', 'Constructii'), ('Comert cu ridicata si cu amanuntul, intretinerea si repararea autovehiculelor si a motocicletelor; ...', 'Comert cu ridicata si cu amanuntul, intretinerea si repararea autovehiculelor si a motocicletelor; ...'), ('Comert cu ridicata si servicii de intermediere in comertul cu ridicata (cu exceptia autovehiculelor ...', 'Comert cu ridicata si servicii de intermediere in comertul cu ridicata (cu exceptia autovehiculelor ...'), ('Comert cu amanuntul (cu exceptia autovehiculelor si motocicletelor); repararea bunurilor personale ...', 'Comert cu amanuntul (cu exceptia autovehiculelor si motocicletelor); repararea bunurilor personale ...'), ('Hoteluri si restaurante', 'Hoteluri si restaurante'), ('Transporturi terestre; transporturi prin conducte', 'Transporturi terestre; transporturi prin conducte'), ('Transporturi pe apa', 'Transporturi pe apa'), ('Transporturi aeriene', 'Transporturi aeriene'), ('Activitati anexe si auxiliare de transport, activitati ale agentiilor de turism', 'Activitati anexe si auxiliare de transport, activitati ale agentiilor de turism'), ('Posta si telecomunicatii', 'Posta si telecomunicatii'), ('Intermedieri financiare (cu exceptia activitatilor de asigurari si ale caselor de pensii)', 'Intermedieri financiare (cu exceptia activitatilor de asigurari si ale caselor de pensii)'), ('Activitati de asigurari si ale caselor de pensii (cu exceptia celor din sistemul public de ...', 'Activitati de asigurari si ale caselor de pensii (cu exceptia celor din sistemul public de ...'), ('Activitati auxiliare intermedierilor financiare', 'Activitati auxiliare intermedierilor financiare'), ('Tranzactii imobiliare', 'Tranzactii imobiliare'), ('Inchirierea masinilor si echipamentelor, fara operator si a bunurilor personale si gospodaresti', 'Inchirierea masinilor si echipamentelor, fara operator si a bunurilor personale si gospodaresti'), ('Informatica si activitati conexe', 'Informatica si activitati conexe'), ('Cercetare-dezvoltare', 'Cercetare-dezvoltare'), ('Alte activitati de servicii prestate in principal intreprinderilor', 'Alte activitati de servicii prestate in principal intreprinderilor'), ('Administratie publica si aparare; asigurari sociale din sistemul public', 'Administratie publica si aparare; asigurari sociale din sistemul public'), ('Invatamant', 'Invatamant'), ('Sanatate si asistenta sociala', 'Sanatate si asistenta sociala'), ('Eliminarea deseurilor si a apelor uzate; salubritate si activitati similare', 'Eliminarea deseurilor si a apelor uzate; salubritate si activitati similare'), ('Activitati asociative diverse', 'Activitati asociative diverse'), ('Activitati recreative, culturale si sportive', 'Activitati recreative, culturale si sportive'), ('Alte activitati de servicii personale', 'Alte activitati de servicii personale'), ('Activitati ale personalului angajat in gospodarii personale', 'Activitati ale personalului angajat in gospodarii personale'), ('Activitati desfasurate in gospodarii private, de producere a bunurilor destinate consumului propriu', 'Activitati desfasurate in gospodarii private, de producere a bunurilor destinate consumului propriu'), ('Activitati ale gospodariilor private, de servicii pentru scopuri proprii', 'Activitati ale gospodariilor private, de servicii pentru scopuri proprii'), ('Activitati ale organizatiilor si organismelor extrateritoriale', 'Activitati ale organizatiilor si organismelor extrateritoriale')], max_length=105),
        ),
    ]