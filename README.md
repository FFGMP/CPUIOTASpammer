# CPUIOTASpammer


## Tutorial:

### How to run IRI 

#### Locally

Running IRI is quick and easy, and you can usually run it without admin rights.
Below is a list of command line options.

At a minimum, the port must be specified on the command-line — e.g., '`-p 14265`' 
or in the `iota.ini` file — e.g., '`PORT = 14265`'.

If the '`iota.ini`' file exists, it will be read.
The port and all the command line options below take precedence over values specified in the ini config file.

Here is an example script that specifies only the port, with all other setting to be read from the ini file **if it exists**:

```
java -jar iri.jar -p 14265
```
## With IRI running

### Install:

```
pip install pyota
```

### Change:
```
address = 'RANDOM ADDRESS'
```
```
RoutingWrapper('PUBLIC NODE')
```
```
seed = b'RANDOM SEED HERE'
```
```
os.system('python DirectoryOfTheFile/file.py')
```
After that you can run your Python Script.

## TorSpammer

Just install torsocks and do the steps above.
 
