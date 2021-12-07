Spaghetti-Durchfluss
====
Mit dieser Einstellung wird die Dichte der Spaghetti-Füllung direkt angepasst.

Normalerweise wirkt sich beim Drucken von Füllungen die Einstellung [Fülldichte](../infill/infill_sparse_density.md) nur auf den [Abstand zwischen den Fülllinien](../infill/infill_line_distance.md) aus. Da die [Fülllinienbreite](../resolution/infill_line_width.md) gleich bleibt, die Linien aber enger beieinander liegen, bewirkt eine Erhöhung der Fülldichte, dass am Ende ein größerer Teil des Füllvolumens mit Material gefüllt wird.

Dies funktioniert anders, wenn [Spaghetti-Füllung](spaghetti_infill_enabled.md) aktiviert ist. Der Abstand der Füllungslinien passt nicht nur den Abstand zwischen den Füllungslinien an, sondern auch die Linienbreite, um die gewünschte Dichte zu erreichen, die durch diese Einstellung festgelegt wird. Diese Einstellung gibt genau den Anteil des gesamten Füllungsvolumens an, der mit Material gefüllt werden soll. Wenn Sie diese Einstellung erhöhen, werden die Linien breiter.

Wenn Sie Spaghetti-Füllung verwenden, um flexible Füllung zu erzeugen, bestimmt diese Einstellung im Wesentlichen, wie steif das Füllmaterial sein wird. Eine Verringerung des Durchflusses führt zu einer weicheren Füllung, während eine Erhöhung des Durchflusses die Füllung steifer macht. Wenn Sie den Durchfluss jedoch zu stark reduzieren, wird die Füllung nicht mehr gleichmäßig verteilt. Sie neigt dazu, zum Boden des Volumens hinunterzufallen und dort Spaghetti-Haufen zu bilden, die nicht zur Steifigkeit des Oberteils beitragen. 

Bei der Verwendung von Spaghetti-Füllung zum Gießen von Material sollte diese Einstellung wahrscheinlich auf nahezu 100 % gesetzt werden, um das Modell vollständig mit Material zu füllen. Sie können diesen Wert jedoch noch leicht anpassen, wenn Ihr Material dazu neigt, beim Aushärten zu schrumpfen oder sich auszudehnen.

**Diese Einstellung wird noch mit der Einstellung [Fluss der Füllung](../material/infill_material_flow.md) multipliziert.**