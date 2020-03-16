Vitesse maximale pour l'égalisation du débit
===

Si le paramètre [Égaliser le débit de filaments](./speed_equalize_flow_enabled.md) est activé, alors la technique de remplissage de petits espaces ajustera sa vitesse de manière à ce que le débit sortant de la buse soit égal à celui de la peau, même si les lignes sont beaucoup plus fines.

Le problème est que des lignes très fines peuvent entraîner des vitesses extrêmement élevées. Ces vitesses peuvent ne pas être atteintes par l'imprimante, ce qui entraîne des pertes de pas et, en fin de compte, un décalage des couches. Ce réglage fixe un maximum pour ces vitesses.

Comme les petits espaces ont tendance à être petits par nature, les lignes tracées à ces vitesses élevées sont généralement courtes également. Cela signifie qu'en raison des limites d'accélération, la buse ne pourra de toute façon pas atteindre les vitesses élevées. Ce réglage n'a normalement un effet que sur les impressions mécaniques droites où la technique de remplissage des espaces remplit de longues fentes droites entre deux parois qui sont trop petites pour que la buse puisse imprimer.
