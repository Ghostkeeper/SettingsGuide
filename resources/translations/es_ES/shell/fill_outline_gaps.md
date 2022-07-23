Imprimir paredes finas
====
Normalmente, Cura omitirá las paredes que sean más delgadas que el <!--if cura_version<5.0:[Outer Wall Line Width](../resolution/wall_line_width_0.md)--><!--if cura_version>=5.0-->[Minimum Odd Wall Line Width](min_odd_wall_line_width.md)<!--endif-->, descartándolas por ser demasiado pequeñas para imprimir.

Si esta configuración está activada, Cura intentará imprimir estas piezas de todos modos. La impresión resultante será imprecisa<!--si cura_version<5.0: y desordenada-->, pero debería producir la forma deseada con cierta fiabilidad.

![Algunas piezas son demasiado finas para imprimir](../images/fill_outline_gaps_disabled.png)
Con este ajuste activado, incluso las partes delgadas se imprimirán](../images/fill_outline_gaps_enabled.png)

<!--if cura_version<5.0:
Las piezas diminutas se rellenan con líneas extremadamente finas. Estas líneas se combinan si son adyacentes entre sí y no son demasiado largas. Esto funciona para muchos casos, pero en algunos casos produce un diminuto zig zag, aumentando significativamente el tiempo de impresión.

Es aconsejable, antes de recurrir a esta configuración, intentar ajustar ligeramente el ancho de la línea de la pared exterior. Si su pieza es ligeramente más fina que un ancho de línea, puede dar un mejor resultado si reduce el ancho de línea de la pared exterior de toda la impresión, de manera que las partes finas se impriman normalmente. Sin embargo, reducir el ancho de la línea demasiado lejos hará que el material fluya de forma poco fiable, lo que provocará una subextrusión.
-->
<! --if cura_version>=5.0-->
Las piezas finas se imprimen utilizando una línea de pared muy fina. Sin embargo, esta línea fina puede no imprimirse bien. Para remediarlo, también existe el [Ancho mínimo de la línea de pared fina](min_bead_width.md). Este ajuste proporciona un límite inferior para el ancho de la línea. Si es más fino, la línea se imprimirá demasiado gruesa, teóricamente imprimiendo más allá de los límites del modelo, pero al menos debería imprimirse de forma fiable. Todo lo que sea más fino que el [Tamaño mínimo de la característica](min_feature_size.md) no se imprimirá en absoluto.
<!--endif-->

**Esto sólo intentará imprimir piezas que sean delgadas en el plano horizontal. Para piezas delgadas en la dirección Z, consulte la configuración de [Tolerancia de segmentación](../experimental/slicing_tolerance.md) o reduzca la altura de la capa.**