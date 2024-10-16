#!/bin/bash

set -euxo pipefail

exec flask run -h 0.0.0.0 -p 5000 --reload
