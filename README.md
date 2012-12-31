Cosm & iDigi Web Connector
==========================

https://github.com/jordanh/cosmidigi

[iDigi][iDigi] is awesome for connecting and managing devices. [Cosm][Cosm]
is a great way to collect, present, share and trigger on information. Wouldn't
it be great if you could somehow marry the two?

The cosmidigi project is a very simple web application which allows you to
publish data from iDigi to the Cosm service.

[iDigi]: http://www.idigi.com
[Cosm]: http://www.cosm.com


Requirements
------------

  * Python v2.6 or greater
  * The [bottle][bottle] framework
  * The [requests][requests] framework

[bottle]: http://bottlepy.org/docs/dev/
[requests]: http://docs.python-requests.org/en/latest/

Installation
------------

There are two ways to run the application: as a stand-alone application
on its own port and as a subordinate CGI application running under the
Apache web server.

To run the application in stand-alone mode simply run app/main.py.

To run the application under your web server, place the files in a
directory which can be served by your webseriver. Ensure that CGI
is enabled for this directory, cross your fingers and access the
URL of the directory from a web browser. You should see a "Hello, world."
message.

Usage
-----

  1. Setup your data feeds on Cosm.

  2. Edit the cfg/config.py file to configure which data from iDigi
     is replicated to Cosm.

  3. Register a Monitor API request with iDigi to push DataPoint
     data to your web application. Consult the doc/ directory for
     examples.

  4. Enjoy your connected world!

Todo
----

  * Support more than one Cosm feed id/API key

  * Utilize auth-basic and https connectivity from iDigi

  * Allow from the republishing of data *back* to iDigi onces its
    been transformed; there's a lot of usefulness in that

License
-------

This software is open-source software.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.

