# Prevue™

**Prevue™** is a Python tool that automatically generates clear, SVG-based flowcharts directly from your Python source code — no manual drawing required.

🌐 **Learn more here:** [https://bit.ly/prevue-info](https://bit.ly/prevue-info)
*(This link redirects safely to the official GitHub Pages site: gezmanick.github.io/Prevue)*

---

### Highlights

- Converts Python source into detailed, structured flowcharts
- Highlights control flow (loops, conditionals, returns) for better readability
- Produces clean SVG output you can view or edit anywhere
- Ideal for learners, educators, and developers documenting code

# ✨ Introducing  Prevue™

Prevue™ will draw an innovative flowchart that hugs your Python
code.  This flowchart lets you see the <b>flow of control</b> within
your script.  An SVG image file is created by Prevue™ for this
purpose.  The image file can be seen in a browser or document viewer.

## ✨ Quick Start to Get & Try Prevue™

1. Visit:    https://github.com/gezmanick/Prevue

2. Click the green  <b>[  <>  Code  ]</b>  button

3. Click on   <b>Download ZIP</b>   at bottom of drop-down menu

4. Save and extract the ZIP file:</br>
   
       • Windows:  right-click → Extract All…</br>
       • macOS:  double-click the ZIP</br>
       • Linux:  download  Prevue-main.zip

5. Further Terminal commands for Linux:</br>
   
       <code> cd ~/Downloads</code></br>
       <code> mv Prevue-main.zip ~/prevue.zip</code></br>
       <code> cd ~</code></br>
       <code> unzip prevue.zip</code></br>
       <code> cd prevue</code></br>
       <code> ls -l</code></br>

6. Among other files in folder `prevue` you will find:</br>
   
       • pv.py – the `main` Prevue™ program</br>
       • pvi.py – a module that pv imports</br>
       • prevue_documentation.html  and supporting files</br>

7. Install svgwrite via this Terminal command:
   
       <code>pip install svgwrite</code>

8. Run Prevue™ from the extracted folder, for example:
   
       <code>python3  pv.py  sort_fcns.py</code>

## ✨ Extra Steps For A Better Way To Run Prevue™

9. Do steps 1 to 6 in the Quick Start (see above)

10. If you don't have a folder named bin in your home</br>
      folder, then create it via 2 Terminal commands:
    
       <code>cd ~</code></br>
       <code>mkdir bin</code>

11. Copy two Prevue™ files to bin via 3 Terminal commands:
    
       <code>cd ~/bin</code></br>
       <code>cp /path/to/prevue/pv  .</code></br>
       <code>cp /path/to/prevue/pvi.py  .</code>

12. Run Prevue™ from within any folder that contains sort_fcns.py:
    
       <code>pv sort_fcns.py</code>

## ✨ Test  Prevue™

13. Step 12 will create a file named  <b>sort_fcns.py.svg</b></br>
      To check that Prevue™ is working, execute the following</br>
      Terminal `compare` command:
    
       <code>cmp  sort_fcns.py.svg  sort_fcns.svg</code>
    
     If no output is generated, it means that the two</br>
     files are identical.

## ✨ To See Image Files

14. Both .svg and .pdf image files can be viewed on most browsers</br>
      including  Chrome, Chromium, Firefox and Brave.

## ✨ Why Prevue™ Is Cool

 •  It draws flow diagrams to enhance Python code</br>
 •  Works offline, with no dependencies beyond svgwrite</br>
 •  Useful for teaching, debugging, and documentation</br>
 •  Offers powerful benefits with an easy learning curve</br>
 •  Can make general-purpose flowcharts  not just Python</br>
 •  Can be used as a flow-chart framework for writing</br>
      better pseudo-code in any programming language

## ✨ To Learn More

Read the unzipped README.txt and</br>
prevue_documentation.html files.

## ✨ Contact / Feedback

r.e.hilburger@gmail.com
