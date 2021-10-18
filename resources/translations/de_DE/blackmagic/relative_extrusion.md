Relative Extrusion
====
Cura schreibt Befehle für den Drucker, um Ihr Objekt in G-Code zu drucken. Diese Befehle bewegen den Druckkopf an bestimmte Positionen und schalten den Einzug ein. Normalerweise speichert Cura sowohl die Koordinaten für die Bewegung des Druckkopfes als auch die Position des Vorschubs als absolute Koordinaten. Wenn diese Einstellung jedoch aktiviert ist, werden die Koordinaten für den Einzug relativ aufgezeichnet.

Wenn dies deaktiviert ist (d.h. absolute Extrusion), wird die Position des Filaments zu Beginn des Drucks als Nullkoordinate festgehalten. Die Position des Filaments nimmt im Laufe der Datei zu, wenn mehr Material extrudiert wird und sich das Filament immer weiter vom Startpunkt am Anfang des Drucks entfernen muss.

Wenn dies jedoch aktiviert ist, wird die Extrusion in jeder einzelnen Zeile des G-Codes separat geschrieben, relativ zur Position der vorherigen Zeile. Jede Linie enthält dann nur die Menge an Material, die für diese spezielle Linie extrudiert wurde.

Die relative Extrusion erleichtert die Bearbeitung des G-Codes, nachdem er erstellt worden ist. Wenn irgendwo dazwischen zusätzliches Material extrudiert werden muss (um Liniensegmente hinzuzufügen oder zu entfernen oder um die Fließgeschwindigkeit anzupassen), muss die neue Extrusion einfach in das zu bearbeitende Teil geschrieben werden. Wenn eine absolute Extrusion verwendet wird, muss die Position des Extruders anschließend mit G92 zurückgesetzt werden, um sicherzustellen, dass alle nachfolgenden Befehle korrekt sind.

Wenn jedoch zu irgendeinem Zeitpunkt während der Verarbeitung des G-Codes (in Cura, der Firmware oder der Bewegung) Rundungsfehler auftreten, wird die absolute Extrusion diese in der nächsten Zeile automatisch korrigieren. Bei der relativen Extrusion führt dies zu einer Über- oder Unterextrusion, wenn auch in sehr geringem Maße.

Nicht jede Drucker-Firmware unterstützt die relative Extrusion.

**Wenn absolute Extrusion verwendet wird, setzt Cura die Filamentposition alle 10 Meter zurück, um Fließkomma-Rundungsfehler in der Firmware zu vermeiden.**