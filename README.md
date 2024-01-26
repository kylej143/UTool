# What is this?
This is a .txt file (.tex is also a txt file) editor that will automatically edit your file in the format for Simulate in Logism.

It solves: Project -> Analyze Circuit -> Export Table, this returns a txt file, which doesn't work when importing it to use for the Simulate.

or

You can also copy paste the body of a tex file format table (see picture below) as a tex file or txt (same thing).

![TTC.png](image%2FTTC.png)

# How to use?
Run it on python! (preferably)

1. Git Clone or Copy the src/truthtable_converter into your directory.
2. With Python run main.py (src/truthtable_converter/main.py)

*NOT RECOMMENDED*
TO Download TTconverter.exe, or other format, you need to disable your security while you do it. (Your antivirus will probably mark it as a virus) (Trojan:Win32/Wacatac.B!ml) (Hurray for Machine Learning False Positives!)

See below for example on what the logism/tex file should look like:
(and yes the \hline is needed)

![logismformat.png](image%2Flogismformat.png)
![texformat.png](image%2Ftexformat.png)
