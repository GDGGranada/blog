# GDG Granada

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=plastic)]() [![Maintenance](https://img.shields.io/maintenance/yes/2017.svg?style=plastic)]() [![Maintenance](https://img.shields.io/badge/Hugo-0.20.6-blue.svg?style=plastic)]()

![Google Developer Group Granada](logo.jpg)

This is the website of [Google Developer Group Granada](http://gdggranada.com).

## How to run it
To run the site you need to install [Hugo](https://gohugo.io/). To generate the website, go to ``src`` and run:
```shell
hugo
```

To run in a development server:
```shell
hugo serve
```

## events.py
This script gets all the events from [our Meetup page](https://www.meetup.com/es-ES/GDG_Granada/) and converts them to Markdown format. You will need to do some changes with the result.

### Requirements
In order to run the script, you will need to install:
* tomd
* requests

## License
#### MIT License

Copyright (c) 2017 David Sánchez Jiménez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
