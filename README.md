In the main directory of the project, [mian.py](main.py) is the main entrance of the program. You can execute it directly or enter the following through the command line.
```python
python3 main.py -i file.smi -o output
-i represents the name of the input file
-o represents the name of the output file.
```
Of course, the prerequisite for operation is that there are already trained files for use.
The SAscore model can be trained by [sa_dbn.py](SAscore/sa_dbn.py) located in the SAscore directory. Using the
following command line.
```python3
python3 sa dbn.py -i file.smi.
```
Same as Toxscore.