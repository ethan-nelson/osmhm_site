OpenStreetMap Hall Monitor Site
===============================

Introduction
------------

This is a frontend for use with the [OSM Hall Monitor](https://github.com/ethan-nelson/osm_hall_monitor) monitoring package. Rather than using a command line to add things to track or to view log events, the website provides the ability to add any trackable things, review log events, and support restrictions to this data via OSM authentication. 

Installing
----------

Note: Python is required and virtualenv is _strongly_ recommended..

- cd osmhm_site

- virtualenv env

- env/bin/python setup.py develop

- env/bin/initialize_osmhm_db development.ini

- env/bin/pserve development.ini

Dependencies include [OSM Diff Tool](https://github.com/ethan-nelson/osm_diff_tool) and [OSM Hall Monitor](https://github.com/ethan-nelson/osm_hall_monitor).
