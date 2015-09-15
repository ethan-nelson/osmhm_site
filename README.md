OpenStreetMap Hall Monitor
==================

Introduction
------------

OpenStreetMap Hall Monitor (OSMHM) is a passive monitoring tool for OpenStreetMap. It boasts a suite of filters, including vandalism/spam/unauthorized import detection. OSMHM works by downloading and scanning hourly diff files from OSM.

A Procfile is included for easy deployment to Heroku.


Installing
---------------

Note: Python and the virtualenv package are required.

- cd osm-hall-monitor

- virtualenv env

- env/bin/python setup.py develop

- env/bin/initialize_osmhm_db development.ini

- env/bin/pserve development.ini

Dependencies include [OSM Diff Tool](https://github.com/ethan-nelson/osm_diff_tool) and [OSM Hall Monitor](https://github.com/ethan-nelson/osm_hall_monitor).
