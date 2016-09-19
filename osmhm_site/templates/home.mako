<%inherit file="base.mako"/>
<%block name="header">
</%block>
<%block name="content">
<h1 class="page-header">Welcome to the OpenStreetMap Hall Monitor</h1>
<p>OpenStreetMap Hall Monitor is a passive monitoring tool for OSM, scouring planet diff files in search for events you are interested.</p>

<p>To get started, <a href="${request.route_path('login')}">log in</a> via OpenStreetMap. Once logged in, use the header links to add any objects, users, or tags you are interested in tracking to their respective watchlists.</p>

<p>To view the source code or report any bugs, check out the <a href="http://github.com/ethan-nelson/osmhm_site" target="_blank">web frontend</a> and <a href="http://github.com/ethan-nelson/osm_hall_monitor" target="_blank">analysis code</a> repositories on GitHub.</p>
</%block>
