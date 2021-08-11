
Wizard.objects.create(name="Hermione Granger", house="Gryffindor", pet="Crookshanks",year="5")
Wizard.objects.create(name="Harry Potter", house="Gryffindor", pet="Hedwig",year="5")



Wizard.objects.get(id=1)

Wizard.objects.filter(house='Gryffindor')


wizupdate = Wizard.objects.get(id=1)

wizupdate.year = '6'


#INSERT INTO Wizard(name,house,pet,year) VALUES ('Luna Lovegood','Ravenclaw','None','4');
#INSERT INTO Wizard(name,house,pet,year) VALUES ('Padma Patil','Ravenclaw','None','5');
#SELECT * FROM Wizard WHERE house = 'Ravenclaw';
#UPDATE Wizard SET year = '5' WHERE name = 'Luna Lovegood'