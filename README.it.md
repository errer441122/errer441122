🇬🇧 [Read in English](https://github.com/errer441122)

# Riccardo Capanna

Formazione in Digital Marketing (Digital Marketing BSc · 24ORE Business School), con focus su **Marketing & Revenue Operations, gestione del CRM, automazione dei processi con l'AI (n8n) e visibilità nelle ricerche AI (GEO / AEO)**.

Lavoro sui vuoti tra un programma e l'altro, dove i team B2B perdono senza accorgersene attribuzione, recapito delle email, rispetto dei consensi o velocità della pipeline commerciale. Uso **n8n** per automatizzare i processi ed **Excel** (senza macro) per riconciliare l'attribuzione: prima le regole fisse, l'AI solo dove serve leggere testo libero, e audit reali quando ci sono dati pubblici.

---

## Progetti principali

Ogni progetto porta prima alla pagina in italiano, poi al codice.

| Ambito | Progetto | Cosa risolve |
| --- | --- | --- |
| **Recapito delle email e DNS** | **[Sender Domain Health](https://errer441122.github.io/sender-domain-health/?lang=it)** · [codice](https://github.com/errer441122/sender-domain-health) | Controlla SPF, DKIM e DMARC dal DNS pubblico e avvisa quando cambiano. Niente AI. Eseguito su 23 domini reali (7 aziende B2B italiane su 20 tengono DMARC solo in monitoraggio). |
| **Controllo prima degli invii B2B, con AI** | **[B2B Pre-Send Hold & Triage](https://errer441122.github.io/ecommerce-cx-analytics/?lang=it)** · [codice](https://github.com/errer441122/ecommerce-cx-analytics) | Incrocia destinatari, consensi, ticket dell'assistenza e ordini del gestionale prima di un invio B2B; ferma tutta l'azienda per partita IVA o dominio. L'AI legge solo i ticket senza categoria e può fermare, mai far passare. 48 casi sporchi + 48.000 destinatari casuali, eseguito in n8n 2.48.7. |
| **Attribuzione dalla campagna all'ordine** | **[B2B Campaign-to-Order Reconciliation](https://errer441122.github.io/digital-campaign-performance-dashboard/?lang=it)** · [codice](https://github.com/errer441122/digital-campaign-performance-dashboard) | Foglio Excel senza macro che incrocia lead delle campagne, contatti del CRM e ordini del gestionale con 8 regole fisse (partita IVA o dominio, note di credito, clienti già attivi o nuovi, finestra di 180 giorni) e passa i casi dubbi a una persona indicata per nome. 60 casi sporchi, 368 controlli. |
| **Visibilità nelle ricerche AI (GEO / AEO)** | **[AI Visibility Audit](https://errer441122.github.io/ai-visibility-audit-geo/?lang=it)** · [codice](https://github.com/errer441122/ai-visibility-audit-geo) | Misura quanto spesso Gemini, GPT, Perplexity e Claude consigliano un marchio e quali fonti citano. Audit reale: Notion su 3 motori + confronto dei `robots.txt` di 5 marchi. |
| **Smistamento dei contatti e pulizia del CRM** | **[AI Inbound Lead Router](https://errer441122.github.io/ai-inbound-lead-router/?lang=it)** · [codice](https://github.com/errer441122/ai-inbound-lead-router) | Valuta con l'AI i contatti in arrivo e li smista in HubSpot senza sovrascrivere i contatti già seguiti dai venditori né gli UTM della prima campagna. L'AI deve citare le parole con cui il cliente chiede un lavoro, altrimenti decide una persona. 23 scenari eseguiti in n8n 2.48.7; 30 casi e 51 messaggi mai visti misurati con un piccolo modello locale. |
| **Email del ciclo di vita e consenso** | **[Klaviyo Lifecycle Lab](https://errer441122.github.io/klaviyo-lifecycle-lab/?lang=it)** · [codice](https://github.com/errer441122/klaviyo-lifecycle-lab) | Flussi di benvenuto (con doppio consenso), carrello abbandonato e riattivazione inviati davvero da un negozio Shopify di prova, più strumenti nel browser per il controllo prima dell'invio, le fasi del cliente legate al consenso e i tempi del secondo ordine. Un iscritto di prova, nessuna vendita: dimostra il meccanismo, non risultati commerciali. |

> *Nota sui nomi dei repository:* gli indirizzi `ecommerce-cx-analytics` e `digital-campaign-performance-dashboard` restano gli stessi perché i link stampati sul CV continuino a funzionare; tutti e due contengono, in `analisi-cv/`, le analisi su dati pubblici citate nel CV, accanto ai nuovi sistemi B2B.

---

## Strumenti e piattaforme

- **Automazione dei processi e AI:** n8n (workflow JSON da importare, monitoraggio degli errori, webhook e moduli), prompt strutturati con risposta in JSON, controlli con una persona nel mezzo (l'AI ferma o prepara una bozza, non invia mai da sola)
- **CRM, attribuzione e recapito delle email:** HubSpot (contatti, proprietà, campi che spettano ai venditori, UTM di prima e ultima campagna), riconciliazione tra campagne B2B e gestionale (Excel, senza macro), consensi GDPR e liste di esclusione, autenticazione DNS (SPF, DKIM, DMARC), Klaviyo e Shopify
- **Ricerca AI (GEO / AEO) e analisi:** audit di visibilità su più motori AI (ChatGPT, Gemini, Perplexity, Claude), regole `robots.txt` per i crawler AI, fonti mancanti e mappa per la digital PR, GA4, Google Search Console
- **Operazioni:** avvisi su Slack, workflow di errore in n8n, gestione operativa di fiere ed eventi, procedure e playbook

---

## Come lavoro

1. **Progettare per i dati sporchi e gli errori, non per il caso perfetto.** Ogni progetto mette alla prova gli errori del suo processo: date rotte, doppioni, partite IVA e domini che non coincidono, consensi in conflitto tra programmi diversi, contatti già seguiti dai venditori, siti irraggiungibili, AI poco sicura, export mancanti.
2. **Prima le regole fisse, l'AI solo per giudicare, l'ultima parola a una persona.** I controlli fissi stanno in formule Excel o in codice semplice; l'AI legge testo libero solo dove le regole si fermano, e non può mai approvare un invio né sovrascrivere i dati dei venditori.
3. **Dire chiaramente cosa è reale e cosa è simulato.** Reale: controlli DNS dal vivo su 23 domini reali, audit GEO dal vivo, appunti dal campo su Klaviyo, Shopify e DNS. Simulato (e dichiarato): l'attribuzione B2B (60 casi sporchi / 368 controlli), il controllo prima degli invii B2B (48 casi sporchi / 48.000 destinatari casuali), il lead router (30 casi e 51 messaggi) e i fogli per gli eventi. Ogni repository dichiara i suoi limiti.

---

## Altri strumenti e analisi di riferimento

- **Eventi B2B — [Appuntamenti allo stand e follow-up](https://github.com/errer441122/eventi-b2b-agenda-e-follow-up)**: due fogli Excel senza macro per fiere e open day: spostare le visite allo stand senza perdere la prenotazione originale, tenere traccia di chi va ancora avvisato, dividere i contatti dopo l'evento tra Vendite, Eventi, Verifica CRM ed Esclusi.
- **RFM, coorti e CLV nel retail (5.878 clienti, UCI Online Retail II):** dentro [digital-campaign-performance-dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard#lanalisi-del-mio-cv) · [report interattivo](https://errer441122.github.io/digital-campaign-performance-dashboard/analysis.html) (in inglese)
- **Ritardi di consegna e soddisfazione dei clienti (95.639 recensioni, Olist):** dentro [ecommerce-cx-analytics](https://github.com/errer441122/ecommerce-cx-analytics#lanalisi-del-mio-cv)

---

## Contatti

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
