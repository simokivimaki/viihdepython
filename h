[33mcommit cd1bc3f05f5dc4fba432aa02b9a91261d1ee1646[m
Author: kattelus <mataka@iki.fi>
Date:   Sun Oct 30 19:16:59 2016 +0200

    pybuilder and installable scripts etc

[33mcommit 21d9791fe1ff8e4685737a9d3a57cfc3e4d925fc[m
Author: kattelus <mataka@iki.fi>
Date:   Sun Oct 30 18:46:14 2016 +0200

    pybuilder and installable scripts etc

[33mcommit a3b63bae66b2699a04b4685ca9967fafc783e0c3[m
Author: kattelus <mataka@iki.fi>
Date:   Sun Oct 30 18:21:41 2016 +0200

    pybuilder and installable scripts etc

[33mcommit cdccc33d6bea6db1ca5aed8053d04ba3430116c8[m
Author: kattelus <mataka@iki.fi>
Date:   Sun Oct 30 18:15:25 2016 +0200

    pybuilder and installable scripts etc

[33mcommit 4532bb1a5389aff11d24ed355c839328be549e05[m
Author: kattelus <mataka@iki.fi>
Date:   Sun Oct 30 17:44:59 2016 +0200

    pybuilder and installable scripts etc

[33mcommit c0b0e1f652f29cbbb88ffca8d8c8f331b618f8b2[m
Author: kattelus <mataka@iki.fi>
Date:   Sun Oct 30 17:43:48 2016 +0200

    pybuilder and installable scripts etc

[33mcommit c5a21077803573398ab18200ba3a20f0de2109c4[m
Author: kattelus <mataka@iki.fi>
Date:   Wed Sep 28 21:08:48 2016 +0300

    pyb

[33mcommit ee0a2db3d7056cad713da48e7e43ee84f36804f1[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Nov 29 22:03:10 2015 +0200

    refactored some command line handling
    - introduced new cli.py helper module
    - using sys.stdin.encoding instead of utf-8 when reading user input
    - Elisaviihde class does not depend from command line
    - todo: the main scripts should use only cli.py for command line input

[33mcommit 465016cd0e08e8d2d983c9a5002d60735bbb5ea5[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sat Nov 28 22:46:03 2015 +0200

    move_simpsonit.py uses argparser, some coding style fixes

[33mcommit 41917a017935473adbaa5bd6b83f8cbb2da480e8[m
Merge: d49df0a 7ac0a3c
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sat Nov 28 20:27:44 2015 +0200

    Merge pull request #1 from kattelus/master
    
    Added possibility give input params as command line arguments

[33mcommit 7ac0a3c9cb2e8b14f4d85ba5d48b2de429c18674[m
Author: kattelus <mataka@iki.fi>
Date:   Wed Nov 25 22:33:03 2015 +0200

    Added possibility to give program inputs as command line paramters

[33mcommit 5d44c37cc72a9771abdceef650ec1fcc6109c560[m
Author: kattelus <mataka@iki.fi>
Date:   Wed Nov 25 22:28:52 2015 +0200

    Added possibility to give program inputs as command line paramters

[33mcommit d49df0a4820942fa427b0f25a890dccb3287b445[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun May 3 21:32:15 2015 +0300

    Works with the new Elisaviihde API.
    - fixed create_subfolder method

[33mcommit 1134dbed8fb6525a72fe27971ebd36cb2e93ce61[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun May 3 19:47:33 2015 +0300

    Works with the new Elisaviihde API.

[33mcommit 946d45c4869552d05e624413e1aff28fb56c79da[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Mon Dec 8 20:31:16 2014 +0200

    Trim strings when detecting duplicates.

[33mcommit 2a86c1103d9b703c28419441017681d613384b09[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Nov 2 16:35:08 2014 +0200

    Code style fixes.

[33mcommit a5b44d450d0d1663353e9cfa3704564952780d9c[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Nov 2 15:27:50 2014 +0200

    Removed unused code.

[33mcommit f77bf9d2221c8f87c8e635f9a77d34a505aa40af[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Nov 2 15:26:03 2014 +0200

    Fixed parsing for new simponit.org layout.

[33mcommit c13b4a1b20e55df99538979cf0dc08989d6744c9[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Nov 2 14:54:20 2014 +0200

    Fixed utf-8 input in folder name.

[33mcommit db69c0a1d60f5c43f2f96e155a8efdc4af715ae9[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Thu Aug 14 20:03:54 2014 +0300

    Fixed list index out of range when episode name not found.

[33mcommit 6bd3aa7bef20f74be0035cdc6a5be917b0dfc03d[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Mon Mar 10 21:34:42 2014 +0200

    Fixed utf-8 input in folder name.

[33mcommit 655f174913db45e99aaf7c4b423a99be14350862[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Tue Sep 24 17:23:48 2013 +0300

    EPG-tiedoissa ei aina jakson nimeä mukana, joten päätellään kausi esitysajan perusteella.

[33mcommit c668f0b8b97cd039903e1fd71340165bc0f8e99b[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Mon Aug 19 20:06:08 2013 +0300

    tarkennettu kuvausta duplikaattien poistosta

[33mcommit 6b7acc638975d0e7f4170b4949509e158294e26e[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 23:34:53 2013 +0300

    korjattu kirjoitusvirhe

[33mcommit 50202c5b2fc43b50440d162259c0d1c81a0a20d4[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 23:00:47 2013 +0300

    markdown syntax

[33mcommit cab7fc7cd8d8a003c4b621ad2ecca950ac894050[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 22:57:01 2013 +0300

    license

[33mcommit 6bcaf9e3bc374f75484907dbc47671d62152bf90[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 22:54:17 2013 +0300

    license

[33mcommit c5fa8eafd204d4884cf9a806482439ae665aa265[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 22:51:38 2013 +0300

    Käytetyt kirjastot.

[33mcommit 5ad5fdf4ef57d80f472148de575e109f894f53b3[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 22:42:44 2013 +0300

    Korjattu muotoilua toimimaan githubin kanssa paremmin.

[33mcommit 39ac096be6f7eaac025e4995396d7ed37410e5d9[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 22:40:49 2013 +0300

    Päivitetty README

[33mcommit bfc1e0922e880d3db1e6769089540c967f9e3901[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 22:30:33 2013 +0300

    Initial commit: bs4 and request libraries and the Elisa Viihde python scripts.

[33mcommit 83f8d2be657c259127583218d97186673099e61b[m
Author: Simo Kivimäki <simo@kivimaki.fi>
Date:   Sun Aug 18 12:20:14 2013 -0700

    Initial commit
