#!/bin/bash
#takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s "{$1}" -X POST -d "X-HolbertonSchool-User-Id=98&subject=I will always be here for PLD"
