# Micro-Earthquake-Forecast-using-SAC
EN

The SAC method has been used for detecting seismic precursors. The SAC (Seismic Analysis Code) software package is a powerful tool widely used in seismology for processing and analyzing digital seismic data. It has a rich set of functions for data manipulation, signal processing, and visualization. SAC can be used for detecting and characterizing various seismic signals, including earthquake precursors such as foreshocks, seismic swarms, and anomalous seismic signals. The software package provides a wide range of time series and frequency domain analyses, including spectral analysis, cross-correlation, wavelet transform, and polarization analysis, among others, that can be used to detect and analyze seismic precursors.

Data aquisition

It is difficult to estimate how much data or how many hours of recordings are needed until the detection shows something as it depends on several factors such as the characteristics of the earthquake signals, the noise level, and the sampling rate of the recording.
In general, the longer the recording and the higher the sampling rate, the higher the chances of detecting the earthquake signals. However, it is also important to consider the noise level as high levels of noise can make it harder to detect the earthquake signals.
In addition, the characteristics of the earthquake signals, such as their frequency content and amplitude, can also affect the detection. Some signals may be easier to detect than others depending on their characteristics.
Therefore, it is important to carefully consider these factors and conduct thorough analyses to optimize the chances of detecting earthquake signals. This code seems to be correct and should update the plot and print the remaining time until the next frequency variation every two seconds. However, if the remaining time always returns "inf", it may be because there is not enough data in the SAC file to detect a frequency variation above the threshold. You could try changing the threshold or using a different SAC file with more data to see if that solves the issue.
To modify the chosen threshold, you can simply change the value of the threshold variable in the code. For example, if you want to set the threshold to 20 dB/Hz instead of 10 dB/Hz, you can change the line: threshold = 10  # dB/Hz


About
The code and the file sacsave.py save SAC to file with the trace.write("data.sac", format="SAC") statement writes the data to the file data.sac in SAC format. The format argument of the write method specifies the file format.

The sacforecast.py is used to make frequency analysis in order to retrive the frequency interval until the next seismic event over the written limits in the code.
Note that the STA/LTA ratio calculation is done using the classic_sta_lta function from ObsPy's signal module, which computes the classic short-term average / long-term average ratio for earthquake detection. The remaining time until the next possible event is calculated by comparing the current ratio value to a threshold that is set as three times the standard deviation above the mean of the ratio values. If the current ratio value is above this threshold, the remaining time is labeled as "Possible event".
This code computes the PSD of the first trace in the SAC file, plots the PSD using a logarithmic frequency axis, and then estimates the remaining time until the next frequency variation above a threshold of 10 dB/Hz. If no frequency variation above the threshold is detected, the code prints a message indicating that no event was detected.

Code usage

In order to run this code you will need to import with pip : numpy obspy matplotlib. The code is written in Python 3.8.10, higher version should work also. You NEED TO RON BOTH FILES in order to make detection in real time sacsave.py that is the client who get the miniseed packs fromseedlink server and save them as .SAC and the sacforecast.py that make the analysis and estimate the remaining time.

<img src="https://i.ibb.co/PgjGM3s/image.png">image</img>

RO

Metoda SAC a fost utilizat?? pentru detectarea precursorilor seismici. Pachetul software SAC (Seismic Analysis Code) este un instrument puternic utilizat pe scar?? larg?? ??n seismologie pentru procesarea ??i analiza datelor seismice digitale. Are un set bogat de func??ii pentru manipularea datelor, procesarea semnalului ??i vizualizare. SAC poate fi utilizat pentru detectarea ??i caracterizarea diferitelor semnale seismice, inclusiv precursori de cutremur, cum ar fi ??ocuri seismice, roiuri seismice ??i semnale seismice anormale. Pachetul software ofer?? o gam?? larg?? de analize de serii temporale ??i de frecven????, inclusiv analiz?? spectral??, corela??ie ??ncruci??at??, transformare wavelet ??i analiz?? de polarizare, printre altele, care pot fi utilizate pentru a detecta ??i analiza precursorii seismici.

Data achizitiei

Este dificil de estimat c??te date sau c??te ore de ??nregistr??ri sunt necesare p??n?? c??nd detectarea arat?? ceva, deoarece depinde de mai mul??i factori, cum ar fi caracteristicile semnalelor de cutremur, nivelul de zgomot ??i rata de e??antionare a ??nregistr??rii.
??n general, cu c??t ??nregistrarea este mai lung?? ??i cu c??t rata de e??antionare este mai mare, cu at??t sunt mai mari ??ansele de a detecta semnalele de cutremur. Cu toate acestea, este de asemenea important s?? se ia ??n considerare nivelul de zgomot, deoarece nivelurile ridicate de zgomot pot ??ngreuna detectarea semnalelor de cutremur.
??n plus, caracteristicile semnalelor de cutremur, cum ar fi con??inutul de frecven???? ??i amplitudinea acestora, pot afecta, de asemenea, detectarea. Unele semnale pot fi mai u??or de detectat dec??t altele, ??n func??ie de caracteristicile lor.
Prin urmare, este important s?? lua??i ??n considerare cu aten??ie ace??ti factori ??i s?? efectua??i analize am??nun??ite pentru a optimiza ??ansele de detectare a semnalelor de cutremur. Acest cod pare a fi corect ??i ar trebui s?? actualizeze graficul ??i s?? imprime timpul r??mas p??n?? la urm??toarea varia??ie de frecven???? la fiecare dou?? secunde. Cu toate acestea, dac?? timpul r??mas revine ??ntotdeauna ???inf???, poate fi din cauz?? c?? nu exist?? suficiente date ??n fi??ierul SAC pentru a detecta o varia??ie de frecven???? peste prag. Pute??i ??ncerca s?? schimba??i pragul sau s?? utiliza??i un alt fi??ier SAC cu mai multe date pentru a vedea dac?? asta rezolv?? problema.
Pentru a modifica pragul ales, pute??i modifica pur ??i simplu valoarea variabilei de prag din cod. De exemplu, dac?? dori??i s?? seta??i pragul la 20 dB/Hz ??n loc de 10 dB/Hz, pute??i modifica linia: prag = 10 # dB/Hz


Despre
Codul ??i fi??ierul sacsave.py salveaz?? SAC ??n fi??ier cu instruc??iunea trace.write("data.sac", format="SAC") scrie datele ??n fi??ierul data.sac ??n format SAC. Argumentul format al metodei write specific?? formatul fi??ierului.

Sacforecast.py este folosit pentru a face analize de frecven???? pentru a prelua intervalul de frecven???? p??n?? la urm??torul eveniment seismic peste limitele scrise ??n cod.
Re??ine??i c?? calculul raportului STA/LTA se face folosind func??ia classic_sta_lta din modulul de semnal al ObsPy, care calculeaz?? raportul clasic mediu pe termen scurt / mediu pe termen lung pentru detectarea cutremurului. Timpul r??mas p??n?? la urm??torul eveniment posibil este calculat prin compararea valorii raportului curent cu un prag care este setat ca de trei ori abaterea standard peste media valorilor raportului. Dac?? valoarea raportului curent este peste acest prag, timpul r??mas este etichetat ca ???Eveniment posibil???.
Acest cod calculeaz?? PSD-ul primei urme din fi??ierul SAC, traseaz?? PSD folosind o ax?? de frecven???? logaritmic?? ??i apoi estimeaz?? timpul r??mas p??n?? la urm??toarea varia??ie de frecven???? peste un prag de 10 dB/Hz. Dac?? nu este detectat?? nicio varia??ie de frecven???? peste prag, codul tip??re??te un mesaj care indic?? faptul c?? nu a fost detectat niciun eveniment.

Utilizarea codului

Pentru a rula acest cod, va trebui s?? importa??i cu pip : numpy obspy matplotlib. Codul este scris ??n Python 3.8.10, ar trebui s?? func??ioneze ??i versiunea superioar??. TREBUIE S?? RULEZI AMBELE FI??IERE pentru a putea detecta ??n timp real sacsave.py, adic?? clientul care prime??te pachetele de miniseed de pe serverul seedlink ??i le salveaz?? ca .SAC ??i sacforecast.py care efectueaz?? analiza ??i estimarea timpului r??mas.
