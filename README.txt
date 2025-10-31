
                🔑 Setting Up Prevue™
                ~~~~~~~~~~~~~~~~~~~~~

These are linux-oriented instructions.  My assumption
is that you know how to execute Terminal commands.

A zip file is a single file, with the extension `.zip`
that holds many other files within it.  The zip file for
Prevue™ is named `Prevue-main.zip`.  After you download
it, get into your home folder:

        cd ~

Move `Prevue-main.zip` to your current folder (home): 

        mv /path/to/Prevue-main.zip .

Change the name to `prevue.zip` via:

        mv Prevue-main.zip prevue.zip

Unzip prevue.zip and thus create the folder `prevue`:

        unzip prevue.zip

The contents are now unzipped into the `prevue` folder.

Because Prevue™ depends on a package named `svgwrite`, 
you must install `svgwrite`.  To do that, give this 
Terminal command:

         pip install svgwrite

If you don't already have `pip`, then you must install
that too.  Ask any AI model how to do that for your
computer operating system.

After unzipping, copy pv and pvi.py to your ~/bin folder.
If it doesn't exist, create it via:

         cd ~
         mkdir bin

Now copy pv and pvi.py to your ~/bin folder via:

         cd bin
         cp ../prevue/pv .
         cp ../prevue/pvi.py .

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
file named `prevue_documentation.html`.  That file is
in the `prevue` folder.

SVG and PDF image files can be seen in a browser such as
Firefox, Brave, or Chrome.  Please see the file LICENSE.txt
for restrictions on the use of Prevue™.
                        ~~~~
