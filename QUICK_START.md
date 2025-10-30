# ✨ Introducing  Prevue™

Prevue™ will draw an innovative flowchart that hugs your Python
code.  This flowchart lets you see the <b>flow of control</b> within
your script.  An SVG image file is created by Prevue™ for this
purpose.  The image file can be seen in a browser or document viewer.

## ✨ Prevue™  Quick Start

1. Visit:    https://github.com/gezmanick/Prevue

2. Click the green  <b>[  <>  Code  ]</b>  button

3. Click on   <b>Download ZIP</b>   at bottom of drop-down menu

4. Save and extract the ZIP file:
   
       • Windows:  right-click → Extract All…
       • macOS:  double-click the ZIP
       • Linux:  download  Prevue-main.zip

5. Further Terminal commands for Linux:
   
           cd ~/Downloads
           mv Prevue-main.zip ~/prevue.zip
           cd ~
           unzip prevue.zip
           cd prevue
           ls -l

6. Among other files in folder `prevue` you will find:
   
       • pv.py – the `main` Prevue™ program
       • pvi.py – a module that pv imports
       • prevue_documentation.html  and supporting files

7. Install `svgwrite` via this Terminal command:
   
          pip install svgwrite

8. Run Prevue™ from the extracted folder, for example:
   
          python3  pv.py  sort_fcns.py

## ✨ Extra Steps For A Better Way To Run Prevue™

9. Do steps 1 to 6 in the **Quick Start** (see above)

10. If you don't have a folder named `bin` in your home
      folder, then create it via 2 Terminal commands:
    
          cd ~
          mkdir bin

11. Copy two Prevue™ files to `bin` via 3 Terminal commands:
    
          cd ~/bin
          cp /path/to/prevue/pv  .
          cp /path/to/prevue/pvi.py  .

12. Run Prevue™ from within any folder that contains `sort_fcns.py`:
    
          pv sort_fcns.py

## ✨ Test  Prevue™

13. Step 12 will create a file named  `sort_fcns.py.svg`
      To check that Prevue™ is working, execute the following
      Terminal compare command:
    
          cmp  sort_fcns.py.svg  sort_fcns.svg
    
     If no output is generated, it means that the two
     files are identical.

## ✨ To See Image Files

14. Both `.svg` and `.pdf` image files can be viewed on most 
      browsers including  Chrome, Chromium, Firefox and Brave.

## ✨ Why Prevue™ Is Cool

    •  It draws flow diagrams to enhance Python code
    •  Works offline, with no dependencies beyond svgwrite
    •  Useful for teaching, debugging, and documentation
    •  Offers powerful benefits with an easy learning curve
    •  Can make general-purpose flowcharts  not just Python
    •  Can be used as a flow-chart framework for writing
       better pseudo-code in any programming language

## ✨ To Learn More

Read the unzipped `README.txt` and
`prevue_documentation.html` files.

## ✨ Contact / Feedback

r.e.hilburger@gmail.com
