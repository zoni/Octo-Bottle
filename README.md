Octo Bottle
===========

*A plugin to embed the [Bottle] micro web-framework within [Octo].*


Usage
-----

It is assumed that you already have *octo* installed. If not, you should [install](http://octo.zoni.nl/#installing) that first.

With octo installed, just clone or download this repository to a location of your choice, then start octo with this directory in your list of plugin directories, like so:

    # Obtain a copy of Octo Bottle
    git clone https://github.com/zoni/Octo-Bottle.git
    
    # Or if you prefer a flat download
    wget https://github.com/zoni/Octo-Bottle/archive/master.zip
    unzip master.zip
    
    # Run octo with it (substitute Octo-Bottle with Octo-Bottle-master 
    # if you downloaded the zipfile instead)
    octo Octo-Bottle

At this point, any other plugins you have may simply `import bottle` and use it's decorators as described in Bottle's documentation.


Configuration
-------------

Configuration can be done by editing `octobottle.octoplugin`. Here you can change the interface to listen on, the port to listen on and the serveradapter to use.


Deployment
----------

For production deployments, it is recommended to place bottle behind some kind of reverse proxy or loadbalancer.


License
-------

Octo Bottle is available under a 2-clause BSD license (the "Simplified BSD License"):

	Copyright (c) 2013, Nick Groenen
	All rights reserved.

	Redistribution and use in source and binary forms, with or without
	modification, are permitted provided that the following conditions are met:
		* Redistributions of source code must retain the above copyright
		  notice, this list of conditions and the following disclaimer.
		* Redistributions in binary form must reproduce the above copyright
		  notice, this list of conditions and the following disclaimer in the
		  documentation and/or other materials provided with the distribution.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDER(S) BE LIABLE FOR ANY
	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




[Octo]: http://octo.zoni.nl/
[Bottle]: http://bottlepy.org/