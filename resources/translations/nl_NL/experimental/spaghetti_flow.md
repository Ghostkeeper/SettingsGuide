Spaghettivulling
====
Met deze instelling wordt de dichtheid van de spaghettivulling direct aangepast.

Normaal gesproken heeft de instelling [Infill Density](../infill/infill_sparse_density.md) bij het printen van vullingen alleen invloed op de [Afstand tussen opvullijnen](../infill/infill_line_distance.md). Omdat de [Lijnbreedte Vulling](../resolution/infill_line_width.md) hetzelfde blijft, maar de lijnen dichter bij elkaar liggen, zal het verhogen van de infill-dichtheid ertoe leiden dat meer van het infill-volume met materiaal wordt gevuld.

Dit werkt anders wanneer [Spaghetti Infill](spaghetti_infill_enabled.md) is ingeschakeld. Vullijnafstand past niet alleen de afstand tussen opvullijnen aan, maar ook de lijnbreedte om de gewenste dichtheid te bereiken die door deze instelling wordt gespecificeerd. Deze instelling specificeert precies het aandeel van het totale vulvolume dat met materiaal moet worden gevuld. Als u deze instelling verhoogt, worden de lijnen breder.

Wanneer u spaghettivulling gebruikt om flexibele vulling te maken, bepaalt deze instelling in wezen hoe stijf de vulling zal zijn. Het verminderen van de stroom resulteert in een zachtere vulling, terwijl het verhogen van de stroom de vulling stijver maakt. Als u de stroom echter te veel vermindert, wordt de vulling niet meer gelijkmatig verdeeld. Het heeft de neiging om naar de bodem van het volume te vallen en daar stapels spaghetti te vormen die niet bijdragen aan de stijfheid van de bovenkant.

Wanneer u spaghettivulling gebruikt om materiaal te gieten, moet deze instelling waarschijnlijk dicht bij 100% worden ingesteld om het model volledig met materiaal te vullen. U kunt deze waarde echter nog enigszins aanpassen als uw materiaal tijdens het uitharden de neiging heeft te krimpen of uit te zetten.

**Deze instelling wordt vermenigvuldigd met de instelling [Infill doorvoer](../material/infill_material_flow.md).**