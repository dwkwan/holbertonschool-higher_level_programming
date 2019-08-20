#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the bodyof the response
curl -s $1 --include | grep -i Content-Length | awk '{print $2}'
