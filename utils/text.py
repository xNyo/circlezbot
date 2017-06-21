from emoji import emojize

START = emojize("""
:waving_hand: *Benvenuto su Circle Pay Italia Bot!*

:thinking_face: *Cos'è Circle?*
*Circle* è una piattaforma di chat istantanea e *condivisione di denaro*, a cui viene associata una carta di debito o di credito (Postepay, Hype, Visa, ecc...).
Potrete gratuitamente inviare soldi con un semplice messaggio, come fosse Telegram o WhatsApp. Il servizio, disponibile sia sul sito web che in app, è *totalmente gratuito* e non comporta costi di gestione (né mensili né annuali), di prelievo, di deposito o di transazione. Tutto totalmente gratuito e senza nessun vincolo contrattuale.

Circle offre la possibilità ai propri utenti registrati di *invitare degli amici* a registrarsi a sua volta, ripagando della registrazione sia l'utente che invita e sia colui che si registra. In che modo? Semplice, facciamo un esempio:
*Io*, utente registrato, *invito un mio amico tramite link di invito* o codice referral (che il mio amico inserirà al momento della registrazione). Una volta registrato *io invierò a lui 5 euro*, li riceverà in modo istantaneo e *lui invierà questi 5 euro nuovamente a me*. _Gli stessi 5 euro._
Si esegue questa operazione di transazione per *5 volte, sempre gli stessi 5 euro iniziali*, i quali, terminata la procedura, torneranno al mittente iniziale.
Terminata questa operazione, e tornati al mittente i 5 euro iniziali, *Circle invierà altri 5 euro* sia al primo utente che al secondo appena registrato. *Ed ecco qui: 5 euro gratis per voi.*
Questa operazione si può fare solo tra un utente già registrato e un utente che si vuole registrare, ed è per questo che *è strettamente necessario inserire un codice referral al momento della registrazione*.

:money_bag: *Come fa a guadagnarci? È sicuro?*
È un'azienda che da anni vanta *milioni di utenti* in tutto il mondo, dotata dei più alti livelli di sicurezza informatica al mondo, premiata più volte da numerosi articoli di giornali (NY Times, Wired, ecc...) che potete trovare facilmente su internet.
Circle guadagna sulla *transazione stessa*, lo spostamento di denaro virtuale genera profitto così come lo spostamento di denaro tramite bancomat genera profitto per la banca. Vi consigliamo di leggere la sezione _"La Società" - "Il Servizio"_ all'interno del loro sito web, per chi volesse ulteriormente approfondire.

_NB: Come esplicitato nel regolamento è severamente proibito "fare i furbi" e intascarsi i 5 euro iniziali oppure creare una catena familiare solo per intascarsi i soldi, pena: chiusura istantanea del conto da parte dell'azienda._
_Questo perchè lo scopo dell'azienda non è far arricchire i furbi ma permettere una condivisione più semplice del denaro e, tramite questo servizio supplementare, far crescere la community al di fuori della propria cerchia familiare._


:money-mouth_face: *Vuoi ricevere i tuoi 5€ tramite Circle?*
:backhand_index_pointing_down: *Clicca sul pulsante qui sotto!* :backhand_index_pointing_down:
""")

ADMIN_REFERRAL_NOTIFY = emojize("""
:money_with_wings: *Qualcuno ha usato il tuo referral!* #cinqueeuroezpz

{} {}
@{} `[{}]`
""")

INSTRUCTIONS = emojize("""
:spiral_notepad: *ISTRUZIONI*

*1.* *Registrati* su circle tramite [questo link](https://www.circle.com/invite/{code}) _(o tramite il pulsante in fondo a questo messaggio)_
*2.* Inserite nei campi appositi: nome, cognome, email e password.
*3.* Una volta registrati arriverà una notifica a noi admin, *vi contatteremo in privato su Circle* per iniziare la procedura.
*4.* *Collega la tua carta di credito o carta Hype* _(va bene anche una Postepay)_ dal sito di Circle.
*5.* *Vi invieremo*, tramite chat privata, *5 euro*. Voi dovrete *rimandare questi 5 euro al mittente*. Eseguita questa operazione per 5 volte, Circle caricherà 5 euro sia a voi che al proprietario del codice.
*6.* Una volta ricevuti i 5€, clicca sul pulsante *"Ho ricevuto i miei 5€" sotto a questo messaggio.*

_NB: È una procedura che si può eseguire un'unica volta con un nuovo utente, registrato con un codice referral. Non si possono eseguire con utenti già registrati. Siete liberi però di trovare per conto vostro tutti gli amici che volete, facendoli registrare con il vostro codice (o link di invito) ed eseguendo questa stessa transazione._
""")

ALREADY_USED = emojize("""
:warning: *ATTENZIONE!*
Hai già richiesto un referral per registrarti, non puoi registrare più di un account!
""")

DONE = emojize("""
:thumbs_up: *Ottimo!* Puoi invitare altre persone a registrarsi su Circle con il tuo link d'invito che trovi su Circle!

_Sei stato rimosso dal gruppo di Circle Pay Italia per aver completato correttamente la procedura, alla prossima!_

:backhand_index_pointing_down: *Altri link utili* :backhand_index_pointing_down:
""")

INSTRUCTIONS_WARNING = emojize("""
:warning: *Attenzione!* Se decidi di proseguire, assicurati di:
*1.* Avere a disposizione *in questo momento* di una carta di credito, una Postepay o una carta Hype *anche senza denaro al suo interno*
*2.* Essere sicuro al *100%* di voler effettuare questa procedura _(richiede 5 minuti ed il bonus di 5€ è garantito, senza spese)_
*3.* *Non essere già registrato a Circle*, poichè è possibile ottenere il bonus di 5€ solo per i nuovi account
""")

STOP = emojize("""
:raised_hand: *Va bene*, puoi ritornare da me quando vuoi!
Usa il comando /start per avviare nuovamente il bot.
""")
