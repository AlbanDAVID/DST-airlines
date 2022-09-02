# DST Dashboard

### Rationale
This readme serves as reference for the functionality of the dashboard linked to the DST Airlines project. This dashboard represents the culmination of our team's effort to implement a functional data pipeline since it is the data consumption part of said project

## Summary
#### I - Install and Usage
#### II - Components and general architecture of the code
#### III - Upcoming features and improvements 
## I - Install and Usage
This section describes how to install the necessary python modules in order to be able to launch the dashboard and also 
how to run the dashboard locally
### Install 
Run the following command lines in order to install necessary python modules
```
cd path/to/DST_airlines/src/
pip install -r requirements.txt 
```
Run the following command lines to run the dashboard at `127.0.0.1:8050`
```
cd path/to/DST_airlines/src/dst_dashboard/
python main.py
```



## II - Components and general architecture of the code 
This section describes the code's file Tree and gives you a quick overlook of the code's architecture

### Code architecture 
The dashboard's code architecture is based upon the idea of scalability. We chose the `Dash` framework because it provides
easy access to mature technologies 
* **Flask** a micro Python web framework. 
* **Plotly** a D3-based graphics library.

It enables us to implement an `html` based front end in which we can insert various data visualizations.
In order to structure said `html` we chose to base the repartition of the display in `cards` which contain `rows` and `columns`. 
In the same fashion as in bare `html` code, we can insert various graphical elements in the `rows` and `columns` thus populating the `cards`. 
Each `card` represents a basic "tile" of the dashboard (the tiles being `cards`). Each tile depends on the nature of the `data` it's consuming, the 
type of information it's providing  and the frequency of update of the data with the end-user in mind. While those elements can vary
depending on the user's needs, this `card` based system enables easy refactoring of the code : changing
the content of our tiles comes without any `css` or `html` remodeling overhead.

### Files 

```
dst_dashboard
├── README.md       
├── dashboard.py    
├── dst_static.py
├── dst_variable.py
├── main.py
└── query_data.py
```
* `dashboard.py` serves as a distribution unit. While it does not contain much code per say, it enables us to `import` the `app` 
into different files, thus we can implement graphical callbacks for the same app in different files avoiding any 
`import loop`
* `dst_static` implements the graphical elements of the static data based visualizations 
* `dst_variable` implements the graphical elements of the variable data based visualizations 
* `query_data.py` implements the querying of the database and serves all the other files with the needed `dataframes`
* `main.py` outer frame html code and entry point of the dashboard

## III - Features and upcoming improvements 

If you take a look at the previous section you will understand that it is quite easy to add and to remove features at will. For now we have:
* Airport information
* Live flight information
* Data table (via search bar single flight or bulk)
* flight trajectories

And here is a short list of what we would like to see in the future :
* Arrival and Departure dates  
* Weather information
* Statistics

Along with the list of new features will come remodeling of the old ones to get better use out of them