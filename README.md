# XAI_project

🎯 Obiettivo principale
	•	Creare un dataset che evidenzi bias comuni (es. colori di sfondo, contesti ambientali).
	•	Utilizzare quel dataset per testare un modello (o più modelli) e misurare le attivazioni (logits) per ogni classe.
	•	Generare un report per ciascuna classe, che mostri in che misura il modello è influenzato dai bias presenti.

⸻

🧠 Fase 1: Costruzione del dataset
	1.	Definisci le caratteristiche su cui indagare:
	•	Ad esempio: sfondi (urbano, naturale, monocromo), dominanza di un colore (rosso, blu, verde), presenza di oggetti secondari (macchine, piante, persone).
	2.	Crea o raccogli immagini che coprano sistematicamente queste caratteristiche:
	•	Puoi usare StableDiffusion o altre tecniche per generare le immagini con prompt come “a dog on a red background”, “a cat in an urban environment”, ecc.
	3.	Organizza il dataset in modo comparabile:
	•	Ad esempio 100 immagini di cani su sfondo rosso, 100 su sfondo blu, 100 in ambiente urbano, ecc.
	•	Le “classi” qui possono essere le entità da classificare (es. cane, gatto) o più semplicemente varianti di bias se vuoi studiare un solo soggetto.

⸻

🧪 Fase 2: Testing e misurazione attivazioni
	1.	Passa le immagini attraverso il tuo modello (o modelli):
	•	Ottieni il vettore di logits (valori prima del softmax) per ciascuna immagine.
	2.	Registra le attivazioni:
	•	Per ogni immagine e per ciascuna classe considerata, misura l’attivazione (logit).
	3.	Organizza i dati:
	•	Per ogni classe target (es. “cane”), metti in relazione l’attivazione media con la caratteristica bias (es. sfondo rosso vs blu vs urbano).

⸻

🧾 Fase 3: Generazione report automatici con LLM
	1.	Prepara un prompt per un LLM (es. GPT-4):
	•	Il prompt potrebbe includere una tabella (CSV o JSON) con colonne:
	•	immagine ID, classe vera, caratteristica (tipo di bias), logits classe1, logits classe2, …
	•	Istruzioni del prompt:

“Ecco i logits aggregati dal modello su un dataset diviso per bias.
 Per ciascuna classe (es. cane, gatto, auto…), analizza se ci sono differenze di attivazione
 legate al colore di sfondo o al contesto. Evidenzia tendenze, bias, suggerimenti su robustezza.”


	2.	Ricevi in output il report:
	•	LLM ti fornisce una narrazione per ogni classe, es.:
	•	“Il modello attiva ‘cane’ più forte con sfondo rosso (+1.2 logit) rispetto al blu (+0.8)…”
	•	“Il bias è evidente: +0.4 logit significa che tende a preferire il rosso”.

⸻

✅ Risultati attesi
	•	Due report:
	•	Modello biasato (es. addestrato con immagini sbilanciate).
	•	Modello senza bias (es. bilanciato o addestrato apposta).
	•	I report devono mostrare comparativamente la sensibilità ai bias:
	•	Quale classe è più influenzata da cambi di colore/sfondo.
	•	Quanto variano i logits tra condizioni.

⸻

📌 In sintesi cosa devi fare
	1.	Progetta e costruisci un dataset pilota con vari livelli di bias (ad es. cani su sfondi diversi).
	2.	Esegui il modello sul dataset, estraendo i logits per ogni immagine/classe.
	3.	Aggrega i dati (medie, deviazioni) strutturandoli in un formato tabellare.
	4.	Invia i dati tabellari e le istruzioni a un LLM per ottenere il report finale.
	5.	Confronta i report tra il modello biasato e quello “corretto” per dimostrare validità del sistema.
