# Pangenomics
A tool software that allows users to build their own database and provide visualization of genomic collinearity, genomic structural variation and pangene families.
## Example

<div algin="center">
  <img src="https://github.com/Kai-Maker1/Pangenomics/blob/main/images/example.png" width=100% height=25%>
</div>  

## Installation
The easiest way to install pangenomics is to download the latest binary from the releases and make sure to chmod +x the resulting binary.
If you are using go, you can build from source with:
```python
go get -u -t -v github.com/Kai-Maker1/Pangenomics/...
go install github.com/Kai-Maker1/Pangenomics/cmd/Pangenomics
```
## Usage
[Database](#部分标题)  
The visualization tool provides users with automatic database generation scripts, and users can complete the database construction process by themselves.
```python
python3 Pangenomics/analysis/CreateAlignment_DB.py
python3 Pangenomics/analysis/CreateSV_DB.py
python3 Pangenomics/analysis/CreatePangenomeCluster_DB.py
```
Before creating a database, you need to save the database file in the corresponding folder.
```python
cp -r yourpath/alignemnetdata Pangenomics/analysis/PangenomeAlignmentResult
cp -r yourpath/svdata Pangenomics/analysis/PangenomeSVResult
cp -r yourpath/pangenomefamilies Pangenomics/analysis/PangenomeFamiliesResult
```
[Flask](#部分标题)  
Install the flask environment before starting the background
```python
pip install flask
```
