Alternativní směry stěn
====
Pokud je toto nastavení povoleno, střídá se směr navíjení stěn ve směru a proti směru hodinových ručiček.

První vnitřní stěna bude vytištěna v opačném směru než vnější stěna a druhá vnitřní stěna bude vytištěna opět v opačném směru. A co víc, v další vrstvě se bude začínat také opačně, takže se budou střídat i stěny, které jsou naskládané nad sebou.

Střídání směru tisku snižuje vliv vnitřních napětí uvnitř modelu, čímž se snižuje efekt [deformace](../troubleshooting/warping.md). Během tisku libovolné linie tryska poměrně silně táhne za strunu roztaveného materiálu, čímž se plast natahuje. Během tuhnutí může toto napětí model deformovat. Pokud je sousední linie vytištěna v opačném směru, je toto napětí vyvažováno tahem sousedních linií v opačném směru. Síla napětí je vyvažována napětím v opačném směru.

Nevýhodou střídání směrů stěn je hystereze portálu tiskárny. Pokud je v osách nebo kladkách tiskárny nějaká vůle, pak se při tisku v opačném směru diagonální linie umístí dolů na trochu jiné místo. V důsledku toho bude stěna méně hladká a rozměry tisku méně přesné. U dobře seřízené tiskárny se tento efekt neprojeví, takže pokud má tiskárna utažené řemeny, kladky a přesné součásti, přinese střídání směrů stěn pravděpodobně jen výhody.

Při tisku [zevnitř ven](../shell/inset_direction.md) je při tomto nastavení šev stěny viditelnější a způsobuje určité zvlnění, protože tryska se těsně před začátkem vnější stěny otočí o 180°, což způsobuje vibrace. Při tisku z vnější strany dovnitř se tento efekt neprojevuje.