from random import randint as rand
intrebari=[
    ["Razboi",
    "Câte stele sunt pe bretelele unui căpitan de armată?",#1 4
    "Cum se numește partea capului unui cartuș de pușcă de luptă sau pistol?",#2 Glonţ
    "Unde poartă militarii epoleți?",#3 pe umeri
    "Cum se numește culoarea de camuflaj a echipamentelor și uniformelor militare?",#4 Camuflaj
    "Ce primeste cel mai des militarul fara rand?",#5 Imbracaminte
    "Ce trebuie să intreprinda un recrut pentru a deveni un soldat deplin?",#6  jurământ militar
    "Cum se numește un avion de luptă pentru combaterea aeronavelor inamice?",#7 Avion de vânătoare
    "La ce grad militar următor poate fi prezentat un colonel?",#8 General maior
    "Cum se numește o mare formație de nave de război de diferite clase?",#9 Escadron
    "Cum erau încărcate tunurile pentru a distruge infanteria?"#10 Buckshot
    ],
    ["Geografie",
    "În ce oraș din America de Sud se află statuia de 38 de metri a lui Isus Hristos?",#1 Rio de Janeiro
    "Care oraș a fost ținta tuturor cruciadelor?",#2 Ierusalim
    "Care republică a fost abolită în URSS în 1924?",#3 Khorezm
    "Care este alt nume pentru Țările de Jos?",#4 Olanda
    "Cum se numeau coloniștii din ținuturile nedescoperite ale Americii? ",#5 Pionierii
    "În ce oraș se afla una dintre cele șapte minuni ale lumii, Grădinile Babilonului?",#6  Babilon
    "Ce zonă din New York este pe insulă?",#7  Manhattan
    "Cum se numește cel mai mare oraș din China?",#8 Shanghai
    "Cine urma să descopere India, dar a descoperit America?",#9  Cristofor Columb
    "Care este capitala Romaniei?",#10 Bucuresti
    ],
    ["Stiinte",
    "Cum se numește mișcarea ordonată a particulelor încărcate?",#1 curent electric 
    "Care dintre acești mari oameni de știință a descoperit radioactivitatea uraniului?",#2 A. Becquerel
    "Care este principala materie primă utilizată în exploatarea centralelor nucleare?",#3 Uranus
    "Cum se numește instrumentul medical folosit pentru a asculta inima și plămânii?",#4 Stetoscop
    "Ce scară este folosită pentru a măsura puterea cutremurelor?",#5 scara Richter
    "Ce disciplină științifică se ocupă cu studiul traiectoriei de zbor a unui glonț tras dintr-un pistol sau un pistol?",#6 Balistică
    "Cum se numește procesul de curățare a instrumentelor chirurgicale?",#7 Sterilizarea
    "Cum se măsoară volumul?",#8 În decibeli
    "Ce este insolația?",#9 lumina directă a soarelui
    "Care os este cel mai bun depozit de ADN?"#10 Coloana vertebrală
    ],
    ["Plante",
    "Ce plantă se numește „trandafir sălbatic”?",#1 Măceșul
    "Care este fructul pomului de pepene galben?",#2 Papaya
    "Ce culoare au trandafirii cu cel mai puternic parfum?",#3 alb
    "Ce este bambusul?",#4 Iarbă
    "Cum se numesc plantele care supraviețuiesc atașându-se de o altă plantă și hrănindu-se cu ea?",#5 parazite
    "Cărei familii de plante aparține trifoiul?",#6 Leguminoase
    "Culoare fistic?",#7 verde deschis
    "Ce fel de legumă este napul?",#8 Ridiche
    "Hibrid de piersici și măr",#9 Nectarine 
    "Care floare, ca floarea soarelui, se întoarce mereu spre soare?",#10 Lotus
    ],
    ["Animale",
    "Cine pe vremuri în Rusia era numit mistreț?",#1 Vier
    "Cum l-au numit respectuos locuitorii Siberiei ursul brun?",#2 Detinatorul la Taiga
    "Cine se numește Toptygin în basmele rusești?",#3 Urs
    "Cum se numea calul preferat al lui Petru I?",#4 Lisetta
    "Ce animal rus a devenit simbolul Jocurilor Olimpice XXII organizate la Moscova în 1980?",#5 Ursuletul Misa
    "Ce pasăre se numește „cântăreața câmpurilor rusești”?",#6 alarcă
    "Rinocerul are coarne care sunt făcute din ce?",#7 Par
    "Cât timp își digeră mâncarea un leneș?",#8 Doua saptamani
    "Lemurii sunt originari dintr-o singură țară, care este?",#9 Madagascar
    "Care este singurul șarpe veninos din Marea Britanie?",#10 Sumator
    ]
    
    ]
raspunsuri=[["","4","Glonţ","Pe umeri","Camuflaj","Imbracaminte","Jurământ militar","Avion de vânătoare","General maior","Escadron","Buckshot"],
            ["","Rio de Janeiro","Ierusalim","Khorezm","Olanda","Pionierii","Babilon","Manhattan","Shanghai","Cristofor Columb","Bucuresti"],
            ["","Curent electric ","A.Becquerel","Uraniu","Stetoscop","Scara Richter","Balistică","Sterilizarea","În decibeli","Lumina directă a soarelui","Coloana vertebrală"],
            ["","Măceșul","Papaya","Alb","Iarbă","Parazite","Leguminoase","Verde deschis","Ridiche","Nectarine","Lotus"],
            ["","Vier","Detinatorul la Taiga","Urs","Lisetta","Ursuletul Misa","Alarcă","Păr","Doua saptamani","Madagascar","Sumator"],
]
def milioner():
    n=0
    tema=rand(0,4)
    intrebare=rand(1,10)
    intrebari_puse=[]
    print("Tema:",intrebari[tema][0])  
    while n<10:
        n+=1
        while intrebare in intrebari_puse:
            intrebare=rand(1,10)

        intrebari_puse.append(intrebare)
        print(intrebari[tema][intrebare]) 
        input("Pentru a afla raspunsul tastati ENTER")
        print(raspunsuri[tema][intrebare])
        print("\n")
    return print("Sfarsit de joaca!")
milioner()