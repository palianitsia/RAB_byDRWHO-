# RAB_byDRWHO-
Il bot creato è un tool automatizzato per registrazioni multiple sul sito Bidoo (sia versione italiana che spagnola).
È stato sviluppato utilizzando Python e la libreria Playwright per interagire con le pagine web in modalità mobile. La GUI (Graphical User Interface) è costruita con Tkinter e offre diverse opzioni configurabili dall'utente. Ecco una panoramica dettagliata di cosa fa esattamente il bot:

Funzionalità Principali
Registrazione Automatica:

Il bot può effettuare una o più registrazioni automatiche sul sito Bidoo, a seconda delle impostazioni dell'utente.
L'utente può scegliere tra la versione italiana (it.bidoo.com) e la versione spagnola (es.bidoo.com) del sito.
Può generare automaticamente un'email, un nome utente e una password casuali per ogni registrazione.
Supporto Proxy e VPN:

Proxy: Se l'utente sceglie di effettuare registrazioni multiple, il bot può utilizzare un proxy diverso per ogni registrazione, selezionato casualmente da una lista predefinita.
VPN: Il bot supporta l'uso di VPN (NordVPN, ExpressVPN, SharkVPN). Se l'utente attiva l'opzione VPN, il bot avvierà la VPN selezionata, cambierà il paese di connessione ad ogni registrazione e utilizzerà la VPN per navigare su Bidoo.
Interfaccia Utente:

L'utente può configurare diverse opzioni tramite una semplice GUI:
Lingua: Selezionare la lingua (italiano o spagnolo) per l'interfaccia utente e per il sito di registrazione.
Email: Decidere se utilizzare un'email personalizzata o generata automaticamente.
Username: Decidere se utilizzare un nome utente personalizzato o generato automaticamente.
Link di Invito: Inserire un link di invito, se disponibile.
Registrazioni Multiple: Specificare il numero di registrazioni da eseguire.
VPN: Selezionare se utilizzare una VPN e quale VPN utilizzare.
Salvataggio dei Dati:

Dopo ogni registrazione, i dati dell'account (email, nome utente, password) vengono salvati in un file acc.txt, in modo che l'utente possa accedere facilmente ai dati degli account creati.
Feedback e Notifiche:

Dopo aver completato tutte le registrazioni richieste, il bot mostra un popup di conferma indicando che le registrazioni sono state completate con successo.
Come Utilizzare il Bot
Configurare le Opzioni:

Apri il bot e configura le opzioni desiderate nella GUI.
Se vuoi utilizzare una VPN, seleziona la VPN dalla lista e fornisci il percorso del file eseguibile della VPN.
Avviare le Registrazioni:

Clicca su "Registrati" per avviare il processo di registrazione. Il bot eseguirà le registrazioni, cambiando il proxy o il paese della VPN ad ogni iterazione, a seconda delle impostazioni scelte.
Visualizzare i Risultati:

Dopo che tutte le registrazioni sono state completate, i dati degli account creati saranno salvati in acc.txt e un popup ti informerà del completamento.



 ____  ______        ___   _  ___ ___ _ 
|  _ \|  _ \ \      / / | | |/ _ \__ \ |
| | | | |_) \ \ /\ / /| |_| | | | |/ / |
| |_| |  _ < \ V  V / |  _  | |_| |_||_|
|____/|_| \_\ \_/\_/  |_| |_|\___/(_)(_)




                                        
Crea un file requirements.txt per installare tutte le dipendenze necessarie:
playwright==1.29.0
tkinter

Istruzioni per l'Installazione e l'Esecuzione
Clonare il repository o scaricare i file reg_acc.py e requirements.txt nel tuo sistema.

Installare le dipendenze: Apri un terminale nella directory dove si trovano i file e esegui:
pip install -r requirements.txt

Inizializzare Playwright: Esegui il seguente comando per installare i browser necessari per Playwright:
python -m playwright install

Eseguire il Bot: Avvia il bot eseguendo il file reg_acc.py:
python reg_acc.py

Questo bot è ora pronto per essere utilizzato per eseguire registrazioni automatizzate su Bidoo, con opzioni di personalizzazione per la lingua, l'uso di proxy, VPN e altro ancora.
