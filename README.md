# CSGames-2024-Chatbot
## Quelle(s) technique(s) avez-vous utilisé? / What technic(s) did you use?

Pour parvenir à un résultat juste et efficace nous utilisons un ensemble de technique. La première méthode utilisé est la méthode par instruction. En étant clair sur notre intention de recevoir un diagnostique de la par du chatbot celui-ci ajuste sa réponse pour donné un verdict. Pour ne pas abruter ça réponse il est important de ne pas le demander initialement, car celui-ci pourrait tenter de terminer la convertation avec son diagnostique. 

	Pour faciliter la remise du diagnostique nous utilison une seconde technique 	celle du choix multiples. Lorsque nous avons soumis sufisament d’information  	au chatbot sur nos symptômes nous lui posons la question : “With the given 	symptom should I consult a doctor or not?

	La dernière technique qui agit tout au long de l’intervention est l’approche 	contextuel. En réutilisant les informations précédentes nous sommes en 	mesure je posés des question qui récupère toute les informations aquis. 
      
    • Complétion de texte / Text completion prompts
    • Basé sur des instructions / Instruction-based prompts
    • Choix multiples / Multiple-choice prompts
    • Contextuel / Contextual prompts
    • Atténuation des biais / Bias mitigation prompts
    • Mise au point / Fine-tuning and interactive prompts
    • Autre / Other ________________________________
## Quel(s) paramètre(s) avez-vous configuré(s)? / What parameters did you use?
    • Top K  – number : 1
    • Top P – number : N/A
    • Temperature – number : 0,1
    • Max New Tokens – number : 75
    • Do Sample – Default | True | False
    • Return Text - Default | True | False
    • Return Full Text – Default | True | False
    • Return Tensors - Default | True | False
    • Clean Up Tokenization Spaces - Default | True | False
    • Prefix – string : You are my medical assistant.
    • Handle Long Generation - Default | None| Hole
    • Autre / Other ________________________________
Décrire l’incidence du paramètrage si utilisé / Describe the impact of the parameters if used


      Top K  n = 1:  Nous traitons seulement la meilleure réponse du modèle. Au risque de pouvoir sonner répétitif, car le chatbot peux répondre 2 fois la même chose à une question d’usage nous simplifions le traitement des réponses retourner.

Temperature = 0,1 : Nous croyons que l’hyper-paramètre de température doit rester bas. Puisque nous travaillons avec des donnés médicals et potentiellement la vie de personne réelle le modèle dois rester le plus terre-à-terre. Au risque de perdre ça touche “humaine” ou “créative” il restera plus proche de la littérature médical. Réduisant ici les chances de remettre un mauvais résultats ou une réponse qui serait mal interprété.
Max new token 75: Avec ce paramètre nous limitons la longueur et la quantité d’information retourné par le chat bot. Cette limite nous permet d’avoir des réponses que nous considérons complète tout en restant le plus simple possible. Ce n’est pas un docteur il doit seulement guider l’utilisateur vers les services publiques ou la médicamentation maison. Si les réponses sont longues et complexes 
Décrire les expérimentations faites ayant mené à la logique derrière votre bot / Describe the experiments carried out that led to the logic behind your bot

Itération de type recherche booléenne pour ajuster les hyper-paramètres de “max_new_token” et “temperature”.






SCÉNARIO 1

Notre prompt : You are my medical assistant. My symptoms are : runny nose, fever, wheezing, decrease in appetite and sneezing. What is my diagnostic?
Réponse