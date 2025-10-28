
                🔑 Setting Up Prevue™
                ~~~~~~~~~~~~~~~~~~~~~

A zip file is a single file, with the extension `.zip`
that holds many other files within it.  The zip file for
Prevue™ is named `prevue.zip`.

`prevue.zip` must be unzipped into a folder that is
directly below the home folder.  So, if your name is
Alan, then you probably have a folder named /home/Alan.
In that case, you must create a folder named `prevue`
that is located just below ~ which is shorthand for your
home folder.  The following two Terminal commands can be
used for that purpose:

         cd ~
         mkdir prevue

Now, you must get into the prevue folder, move the
prevue.zip file to the `current folder`, which is
denoted by `.`, and unzip the `preview.zip` file into
the current folder via:

         cd prevue
         mv /path/to/prevue.zip .
         unzip prevue.zip

Because Prevue™ depends on svgwrite, you must install
svgwrite.  To do that, give this Terminal command.

         pip install svgwrite

If you don't already have `pip`, then you must install
that too.  Ask any AI model how to do that.

After unzipping, copy pv and pvi.py to your ~/bin folder.
If it doesn't exist, create it via:

         cd ~
         mkdir bin

Now copy pv and pvi.py to your ~/bin folder via:

         cd bin
         cp ../svgwrite/pv .
         cp ../svgwrite/pvi.py .

Now, Prevue™ is "installed".


🔑 Using Prevue™
~~~~~~~~~~~~~~~~

Suppose you have a Python script named `planner.py` that
you are developing.  Now, suppose you wish to see it
flowcharted by Prevue™.  You can get into the folder where
`planner.py` is located, and give the following command:

         pv  planner.py

The file `planner.svg` will be generated and put into the
same folder as `planner.py`.  To view `planner.svg`, load
it into a browser or a document viewer such as Okular.

Much more info about using Prevue™ is located in the
HTML file named `prevueMH.html`, which can be loaded
into a browser such as Firefox, and read.  Please see
file LICENSE.txt for restrictions on the use of Prevue™.

                        ~~~~