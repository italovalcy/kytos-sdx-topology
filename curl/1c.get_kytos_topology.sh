#!/bin/bash
TOPOLOGY_API="http://0.0.0.0:8383/api/kytos/topology/v3"
echo "##### kytos link  topology #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API

