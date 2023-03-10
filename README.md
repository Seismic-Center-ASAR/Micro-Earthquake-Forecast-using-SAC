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

Metoda SAC a fost utilizată pentru detectarea precursorilor seismici. Pachetul software SAC (Seismic Analysis Code) este un instrument puternic utilizat pe scară largă în seismologie pentru procesarea și analiza datelor seismice digitale. Are un set bogat de funcții pentru manipularea datelor, procesarea semnalului și vizualizare. SAC poate fi utilizat pentru detectarea și caracterizarea diferitelor semnale seismice, inclusiv precursori de cutremur, cum ar fi șocuri seismice, roiuri seismice și semnale seismice anormale. Pachetul software oferă o gamă largă de analize de serii temporale și de frecvență, inclusiv analiză spectrală, corelație încrucișată, transformare wavelet și analiză de polarizare, printre altele, care pot fi utilizate pentru a detecta și analiza precursorii seismici.

Data achizitiei

Este dificil de estimat câte date sau câte ore de înregistrări sunt necesare până când detectarea arată ceva, deoarece depinde de mai mulți factori, cum ar fi caracteristicile semnalelor de cutremur, nivelul de zgomot și rata de eșantionare a înregistrării.
În general, cu cât înregistrarea este mai lungă și cu cât rata de eșantionare este mai mare, cu atât sunt mai mari șansele de a detecta semnalele de cutremur. Cu toate acestea, este de asemenea important să se ia în considerare nivelul de zgomot, deoarece nivelurile ridicate de zgomot pot îngreuna detectarea semnalelor de cutremur.
În plus, caracteristicile semnalelor de cutremur, cum ar fi conținutul de frecvență și amplitudinea acestora, pot afecta, de asemenea, detectarea. Unele semnale pot fi mai ușor de detectat decât altele, în funcție de caracteristicile lor.
Prin urmare, este important să luați în considerare cu atenție acești factori și să efectuați analize amănunțite pentru a optimiza șansele de detectare a semnalelor de cutremur. Acest cod pare a fi corect și ar trebui să actualizeze graficul și să imprime timpul rămas până la următoarea variație de frecvență la fiecare două secunde. Cu toate acestea, dacă timpul rămas revine întotdeauna „inf”, poate fi din cauză că nu există suficiente date în fișierul SAC pentru a detecta o variație de frecvență peste prag. Puteți încerca să schimbați pragul sau să utilizați un alt fișier SAC cu mai multe date pentru a vedea dacă asta rezolvă problema.
Pentru a modifica pragul ales, puteți modifica pur și simplu valoarea variabilei de prag din cod. De exemplu, dacă doriți să setați pragul la 20 dB/Hz în loc de 10 dB/Hz, puteți modifica linia: prag = 10 # dB/Hz


Despre
Codul și fișierul sacsave.py salvează SAC în fișier cu instrucțiunea trace.write("data.sac", format="SAC") scrie datele în fișierul data.sac în format SAC. Argumentul format al metodei write specifică formatul fișierului.

Sacforecast.py este folosit pentru a face analize de frecvență pentru a prelua intervalul de frecvență până la următorul eveniment seismic peste limitele scrise în cod.
Rețineți că calculul raportului STA/LTA se face folosind funcția classic_sta_lta din modulul de semnal al ObsPy, care calculează raportul clasic mediu pe termen scurt / mediu pe termen lung pentru detectarea cutremurului. Timpul rămas până la următorul eveniment posibil este calculat prin compararea valorii raportului curent cu un prag care este setat ca de trei ori abaterea standard peste media valorilor raportului. Dacă valoarea raportului curent este peste acest prag, timpul rămas este etichetat ca „Eveniment posibil”.
Acest cod calculează PSD-ul primei urme din fișierul SAC, trasează PSD folosind o axă de frecvență logaritmică și apoi estimează timpul rămas până la următoarea variație de frecvență peste un prag de 10 dB/Hz. Dacă nu este detectată nicio variație de frecvență peste prag, codul tipărește un mesaj care indică faptul că nu a fost detectat niciun eveniment.

Utilizarea codului

Pentru a rula acest cod, va trebui să importați cu pip : numpy obspy matplotlib. Codul este scris în Python 3.8.10, ar trebui să funcționeze și versiunea superioară. TREBUIE SĂ RULEZI AMBELE FIȘIERE pentru a putea detecta în timp real sacsave.py, adică clientul care primește pachetele de miniseed de pe serverul seedlink și le salvează ca .SAC și sacforecast.py care efectuează analiza și estimarea timpului rămas.
