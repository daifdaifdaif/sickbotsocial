*>>>>> dieser saaltext befindet sich noch in arbeit*

# sickbotsocial

sickbotsocial (Jessica 🤖 Jurassica) ist eine interaktive und selbstreferenzielle Medienkunstinstallation auf Twitter, Instagram und [dieyungenhuren.hiv/sickbotsocial](http://www.dieyungenhuren.hiv/sickbotsocial/index2.php). 

Das Script `jj-quote.py` generiert stündlich neue Tweets (Texte kürzer als 280 Zeichen) anhand eines [Random Walk](https://de.wikipedia.org/wiki/Random_Walk) durch gewichtete [Markov-Ketten](https://de.wikipedia.org/wiki/Markow-Kette). Die Parameter des Markov-Skripts werden dabei laufend zufällig verändert, so dass Bot Texte generiert, die kohärent, oder auch wahllos zusammengewürfelt wirken können. 

Als Korpus dient der Twitter-Account von [Jessica Jurassica](http://www.twitter.com/jessicajurassica), deren neue Tweets bei jeder Durchführung des Bot-Skripts dem Korpus hinzugefügt werden. Des Weiteren werden die durch Bot generierten Texte ebenfalls dem Korpus hinzugefügt. Da das Volumen an Bot-Tweets jenes der Tweets von Jessica Jurassica bereits nach ~2 Monaten Laufzeit übertraf, generiert Bot seither Texte, die mehrheitlich auf den bisher generierten Texten basieren.

Die Willkürlichkeit des Markov-Prozesses führt zu einer Unmenge an Resultaten, deren künstlerischer/ästhetischer Wert stark variiert. Eine Selektion dieser Resultate wird durch User-Interaktionen auf Twitter durchgeführt. Favs und Retweets eines Bot-Tweets lösen einen Crosspost des jeweiligen Textes auf dem Instagram-Profil von Bot aus (`tw_favs_to_insta.py`). Twitter-User übernehmen so eine kuratierende Rolle und gestalten eines der Endprodukte (Instagram) aktiv mit. 

### Theorie

*>>>>> hier etwas zu algorithmisch generierten texten, kreativität als reinen selektionsprozess, "alles ist ein remix" einfügen*

### Technische Details

Der auf Github abgelegte Quellcode entspricht der deployed version, die auf einem Raspberry Pi 3b ausgeführt wird. 
